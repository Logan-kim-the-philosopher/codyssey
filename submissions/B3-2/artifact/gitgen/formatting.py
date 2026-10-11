"""구조 검증과 후처리. 내용이 누락되면 오류를 반환한다."""
import re
from .errors import ToolError
from .safety import mask


def clean(text: str) -> str:
    # 터미널 제어문자·ANSI 출력 제거
    return re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', text).strip()


def text_field(data: dict, key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not clean(value):
        raise ToolError(f'생성 결과의 {key} 문자열이 비어 있거나 잘못되었습니다.')
    return clean(value)


def bullets(data: dict, key: str, limit: int | None = None) -> list[str]:
    value = data.get(key)
    if not isinstance(value, list) or not value or any(not isinstance(x, str) or not clean(x).lstrip('-* ').strip() for x in value):
        raise ToolError(f'생성 결과의 {key}에 최소 1개 유효한 불릿이 필요합니다.')
    return [clean(x).lstrip('-* ').strip() for x in value[:limit]]


def format_result(data: dict, command: str, convention: dict, secrets: tuple[str, ...] = ()) -> str:
    summary = text_field(data, 'summary')
    title = mask(text_field(data, 'title'), secrets)
    allowed = '|'.join(re.escape(x) for x in convention['prefixes'])
    scope = convention['scope']
    scope_pattern = re.escape(f'({scope})') if scope else r'(?:\([^()\r\n]+\))?'
    matched = re.fullmatch(rf'((?:{allowed}){scope_pattern}:\s+)(\S.*)', title)
    if not matched:
        raise ToolError('생성 제목이 컨벤션 prefix/scope 규칙과 다릅니다. 맥락·컨벤션을 확인하세요.')
    maximum = 72 if command == 'commit' else 80
    prefix, description = matched.groups()
    available = maximum - len(prefix)
    if available < 2:
        raise ToolError('컨벤션 scope가 너무 길어 제목 설명을 넣을 수 없습니다.')
    if len(description) > available:
        title = prefix + description[:available - 1].rstrip() + '…'
    if command == 'commit':
        body = '\n'.join('- ' + x for x in bullets(data, 'body', 2))
        result = f'--- Change Summary ---\n{summary}\n\n--- Commit Message ---\n{title}\n\n{body}'
    else:
        sections = [('Why', 'why'), ('What', 'what'), ('How to Test', 'how_to_test')]
        body = '\n\n'.join('## ' + heading + '\n' + '\n'.join('- ' + x for x in bullets(data, key)) for heading, key in sections)
        result = f'--- Change Summary ---\n{summary}\n\n--- PR Title ---\n{title}\n\n--- PR Body ---\n{body}'
    return mask(result, secrets) + '\n----------------------\n[REVIEW] AI 초안입니다. 변경 사실·제목·테스트 방법을 검토 후 적용하세요.\n'
