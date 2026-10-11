#!/bin/bash
set -euo pipefail
cd /opt/b3-1
docker run -d --name b3-1-https --restart unless-stopped \
  -p 443:443 --add-host host.docker.internal:host-gateway \
  -v "$PWD/Caddyfile:/etc/caddy/Caddyfile:ro" \
  -v b3-1-caddy-data:/data -v b3-1-caddy-config:/config \
  caddy:2.10-alpine
# HTTP remains served by Nginx, and ACME uses TLS-ALPN-01 on 443.
