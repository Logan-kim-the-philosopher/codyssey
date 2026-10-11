#!/usr/bin/env bash
# Linux host monitoring. Cron supplies the same environment as an interactive run.
set -euo pipefail
export LC_ALL=C
umask 007
LOG_DIR=${AGENT_LOG_DIR:-/var/log/agent-app}
PORT=${AGENT_PORT:-15034}
PROCESS_NAME=${AGENT_PROCESS_NAME:-agent-app-linux-arm64}
PROC_ROOT=${AGENT_PROC_ROOT:-/proc}
MAX_BYTES=10000000 # 10 MB; current log plus nine backups.
warning() { printf '[WARNING] %s\n' "$*" >&2; }
fail() { printf '[ERROR] %s\n' "$*" >&2; exit 1; }
# /proc/comm truncates names to 15 characters. Match argv[0]'s basename instead.
pid=''
for entry in "$PROC_ROOT"/[0-9]*/cmdline; do
    [[ -r $entry ]] || continue
    argv0=''
    IFS= read -r -d '' argv0 < "$entry" || true
    if [[ ${argv0##*/} == "$PROCESS_NAME" ]]; then
        candidate=${entry%/cmdline}; pid=${candidate##*/}; break
    fi
done
[[ -n $pid ]] || fail "App process absent: $PROCESS_NAME"
ss -H -ltn | awk -v port="$PORT" '$4 ~ (":" port "$") {found=1} END {exit !found}' || fail "TCP $PORT is not listening"
# No interactive sudo: provisioning grants only this read-only status command.
firewall=''
if command -v ufw >/dev/null 2>&1; then
    firewall=$(ufw status 2>/dev/null) || firewall=$(sudo -n /usr/sbin/ufw status 2>/dev/null) || true
    [[ $firewall == *'Status: active'* ]] || warning 'Firewall inactive or status unavailable'
elif command -v firewall-cmd >/dev/null 2>&1; then
    firewall=$(firewall-cmd --state 2>/dev/null) || true
    [[ $firewall == running ]] || warning 'Firewall inactive or status unavailable'
else
    warning 'Firewall status unavailable'
fi
read_cpu() {
    awk '/^cpu / {idle=$5+$6; total=0; for(i=2;i<=9;i++) total+=$i; print total,idle; exit}' "$PROC_ROOT/stat"
}
read -r total1 idle1 < <(read_cpu)
sleep "${AGENT_SAMPLE_SECONDS:-1}"
read -r total2 idle2 < <(read_cpu)
cpu=$(awk -v t="$((total2-total1))" -v i="$((idle2-idle1))" 'BEGIN {if(t<=0) print "0.00"; else printf "%.2f",100*(t-i)/t}')
mem=$(awk '/^MemTotal:/ {t=$2} /^MemAvailable:/ {a=$2} END {if(t<=0) exit 1; printf "%.2f",100*(t-a)/t}' "$PROC_ROOT/meminfo")
disk=$(df -P / | awk 'NR==2 {gsub(/%/,"",$5); print $5}')
[[ $disk =~ ^[0-9]+$ ]] || fail 'Cannot read root disk utilization'
for metric in CPU MEM DISK_USED; do
    case $metric in CPU) value=$cpu; limit=20;; MEM) value=$mem; limit=10;; DISK_USED) value=$disk; limit=80;; esac
    if awk -v value="$value" -v limit="$limit" 'BEGIN {exit !(value>limit)}'; then warning "$metric $value% exceeds $limit%"; fi
done
[[ -d $LOG_DIR && -w $LOG_DIR ]] || fail "Log directory unavailable: $LOG_DIR"
exec 9>"$LOG_DIR/.monitor.lock"
flock -x 9
log="$LOG_DIR/monitor.log"
printf -v line '[%s] PID:%s CPU:%s%% MEM:%s%% DISK_USED:%s%%' "$(date '+%Y-%m-%d %H:%M:%S')" "$pid" "$cpu" "$mem" "$disk"
size=0
[[ ! -e $log ]] || size=$(stat -c %s "$log")
if ((size+${#line}+1>MAX_BYTES)); then
    rm -f -- "$log.9"
    for ((n=8;n>=1;n--)); do [[ ! -e $log.$n ]] || mv -- "$log.$n" "$log.$((n+1))"; done
    [[ ! -e $log ]] || mv -- "$log" "$log.1"
fi
printf '%s\n' "$line" >> "$log"
printf '%s\n' "$line"
