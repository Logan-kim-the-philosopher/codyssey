FROM ubuntu:26.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server ufw acl cron procps iproute2 sudo gzip gawk util-linux && rm -rf /var/lib/apt/lists/*
CMD ["sleep", "infinity"]
