#!/bin/bash
set -eu
pid=$1
interval=${2:-1}
printf 'timestamp,pid,elapsed_s,cpu_pct,mem_pct,rss_kb,threads,state\n'
while kill -0 "$pid" 2>/dev/null; do
  ps -p "$pid" -o pid=,etimes=,%cpu=,%mem=,rss=,nlwp=,stat= | awk -v t="$(date -u +%FT%TZ)" 'NF {printf "%s,%s,%s,%s,%s,%s,%s,%s\n",t,$1,$2,$3,$4,$5,$6,$7}'
  sleep "$interval"
done
