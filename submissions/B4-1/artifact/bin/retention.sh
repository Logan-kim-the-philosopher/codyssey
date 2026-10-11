#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C
umask 007
log_dir=${AGENT_LOG_DIR:-/var/log/agent-app}
archive=${AGENT_ARCHIVE_DIR:-/var/log/monitor/agent-app/archive}
warning() { printf '[WARNING] %s\n' "$*" >&2; }
[[ -d $log_dir && -w $log_dir && -x $log_dir ]] || { warning 'Log directory missing or not writable'; exit 0; }
[[ -d $archive && -w $archive && -x $archive ]] || { warning 'Archive directory missing or not writable'; exit 0; }
exec 9>"$log_dir/.monitor.lock" || { warning 'Cannot acquire lock file'; exit 0; }
flock -x 9
now=$(date +%s)
count=0
while IFS= read -r -d '' file; do
    [[ -r $file && -w $file ]] || { warning "Cannot archive $file"; continue; }
    modified=$(stat -c %Y "$file")
    ((now-modified>=7*86400)) || continue
    # Unique destination; preserve original mtime so age means source log age.
    dest=$(mktemp "$archive/$(basename "$file").XXXXXXXX.gz") || { warning 'Cannot create archive'; continue; }
    if gzip -c -- "$file" > "$dest" && chmod 660 "$dest" && touch -r "$file" "$dest"; then
        if [[ $file == "$log_dir/monitor.log" ]]; then
            # Lock prevents monitor append while the old inode is removed/recreated.
            rm -- "$file"; : > "$file"
        else
            rm -- "$file"
        fi
        count=$((count+1))
    else
        rm -f -- "$dest"; warning "Compression failed: $file"
    fi
done < <(find "$log_dir" -maxdepth 1 -type f -name '*.log' -print0)
while IFS= read -r -d '' file; do
    modified=$(stat -c %Y "$file")
    if ((now-modified>=30*86400)); then rm -- "$file" || warning "Cannot delete $file"; fi
done < <(find "$archive" -maxdepth 1 -type f -name '*.gz' -print0)
printf 'Archived: %s\n' "$count"
