#!/usr/bin/env bash
# Run on Linux: bash tests/scripts-test.sh
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
mkdir -p "$work/logs" "$work/archive" "$work/proc/123" "$work/tools"
printf '/opt/agent-app-linux-arm64\0' > "$work/proc/123/cmdline"
printf 'cpu  100 0 100 800 0 0 0 0\n' > "$work/proc/stat"
printf 'MemTotal: 1000 kB\nMemAvailable: 800 kB\n' > "$work/proc/meminfo"
cat > "$work/tools/ss" <<'TOOL'
#!/usr/bin/env bash
[[ ${NO_LISTEN:-0} == 1 ]] || echo 'LISTEN 0 128 0.0.0.0:15034 0.0.0.0:*'
TOOL
cat > "$work/tools/ufw" <<'TOOL'
#!/usr/bin/env bash
echo 'Status: inactive'
TOOL
chmod +x "$work/tools/"*
export PATH="$work/tools:$PATH" AGENT_LOG_DIR="$work/logs" AGENT_ARCHIVE_DIR="$work/archive" AGENT_PROC_ROOT="$work/proc" AGENT_SAMPLE_SECONDS=0
bash "$root/bin/monitor.sh" > "$work/output" 2> "$work/warnings"
[[ $(wc -l < "$work/logs/monitor.log") == 1 ]]
grep -E '\[WARNING\] Firewall' "$work/warnings"
grep -E '\[WARNING\] MEM 20.00% exceeds 10%' "$work/warnings"
grep -E 'PID:123 CPU:0.00% MEM:20.00% DISK_USED:[0-9]+%' "$work/output"
if NO_LISTEN=1 bash "$root/bin/monitor.sh" >/dev/null 2>&1; then echo 'Missing listen did not fail'; exit 1; fi
mv "$work/proc/123/cmdline" "$work/proc/123/absent"
if bash "$root/bin/monitor.sh" >/dev/null 2>&1; then echo 'Missing process did not fail'; exit 1; fi
mv "$work/proc/123/absent" "$work/proc/123/cmdline"
truncate -s 10000000 "$work/logs/monitor.log"
for n in {1..9}; do echo "$n" > "$work/logs/monitor.log.$n"; done
bash "$root/bin/monitor.sh" >/dev/null 2>&1
[[ $(stat -c %s "$work/logs/monitor.log.1") == 10000000 ]]
[[ $(cat "$work/logs/monitor.log.9") == 8 ]]
[[ $(find "$work/logs" -name 'monitor.log*' | wc -l) == 10 ]]
cat > "$work/logs/monitor.log" <<'LOG'
[2026-10-01 10:00:00] PID:123 CPU:10.00% MEM:20.00% DISK_USED:30%
[2026-10-01 11:00:00] PID:123 CPU:30.00% MEM:40.00% DISK_USED:50%
invalid
LOG
bash "$root/bin/report.sh" > "$work/report"
grep -E 'Samples: 2' "$work/report"
grep -E 'CPU AVG:20.00% MAX:30.00% MIN:10.00%' "$work/report"
bash "$root/bin/report.sh" "$work/logs/monitor.log" '2026-10-01 11:00:00' '2026-10-01 11:00:00' | grep -E 'Samples: 1'
bash "$root/bin/report.sh" "$work/logs/monitor.log" '2026-10-02 00:00:00' | grep -E 'Samples: 0'
if bash "$root/bin/report.sh" "$work/logs/monitor.log" invalid >/dev/null 2>&1; then exit 1; fi
printf old > "$work/logs/old log.log"
touch -d '8 days ago' "$work/logs/old log.log" "$work/logs/monitor.log"
printf recent > "$work/logs/recent.log"
printf expired > "$work/archive/expired.gz"
touch -d '31 days ago' "$work/archive/expired.gz"
bash "$root/bin/retention.sh" | grep -E 'Archived: 2'
[[ ! -e "$work/logs/old log.log" && ! -e "$work/archive/expired.gz" ]]
[[ -f "$work/logs/monitor.log" && ! -s "$work/logs/monitor.log" && -f "$work/logs/recent.log" ]]
[[ $(find "$work/archive" -name '*.gz' | wc -l) == 2 ]]
find "$work/archive" -name '*.gz' -exec gzip -t {} +
bash "$root/bin/retention.sh" | grep -E 'Archived: 0'
AGENT_LOG_DIR="$work/missing" bash "$root/bin/retention.sh" 2>&1 | grep -E '\[WARNING\]'
echo 'PASS: scripts fixtures'
