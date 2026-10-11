"""비용 없는 로컬 검증·증거 생성. 실제 AI 호출이나 PR 증빙을 만들지 않는다."""
import ast
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from gitgen.formatting import format_result
from gitgen.prompt import DEFAULT_CONVENTION, load_convention
from gitgen.safety import prepare_diff


def main():
    evidence = ROOT / 'evidence'
    evidence.mkdir(exist_ok=True)
    result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], cwd=ROOT, capture_output=True, text=True)
    (evidence / 'unit-tests.txt').write_text(result.stdout + result.stderr)
    print(result.stderr)
    if result.returncode:
        return result.returncode
    sources = list(ROOT.glob('gitgen/*.py')) + [ROOT / 'main.py'] + list(ROOT.glob('tools/*.py')) + list(ROOT.glob('tests/*.py'))
    for source in sources:
        ast.parse(source.read_text(), filename=str(source), feature_version=(3, 10))
    syntax = f'{len(sources)} Python files parse with Python 3.10 grammar.\nRuntime tests: {sys.version.split()[0]} (not a Python 3.10 runtime test).\n'
    (evidence / 'syntax-check.txt').write_text(syntax)
    print(syntax)
    synthetic = 'diff --git a/app.py b/app.py\n--- a/app.py\n+++ b/app.py\n@@ -1 +1,3 @@\n-old=1\n+token="FAKE_TEST_ONLY"\n+email="fixture@example.invalid"\n+value=2\n'
    on = prepare_diff(synthetic, enabled=True, max_files=10, max_lines=200).diff
    off = prepare_diff(synthetic, enabled=False, max_files=10, max_lines=200).diff
    comparison = '# safe-mode 실제 전처리 비교\n\n입력은 합성 fixture이고 비밀은 가짜다. API 호출 0회. 모델 결과 비교가 아니다.\n정책: 10개 diff 블록, 200줄; 마스킹·제외 상세는 README 참조.\n\n## ON\n```diff\n' + on + '\n```\n\n## OFF\n```diff\n' + off + '\n```\n'
    (evidence / 'safety-comparison.md').write_text(comparison)
    commit = {'summary': '오류 안내 문구를 구체화', 'title': 'fix: API Key 누락 안내 개선', 'body': ['환경변수 설정 방법을 안내']}
    pr = {'summary': '실행 위치 안내를 보강', 'title': 'docs: 실행 안내 보강', 'why': ['사용자가 실행 위치를 혼동할 수 있음'], 'what': ['프로젝트 루트 실행 방법을 문서화'], 'how_to_test': ['README 명령을 로컬에서 확인']}
    for kind, data in [('commit', commit), ('pr', pr)]:
        (evidence / f'mock-{kind}.txt').write_text('[MOCK] 미리 정의한 모의 API 응답의 실제 포맷팅 결과. API 호출 0회.\n' + format_result(data, kind, DEFAULT_CONVENTION))
    convention = load_convention(ROOT / 'examples/b3-1-convention.json')
    custom = commit | {'title': 'fix(b3-1): API Key 누락 안내 개선'}
    (evidence / 'convention-comparison.md').write_text('# 컨벤션 모의 응답 비교\n\n아래는 입력 응답을 직접 정의한 formatter 검증이다. AI 생성 전후 비교는 아직 미수행.\n\n## 기본\n```text\n' + format_result(commit, 'commit', DEFAULT_CONVENTION) + '```\n\n## B3-1 컨벤션\n```text\n' + format_result(custom, 'commit', convention) + '```\n')
    manifest = {'runtime': sys.version.split()[0], 'testsExitCode': result.returncode, 'actualApiCalls': 0,
                'evidenceKinds': {'unit-tests.txt': 'real Git fixtures and mocked HTTP', 'safety-comparison.md': 'real preprocessing of synthetic input', 'mock-commit.txt': 'mock response formatting', 'mock-pr.txt': 'mock response formatting', 'convention-comparison.md': 'mock response formatting'},
                'pending': ['real OpenAI generation', 'parameter experiment', 'AI convention comparison', 'GitHub source push', 'previous mission PR and 5-10 line revision summary']}
    (evidence / 'local-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print('Local evidence saved; actual OpenAI calls: 0.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
