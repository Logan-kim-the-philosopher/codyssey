#!/bin/bash
set -eu
pid=$1
interval=${CPU_SAMPLE_INTERVAL:-0.2}
hz=$(getconf CLK_TCK)
echo 'timestamp,pid,utime_ticks,stime_ticks,uptime_s,interval_cpu_pct'
prev_ticks=''; prev_time=''
while [ -r "/proc/$pid/stat" ]; do
 raw=$(cat "/proc/$pid/stat") || break
 fields=${raw##*) }
 set -- $fields
 ticks=$((${12}+${13}))
 uptime=$(cut -d ' ' -f1 /proc/uptime)
 pct=$(awk -v t="$ticks" -v p="$prev_ticks" -v u="$uptime" -v v="$prev_time" -v hz="$hz" 'BEGIN{if(v!="" && u>v) printf "%.2f",100*(t-p)/hz/(u-v); else printf "NA"}')
 echo "$(date -u +%FT%TZ),$pid,${12},${13},$uptime,$pct"
 prev_ticks=$ticks; prev_time=$uptime
 sleep "$interval"
done
