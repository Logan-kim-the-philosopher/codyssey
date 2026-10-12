from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parents[1]
e=root/'evidence'
s=json.loads((e/'summary.json').read_text())
for name in s:
 log=(e/name/'application.log').read_text()
 assert 'All Boot Checks Passed!' in log,name
 assert s[name]['uid']=='1000'
 assert s[name]['pid']!=s[name]['launcher_pid']
 rows=list(csv.DictReader((e/name/'monitor.csv').open()))
 assert rows and all(x['pid']==s[name]['pid'] for x in rows)
for name in ['oom-before','oom-after']:
 assert 'Memory limit exceeded' in (e/name/'application.log').read_text()
 assert s[name]['exit_code']=='137'
assert int(s['oom-after']['elapsed_s'])>int(s['oom-before']['elapsed_s'])
assert 'CPU Threshold Violated' in (e/'cpu-before/application.log').read_text()
assert 'observation-ended' not in (e/'cpu-before/config.txt').read_text()
assert 'CPU Threshold Violated' not in (e/'cpu-after/application.log').read_text()
assert 'observation-ended' in (e/'cpu-after/config.txt').read_text()
log=(e/'deadlock-confirmed/application.log').read_text()
assert 'WAITING for [Shared_Memory_A]' in log and 'WAITING for [Socket_Pool_B]' in log
assert 'futex_wait_queue' in (e/'deadlock-confirmed/process-threads.log').read_text()
rows=list(csv.DictReader((e/'deadlock-confirmed/monitor.csv').open()))
assert len(rows[-8:])==8 and len({x['rss_kb'] for x in rows[-8:]})==1
assert 'BLOCKED' not in (e/'deadlock-after/application.log').read_text()
assert 'All tasks completed' in (e/'deadlock-after/application.log').read_text()
for md in (root/'reports').glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',md.read_text()):
  if not target.startswith('https:'): assert (md.parent/target).exists(),(md,target)
print('PASS: boot/PID provenance, OOM comparison, CPU policy contrast, circular wait, recovery, report links')
import subprocess,sys
subprocess.run([sys.executable,str(root/'scripts/verify-cpu-burst.py')],check=True)
