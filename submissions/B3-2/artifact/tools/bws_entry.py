"""BWS 내부 소비 프로세스. 비밀은 메모리에서만 다루며 진단 원문을 출력하지 않는다."""
import contextlib
import io
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from gitgen.environment import public_environment


def consume(argv):
    key = os.environ.get('CODEYSSEY_LLM_API', '')
    # BWS가 주입한 다른 비밀도 출력·저장 검사의 금지값으로 보관한다.
    forbidden = tuple(value for name, value in os.environ.items()
                      if name not in ('PATH', 'LANG', 'LC_ALL', 'LC_CTYPE', 'TMPDIR') and len(value) >= 8)
    public = public_environment()
    os.environ.clear()
    os.environ.update(public)
    if not key:
        return 3
    os.environ['AI_API_KEY'] = key
    from main import main
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            code = main(argv)
    except BaseException:
        return 4  # traceback이나 예외 원문을 외부로 내보내지 않는다.
    finally:
        os.environ.pop('AI_API_KEY', None)
    text = output.getvalue()
    if any(secret in text for secret in forbidden):
        return 5  # 비밀이 검출된 출력은 폐기; 파일 저장·출력 금지.
    # BWS stdout은 상위 런처가 폐기한다. 결과는 별도 전용 fd로 전달한다.
    fd = int(os.environ.get('GITGEN_RESULT_FD', '3'))
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as result:
            result.write(text)
    except OSError:
        return 4
    return code


if __name__ == '__main__':
    sys.exit(consume(sys.argv[1:]))
