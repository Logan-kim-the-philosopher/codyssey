#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C
# Inclusive ISO local-time bounds; defaults include the complete current log.
if (($#>3)); then echo 'Usage: report.sh [log-file [start-time [end-time]]]' >&2; exit 1; fi
log=${1:-${AGENT_LOG_DIR:-/var/log/agent-app}/monitor.log}
start=${2:-}; end=${3:-}
for bound in "$start" "$end"; do
    if [[ -n $bound ]]; then
        [[ $bound =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}$ ]] && date -d "$bound" >/dev/null 2>&1 || { echo 'Invalid time bound' >&2; exit 1; }
    fi
done
[[ -z $start || -z $end || $start < $end || $start == "$end" ]] || { echo 'Start exceeds end' >&2; exit 1; }
[[ -f $log && -r $log ]] || { echo '[WARNING] Log unavailable' >&2; exit 1; }
awk -v start="$start" -v end="$end" '
/^\[[0-9][0-9][0-9][0-9]-/ {
 time=substr($0,2,19); if((start!="" && time<start)||(end!="" && time>end)) next;
 if(NF!=6 || $3 !~ /^PID:[0-9]+$/ || $4 !~ /^CPU:[0-9]+(\.[0-9]+)?%$/ || $5 !~ /^MEM:[0-9]+(\.[0-9]+)?%$/ || $6 !~ /^DISK_USED:[0-9]+(\.[0-9]+)?%$/) next;
 n++; for(i=1;i<=3;i++) {v=$(i+3); sub(/^[^:]+:/,"",v); sub(/%$/,"",v); v+=0; sum[i]+=v; if(n==1 || v<min[i])min[i]=v; if(n==1 || v>max[i])max[i]=v;}
}
END {printf "Samples: %d\n",n; names[1]="CPU"; names[2]="MEM"; names[3]="DISK"; if(n==0){print "No samples in selected interval"; exit} for(i=1;i<=3;i++)printf "%s AVG:%.2f%% MAX:%.2f%% MIN:%.2f%%\n",names[i],sum[i]/n,max[i],min[i]}
' "$log"
