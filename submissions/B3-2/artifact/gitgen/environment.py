"""자식 프로세스에는 필요한 비민감 환경만 전달한다."""
import os

ALLOWLIST = ('PATH', 'LANG', 'LC_ALL', 'LC_CTYPE', 'TMPDIR')


def public_environment(source=None):
    source = os.environ if source is None else source
    result = {key: source[key] for key in ALLOWLIST if key in source}
    result.setdefault('PATH', '/usr/bin:/bin:/usr/sbin:/sbin')
    return result
