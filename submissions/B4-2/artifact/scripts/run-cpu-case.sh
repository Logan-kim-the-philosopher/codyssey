#!/bin/bash
set -eu
name=$1
memory=$2
cpu=$3
threads=$4
seconds=${5:-60}
export AGENT_HOME=/tmp/agent-home AGENT_PORT=15034
export AGENT_UPLOAD_DIR=$AGENT_HOME/upload_files AGENT_KEY_PATH=$AGENT_HOME/api_keys AGENT_LOG_DIR=$AGENT_HOME/logs
export MEMORY_LIMIT=$memory CPU_MAX_OCCUPY=$cpu MULTI_THREAD_ENABLE=$threads
mkdir -p "$AGENT_UPLOAD_DIR" "$AGENT_KEY_PATH" "$AGENT_LOG_DIR" "/work/evidence/$name"
printf 'agent_api_key_test' > "$AGENT_KEY_PATH/secret.key"
out=/work/evidence/$name
printf 'started=%s\nuid=%s\nMEMORY_LIMIT=%s\nCPU_MAX_OCCUPY=%s\nMULTI_THREAD_ENABLE=%s\nobservation_limit_s=%s\n' "$(date -u +%FT%TZ)" "$(id -u)" "$memory" "$cpu" "$threads" "$seconds" > "$out/config.txt"
/work/bin/${AGENT_BINARY:-agent-leak-app-arm64} > "$out/application.log" 2>&1 &
launcher=$!
sleep 1
pid=$(pgrep -P "$launcher" | head -1)
pid=${pid:-$launcher}
echo "launcher_pid=$launcher" >> "$out/config.txt"
ps -ef > "$out/process-tree-start.log"
echo "pid=$pid" >> "$out/config.txt"
bash /work/scripts/monitor.sh "$pid" > "$out/monitor.csv" &
mon=$!
bash /work/scripts/cpu-interval.sh "$pid" > "$out/cpu-interval.csv" &
interval_pid=$!
top -b -d 1 -p "$pid" > "$out/top.log" &
top_pid=$!
ps -L -p "$pid" -o pid,tid,cls,rtprio,ni,pri,stat,wchan:24,comm > "$out/scheduling-policy.log"
start=$SECONDS
while kill -0 "$pid" 2>/dev/null && (( SECONDS-start < seconds )); do
  { date -u +%FT%TZ; ps -p "$pid" -o pid,ppid,etimes,pcpu,pmem,rss,nlwp,stat,args; ps -L -p "$pid" -o pid,tid,pcpu,stat,wchan:24,comm; } >> "$out/process-threads.log" || true
  sleep 2
done
if kill -0 "$pid" 2>/dev/null; then
 echo 'observation-ended: process still alive; harness sends SIGTERM' >> "$out/config.txt"
 kill -TERM "$pid" 2>/dev/null || true
 sleep 1
 kill -KILL "$pid" 2>/dev/null || true
fi
set +e
wait "$launcher"; result=$?
wait "$mon"
wait "$interval_pid"
kill "$top_pid" 2>/dev/null || true
wait "$top_pid"
set -e
printf 'exit_code=%s\nelapsed_s=%s\nended=%s\n' "$result" "$((SECONDS-start))" "$(date -u +%FT%TZ)" >> "$out/config.txt"
cp -R "$AGENT_LOG_DIR" "$out/internal-logs"
