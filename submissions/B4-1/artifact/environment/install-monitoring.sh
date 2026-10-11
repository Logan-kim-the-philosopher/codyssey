#!/usr/bin/env bash
set -euo pipefail
[[ $EUID == 0 ]] || exit 1
for name in monitor report retention; do install -o agent-dev -g agent-core -m 750 "/workspace/bin/$name.sh" "/opt/agent-app/bin/$name.sh"; done
printf '%s\n' 'agent-admin ALL=(root) NOPASSWD: /usr/sbin/ufw status' > /etc/sudoers.d/agent-firewall-status
chmod 440 /etc/sudoers.d/agent-firewall-status
visudo -cf /etc/sudoers.d/agent-firewall-status
cat > /tmp/agent-crontab <<'CRON'
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
* * * * * . /etc/profile.d/agent-app.sh; /opt/agent-app/bin/monitor.sh >> /var/log/agent-app/cron.log 2>&1
5 0 * * * . /etc/profile.d/agent-app.sh; /opt/agent-app/bin/retention.sh >> /var/log/agent-app/retention.log 2>&1
CRON
crontab -u agent-admin /tmp/agent-crontab
rm /tmp/agent-crontab
