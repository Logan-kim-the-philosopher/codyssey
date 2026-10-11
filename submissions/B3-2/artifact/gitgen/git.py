"""읽기 전용 Git 수집. 외부 diff 도구와 textconv는 실행하지 않는다."""
from dataclasses import dataclass
from pathlib import Path
import subprocess
import tempfile
from .errors import ToolError
from .environment import public_environment

MAX_INPUT_BYTES = 1_000_000

@dataclass(frozen=True)
class Changes:
    status: str
    diff: str
    files: tuple[str, ...]
    untracked: tuple[str, ...]


def run_git(root: Path, *args: str) -> str:
    try:
        with tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as errors:
            result = subprocess.run(
                ['git', '-c', 'core.quotePath=false', '-c', 'core.fsmonitor=false', *args], cwd=root,
                env=public_environment(),
                stdout=output, stderr=errors, timeout=15, check=False,
            )
            output.seek(0)
            raw = output.read(MAX_INPUT_BYTES + 1)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ToolError('Git 실행 실패 또는 제한 시간 초과') from exc
    if result.returncode:
        raise ToolError('Git 수집 실패: Git 저장소와 실행 위치를 확인하세요.')
    if len(raw) > MAX_INPUT_BYTES:
        raise ToolError('Git 출력이 1MB를 초과합니다. 변경을 나눠 실행하세요.')
    return raw.decode('utf-8', errors='replace')


def collect_changes(root: Path) -> Changes:
    if not (root / '.git').exists():
        raise ToolError('Git 프로젝트 루트(.git이 있는 디렉토리)에서 실행하세요.')
    raw = run_git(root, 'status', '--porcelain=v1', '-z', '--untracked-files=all')
    records = raw.split('\0')
    files, untracked, status = [], [], []
    index = 0
    while index < len(records):
        record = records[index]
        index += 1
        if not record:
            continue
        flag, name = record[:2], record[3:]
        files.append(name)
        status.append(f'{flag} {name}')
        if flag == '??':
            untracked.append(name)
        if 'R' in flag or 'C' in flag:
            index += 1  # -z 형식의 원래 경로 레코드
    flags = ('--no-ext-diff', '--no-textconv', '--no-color')
    staged = run_git(root, 'diff', *flags, '--cached', '--')
    unstaged = run_git(root, 'diff', *flags, '--')
    diff = staged + unstaged
    if len(diff.encode('utf-8')) > MAX_INPUT_BYTES:
        raise ToolError('합산 diff가 1MB를 초과합니다. 변경을 나눠 실행하세요.')
    return Changes('\n'.join(status), diff, tuple(files), tuple(untracked))
