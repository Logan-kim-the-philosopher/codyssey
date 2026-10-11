#!/bin/bash
set -euo pipefail
cd /opt/b3-1
# Keep plain HTTP on port 80 for the assignment's fixed public-IP test.
if docker container inspect b3-1-web >/dev/null 2>&1; then
  docker start b3-1-web >/dev/null
else
  docker run -d --name b3-1-web --restart unless-stopped \
  -p 80:80 \
  -v "$PWD/web:/usr/share/nginx/html:ro" \
  -v "$PWD/web/nginx.conf:/etc/nginx/conf.d/default.conf:ro" \
  nginx:1.28-alpine
fi
for attempt in {1..10}; do
  if curl --fail --show-error http://localhost/health; then exit 0; fi
  sleep 2
done
echo "Web server readiness check failed" >&2
exit 1
