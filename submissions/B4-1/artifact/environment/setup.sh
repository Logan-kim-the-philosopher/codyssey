#!/usr/bin/env bash
set -euo pipefail
[[ $EUID == 0 ]] || { echo 'Run setup as root inside the dedicated Linux environment.' >&2; exit 1; }
for group in agent-common agent-core; do getent group "$group" >/dev/null || groupadd "$group"; done
for user in agent-admin agent-dev agent-test; do id "$user" >/dev/null 2>&1 || useradd -m -s /bin/bash "$user"; usermod -aG agent-common "$user"; done
for user in agent-admin agent-dev; do usermod -aG agent-core "$user"; done
# Shared application root avoids traversal access through a private user home.
install -d -o agent-admin -g agent-common -m 2750 /opt/agent-app
install -d -o agent-admin -g agent-common -m 2770 /opt/agent-app/upload_files
install -d -o agent-admin -g agent-core -m 2770 /opt/agent-app/api_keys /var/log/agent-app /var/log/monitor/agent-app/archive
install -d -o agent-dev -g agent-core -m 2750 /opt/agent-app/bin
for dir in /opt/agent-app/upload_files /opt/agent-app/api_keys /var/log/agent-app /var/log/monitor/agent-app/archive; do
 setfacl -m u::rwx,g::rwx,o::---,m::rwx "$dir"
 setfacl -d -m u::rwx,g::rwx,o::---,m::rwx "$dir"
done
printf '%s\n' agent_api_key_test > /opt/agent-app/api_keys/t_secret.key
chown agent-admin:agent-core /opt/agent-app/api_keys/t_secret.key
chmod 660 /opt/agent-app/api_keys/t_secret.key
ln -sfn t_secret.key /opt/agent-app/api_keys/secret.key
install -o agent-admin -g agent-core -m 750 /workspace/vendor/agent-app-linux-arm64 /opt/agent-app/agent-app-linux-arm64
cat > /etc/profile.d/agent-app.sh <<'ENV'
export AGENT_HOME=/opt/agent-app
export AGENT_PORT=15034
export AGENT_UPLOAD_DIR=/opt/agent-app/upload_files
export AGENT_KEY_PATH=/opt/agent-app/api_keys/t_secret.key
export AGENT_LOG_DIR=/var/log/agent-app
ENV
# A dedicated container has no remote session to disrupt.
mkdir -p /run/sshd /etc/ssh/sshd_config.d
cat > /etc/ssh/sshd_config.d/00-agent.conf <<'SSH'
Port 20022
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
SSH
/usr/sbin/sshd -t
ufw default deny incoming
ufw default allow outgoing
ufw allow 20022/tcp
ufw allow 15034/tcp
ufw --force enable
/usr/sbin/sshd
cron
