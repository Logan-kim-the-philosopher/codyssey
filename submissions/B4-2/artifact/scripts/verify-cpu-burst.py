from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parents[1]
e=root/'evidence'
result={}
for name in ['cpu-arm64-recheck','cpu-arm64-burst','cpu-arm64-burst-low','cpu-x86-recheck']:
 p=e/name
 cfg=dict(x.split('=',1) for x in (p/'config.txt').read_text().splitlines() if '=' in x)
 assert 'exit_code' in cfg, f'{name}: not finished'
 rows=list(csv.DictReader((p/'cpu-interval.csv').open()))
 intervals=[]
 for a,b in zip(rows,rows[1:]):
  dt=float(b['uptime_s'])-float(a['uptime_s'])
  delta=int(b['utime_ticks'])+int(b['stime_ticks'])-int(a['utime_ticks'])-int(a['stime_ticks'])
  assert dt>0 and delta>=0
  calculated=100*delta/100/dt
  assert abs(calculated-float(b['interval_cpu_pct']))<0.011
  assert b['pid']==cfg['pid']
  intervals.append({'timestamp':b['timestamp'],'start_uptime':a['uptime_s'],'end_uptime':b['uptime_s'],'delta_cpu_ticks':delta,'interval_cpu_pct':float(b['interval_cpu_pct'])})
 log=(p/'application.log').read_text()
 assert 'All Boot Checks Passed!' in log
 high='low' not in name
 assert ('CPU Threshold Violated' in log)==high
 assert ('observation-ended' in (p/'config.txt').read_text())==(not high)
 result[name]={'config':cfg,'samples':len(intervals),'max_interval_cpu_pct':max(x['interval_cpu_pct'] for x in intervals),'over_50_samples':sum(x['interval_cpu_pct']>50 for x in intervals),'peak':max(intervals,key=lambda x:x['interval_cpu_pct']),'peak_context':[]}
 i=max(range(len(intervals)),key=lambda j:intervals[j]['interval_cpu_pct'])
 result[name]['peak_context']=intervals[max(0,i-2):i+3]
assert result['cpu-arm64-burst']['max_interval_cpu_pct']>50
assert result['cpu-arm64-burst']['config']['exit_code']=='143'
assert int(result['cpu-arm64-burst-low']['config']['observation_limit_s'])>int(result['cpu-arm64-burst']['config']['elapsed_s'])
(e/'cpu-burst-summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS: raw /proc deltas reproduce CPU samples; real burst >50%; protection exit; longer-lived lower-setting control')
for n,d in result.items():print(n,d['max_interval_cpu_pct'],d['config']['elapsed_s'])
