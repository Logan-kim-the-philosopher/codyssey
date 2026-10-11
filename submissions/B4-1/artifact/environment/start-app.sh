#!/usr/bin/env bash
set -euo pipefail
source /etc/profile.d/agent-app.sh
# Supplied binary expects a directory; assignment specifies a file path.
export AGENT_KEY_PATH="$AGENT_HOME/api_keys"
exec "$AGENT_HOME/agent-app-linux-arm64"
