"""Keychain → BWS 런타임 주입. 토큰·BWS 원문 진단을 출력하지 않는다."""
import os
from pathlib import Path
import shlex
import signal
import subprocess
import sys
import select
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from gitgen.environment import public_environment


def stop_tree(process):
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait()


def main(argv):
    # --output은 소비 프로세스가 출력 검사를 하기 전에 저장하므로 사용 금지.
    if any(arg == '--output' or arg.startswith('--output=') for arg in argv):
        print('[ERROR] BWS 실행에서는 --output 대신 런처의 검증된 표준출력을 사용하세요.')
        return 2
    if '--model' not in argv and '-model' not in argv and not any(a.startswith('--model=') for a in argv):
        argv = [*argv, '--model', 'gpt-5.4-mini']
    if '--temperature' not in argv and '-temperature' not in argv and not any(a.startswith('--temperature=') for a in argv):
        argv = [*argv, '--temperature', '1']
    if '--max-tokens' not in argv and '-max-tokens' not in argv and not any(a.startswith('--max-tokens=') for a in argv):
        argv = [*argv, '--max-tokens', '3000']
    if '--base-url' not in argv and not any(a.startswith('--base-url=') for a in argv):
        argv = [*argv, '--base-url', 'https://copa.codyssey.kr/v1']
    public = public_environment()
    try:
        token_result = subprocess.run(['/usr/bin/security', 'find-generic-password', '-s', 'bitwarden-bws-access-token', '-w'],
                                      env=public, capture_output=True, timeout=30, check=False)
        if token_result.returncode:
            print('[ERROR] Keychain BWS 토큰 접근 실패. 진단 원문은 출력하지 않습니다.')
            return 3
        token = token_result.stdout.decode('utf-8').strip()
        if not token:
            print('[ERROR] Keychain BWS 토큰이 비어 있습니다.')
            return 3
        # stdout/stderr는 폐기하고 소비 프로세스의 검사된 결과만 별도 pipe로 수신.
        read_fd, write_fd = os.pipe()
        command = shlex.join([sys.executable, str(ROOT / 'tools/bws_entry.py'), *argv])
        shell_command = f'{command} 3>&{write_fd}'
        env = public | {'BWS_ACCESS_TOKEN': token}
        try:
            process = subprocess.Popen([str(Path.home() / '.local/bin/bws'), 'run', '--no-inherit-env', '--shell', '/bin/sh', '-o', 'none', '--', shell_command],
                                       env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, pass_fds=(write_fd,), start_new_session=True)
        except BaseException:
            os.close(read_fd)
            raise
        finally:
            os.close(write_fd)
            env.pop('BWS_ACCESS_TOKEN', None)
        deadline = time.monotonic() + 60
        chunks, size = [], 0
        try:
            while True:
                remaining = deadline - time.monotonic()
                if remaining <= 0 or not select.select([read_fd], [], [], remaining)[0]:
                    stop_tree(process)
                    print('[ERROR] BWS 실행 제한 시간 초과. 출력을 폐기했습니다.')
                    return 4
                chunk = os.read(read_fd, 65536)
                if not chunk:
                    break
                size += len(chunk)
                if size > 1_100_000:
                    stop_tree(process)
                    print('[ERROR] 결과 크기 제한 초과. 출력을 폐기했습니다.')
                    return 4
                chunks.append(chunk)
            code = process.wait(timeout=max(1, deadline - time.monotonic()))
        finally:
            os.close(read_fd)
            if process.poll() is None:
                stop_tree(process)
        output = b''.join(chunks)
        # 토큰 값이 결과에 나타나면 원문을 내보내지 않고 폐기한다.
        if token.encode() in output:
            print('[ERROR] 민감정보 검사 실패. 결과를 폐기했습니다.')
            return 5
        if output:
            print(output.decode('utf-8'), end='')
        elif code:
            print(f'[ERROR] BWS 주입 또는 소비 프로세스 실패 (종료 코드 {code}). 비밀·진단 원문은 출력하지 않습니다.')
        return code
    except (OSError, UnicodeError, subprocess.SubprocessError):
        print('[ERROR] 안전한 BWS 실행 실패. 진단 원문은 출력하지 않습니다.')
        return 4


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
