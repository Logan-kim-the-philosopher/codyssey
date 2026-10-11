#!/bin/bash
set -euo pipefail
# Amazon Linux 2023; no credentials or private keys are embedded here.
dnf install -y docker
systemctl enable --now docker
install -d -m 755 /opt/b3-1/web
# Site files are copied through SSH after cloud-init completes.
