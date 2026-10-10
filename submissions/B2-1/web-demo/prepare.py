"""Refresh deploy copies; no edits to the original assignment artifact."""
from pathlib import Path
import shutil
import html
import zipfile

root = Path(__file__).resolve().parent
source = root.parent / "artifact" / "budget_app"
if source.exists():
    shutil.copytree(source, root / "budget_app", dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
deck = root.parent / "preview-export"
if deck.exists():
    shutil.copytree(deck, root / "public" / "presentation", dirs_exist_ok=True)
source_page = root / "public" / "source"
source_page.mkdir(parents=True, exist_ok=True)
files = sorted((root / "budget_app").glob("*.py"))
sections = []
with zipfile.ZipFile(source_page / "budget_app.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for file in files:
        archive.write(file, "budget_app/" + file.name)
        sections.append('<details><summary>' + html.escape(file.name) + '</summary><pre><code>'
                        + html.escape(file.read_text()) + '</code></pre></details>')
source_page.joinpath("index.html").write_text('''<!doctype html><html lang="ko"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>용돈 기입장 소스코드</title>
<style>body{background:#08152b;color:#e6efff;font:16px/1.6 system-ui;max-width:1000px;margin:40px auto;padding:0 24px}a{color:#9cddff}details{margin:16px 0;border:1px solid #34516d;border-radius:8px;padding:16px}summary{cursor:pointer;font-weight:600}pre{overflow:auto;font:13px/1.6 monospace}</style>
<h1>용돈 기입장 소스코드</h1><p>콘솔 프로그램의 Python 원본입니다.</p>
<p><a href="budget_app.zip" download>전체 소스 다운로드</a> · <a href="/">서비스 체험</a> · <a href="/presentation/index.html#15">발표자료</a></p>
<p>다운로드한 ZIP을 풀고 해당 폴더에서 <code>python3 -m budget_app --help</code>로 실행하세요.</p>
''' + ''.join(sections) + '</html>')
print("Deploy copies ready")
