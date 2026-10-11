"""표준 라이브러리로 OpenAI REST 호출. 자동 재시도 없음."""
import json
import socket
from urllib import request, error
from urllib.parse import urlsplit
from .errors import ToolError

ENDPOINT = 'https://api.openai.com/v1/chat/completions'
MAX_RESPONSE_BYTES = 1_000_000

class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ToolError('API 리다이렉트는 허용하지 않습니다.')


def endpoint_for(base_url: str) -> str:
    url = urlsplit(base_url)
    try:
        port = url.port
    except ValueError as exc:
        raise ToolError('유효한 HTTPS API 주소가 필요합니다.') from exc
    if (url.scheme != 'https' or url.hostname not in ('api.openai.com', 'copa.codyssey.kr')
            or url.username or url.password or url.query or url.fragment or port not in (None, 443)
            or url.path.rstrip('/') != '/v1'):
        raise ToolError('승인된 HTTPS API 주소(/v1)만 사용할 수 있습니다.')
    return base_url.rstrip('/') + '/chat/completions'


def prepare_payload(payload: dict, base_url: str) -> dict:
    result = dict(payload)
    if urlsplit(base_url).hostname == 'copa.codyssey.kr':
        result['max_tokens'] = result.pop('max_completion_tokens', result.get('max_tokens', 1200))
        result.pop('store', None)
        result.pop('response_format', None)
    return result


def generate(payload: dict, api_key: str, timeout: float = 30,
             base_url: str = 'https://api.openai.com/v1') -> dict:
    payload = prepare_payload(payload, base_url)
    req = request.Request(endpoint_for(base_url), data=json.dumps(payload).encode(),
                          headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}, method='POST')
    try:
        with request.build_opener(NoRedirect).open(req, timeout=timeout) as response:
            raw = response.read(MAX_RESPONSE_BYTES + 1)
    except error.HTTPError as exc:
        hint = ''
        with exc:
            try:
                raw_diagnostic = exc.read(16384).decode('utf-8', errors='replace')
                # 원문은 메모리에서 고정 분류 비교에만 사용한다. 출력·파일 저장 금지.
                labels = {'temperature': 'temperature', 'max_tokens': 'max_tokens',
                          'max_completion_tokens': 'max_completion_tokens', 'response_format': 'response_format',
                          'store': 'store', 'model': 'model', '모델': 'model', 'stream': 'stream',
                          'quota': 'quota', 'balance': 'balance', 'credit': 'credit',
                          'insufficient': 'insufficient', 'json': 'json', 'messages': 'messages',
                          'unsupported': 'unsupported', 'not found': 'not-found',
                          'authentication': 'authentication', 'unauthorized': 'authentication',
                          'permission': 'permission', '권한': 'permission', '잔액': 'balance',
                          'user-agent': 'user-agent', 'user agent': 'user-agent', 'client': 'client',
                          'endpoint': 'endpoint', 'path': 'path', 'method': 'method',
                          'proxy': 'proxy', 'protocol': 'protocol', 'version': 'version', 'http': 'http'}
                matches = sorted({label for term, label in labels.items() if term in raw_diagnostic.lower()})
                if matches:
                    hint = ' 고정 진단 분류: ' + ', '.join(matches) + '.'
                del raw_diagnostic
            except (ValueError, TypeError, AttributeError):
                pass
        reason = {401: '인증 실패', 403: '접근 거부', 429: '요청 한도 또는 잔액 확인', 400: '모델·파라미터 확인'}.get(exc.code, 'API 요청 실패')
        raise ToolError(f'HTTP {exc.code}: {reason}.{hint} 서버 오류 원문은 출력하지 않습니다.') from exc
    except (error.URLError, TimeoutError, socket.timeout, OSError) as exc:
        raise ToolError('네트워크 오류 또는 요청 제한 시간 초과. 연결을 확인하세요.') from exc
    if len(raw) > MAX_RESPONSE_BYTES:
        raise ToolError('API 응답이 허용 크기(1MB)를 초과했습니다.')
    try:
        envelope = json.loads(raw)
        choice = envelope['choices'][0]
        if not isinstance(choice, dict):
            raise ValueError('Expected choice object')
        if choice.get('finish_reason') != 'stop':
            raise ToolError('응답이 중단되거나 거부되었습니다. max-tokens와 입력 크기를 확인하세요.')
        content = choice['message']['content']
        result = json.loads(content)
        if not isinstance(result, dict):
            raise ValueError('Expected object')
        return result
    except (ValueError, KeyError, IndexError, TypeError) as exc:
        raise ToolError('API 응답에 유효한 JSON 초안이 없습니다.') from exc
