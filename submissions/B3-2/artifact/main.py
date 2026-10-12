#!/usr/bin/env python3
"""Git 프로젝트 루트에서 실행하는 AI 커밋/PR 초안 생성기."""
import argparse
import json
import math
import os
from pathlib import Path
import sys
from gitgen.api import generate, endpoint_for, prepare_payload
from gitgen.errors import ToolError
from gitgen.formatting import clean, format_result
from gitgen.git import collect_changes
from gitgen.prompt import build_payload, load_convention
from gitgen.safety import mask, prepare_diff


def positive(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError('양의 정수가 필요합니다.')
    return number


def temperature_value(value: str) -> float:
    number = float(value)
    if not math.isfinite(number) or not 0 <= number <= 2:
        raise argparse.ArgumentTypeError('temperature는 0~2의 유한한 수입니다.')
    return number


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    result.add_argument('command', choices=('commit', 'pr'))
    result.add_argument('--base-url', default='https://api.openai.com/v1', help='승인된 OpenAI 또는 Codyssey HTTPS /v1 주소')
    result.add_argument('--model', '-model', default='gpt-4.1-mini')
    result.add_argument('--temperature', '-temperature', type=temperature_value, default=0.2)
    result.add_argument('--max-tokens', '-max-tokens', type=positive, default=1200)
    safety = result.add_mutually_exclusive_group()
    safety.add_argument('--safe-mode', '-safe-mode', dest='safe_mode', action='store_true')
    safety.add_argument('--no-safe-mode', dest='safe_mode', action='store_false')
    result.set_defaults(safe_mode=True)
    result.add_argument('--max-files', type=positive, default=10)
    result.add_argument('--max-lines', type=positive, default=200)
    result.add_argument('--why', default='', help='실제 변경 배경')
    result.add_argument('--test-plan', default='', help='사용자가 제시한 테스트 방법; 수행 완료를 뜻하지 않음')
    result.add_argument('--convention', type=Path, help='팀 컨벤션 JSON 경로')
    result.add_argument('--dry-run', action='store_true', help='전송 예정 입력만 확인 (API 호출 0회)')
    result.add_argument('--output', type=Path, help='검토용 초안을 새 파일로 저장; 기존 파일 덮어쓰기 금지')
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    calls = 0
    secrets = tuple(x for x in (os.getenv('AI_API_KEY', ''), os.getenv('OPENAI_API_KEY', '')) if x)
    try:
        endpoint_for(args.base_url)
        key = secrets[0] if secrets else ''
        if not key and not args.dry_run:
            raise ToolError('AI_API_KEY 또는 OPENAI_API_KEY 환경변수가 설정되지 않았습니다.')
        if args.output and args.output.exists():
            raise ToolError('출력 파일이 이미 존재합니다. 새 경로를 지정하세요.')
        changes = collect_changes(Path.cwd())
        if not changes.files:
            print('[INFO] 변경 사항이 없습니다. 초안을 생성하지 않고 종료합니다.')
            return 0
        print(f'[INFO] Git status 수집 완료: {len(changes.files)}개 파일 변경 감지')
        if changes.untracked:
            print(f'[INFO] 미추적 파일 {len(changes.untracked)}개는 diff에 포함되지 않습니다. 검토 후 git add로 추가하세요.')
        if not changes.diff.strip():
            print('[INFO] 텍스트 diff가 없습니다. 미추적 파일을 stage하거나 변경 내용을 확인하세요.')
            return 0
        print(f'[INFO] Git diff 수집 완료: {len(changes.diff.splitlines())}줄 (staged + unstaged)')
        safe = prepare_diff(changes.diff, enabled=args.safe_mode, max_files=args.max_files, max_lines=args.max_lines, secrets=secrets)
        if not safe.diff.strip():
            print('[INFO] 안전 정책 적용 후 전송할 diff가 없습니다. API 호출 없이 종료합니다.')
            return 0
        if safe.truncated:
            print(f'[INFO] 일부 변경만 전달합니다: 제외 블록 {safe.omitted_files}개, 최대 {args.max_files}개 블록/{args.max_lines}줄')
        convention = load_convention(args.convention)
        # status 경로도 개인정보를 포함할 수 있어 동일하게 마스킹한다.
        status = mask(changes.status, secrets) if args.safe_mode else changes.status
        payload = build_payload(
            args.command, diff=safe.diff, status=status,
            why=mask(args.why, secrets), test_plan=mask(args.test_plan, secrets),
            convention=convention, model=args.model,
            temperature=args.temperature, max_tokens=args.max_tokens,
            truncated=safe.truncated,
        )
        # OFF 모드에서도 현재 실행용 API Key는 어떤 필드로도 전송하지 않는다.
        serialized = json.dumps(payload, ensure_ascii=False)
        for secret in secrets:
            serialized = serialized.replace(secret, '[REDACTED KEY]')
        payload = prepare_payload(json.loads(serialized), args.base_url)
        if args.dry_run:
            # 터미널 제어문자를 실행하지 않도록 JSON 문자열의 escape를 유지한다.
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 0
        print('[INFO] AI API 요청 중...')
        calls += 1
        data = generate(payload, key, base_url=args.base_url)
        output = format_result(data, args.command, convention, secrets)
        if safe.truncated:
            output = '[PARTIAL] 일부 diff만 반영된 초안입니다. 전체 변경을 검토하세요.\n' + output
        if args.output:
            with args.output.open('x', encoding='utf-8') as file:
                file.write(output)
        print('[DONE] 초안 생성 완료')
        print(output, end='')
        return 0
    except (ToolError, OSError, UnicodeError) as exc:
        print('[ERROR] ' + clean(mask(str(exc), secrets)), file=sys.stderr)
        return 1
    finally:
        print(f'[INFO] API 호출 횟수: {calls}')


if __name__ == '__main__':
    sys.exit(main())
