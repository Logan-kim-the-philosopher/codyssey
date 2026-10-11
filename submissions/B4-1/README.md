# B4-1 수행 내역서

## 실행 환경과 재현

Ubuntu 26.04 LTS ARM64 Docker 환경(동등 Linux 환경). 제공 앱 `agent-app-linux-arm64`를 수정 없이 실행한다. 호스트에 SSH/방화벽/계정을 설정하지 않는다.

아래 명령은 제출 폴더의 `artifact/` 디렉토리에서 실행한다.

```bash
docker build -t codyssey-b4-1 environment
docker run -d --name codyssey-b4-1 --cap-add NET_ADMIN \
  -p 127.0.0.1:20022:20022 -p 127.0.0.1:15034:15034 \
  -v "$PWD":/workspace codyssey-b4-1
docker exec codyssey-b4-1 bash /workspace/environment/setup.sh
```

NET_ADMIN은 컨테이너 네트워크 방화벽 설정에 필요하다. 호스트 공개 범위는 localhost이며, 앱은 컨테이너 내부에서 0.0.0.0:15034를 사용한다. SSH 비밀번호 로그인은 차단하고 공개키 인증을 사용한다. 실제 SSH 연결이 필요하면 agent-admin의 authorized_keys에 공개키를 설치한다.

## 계정·그룹·디렉토리

agent-common: agent-admin/dev/test. agent-core: agent-admin/dev. `/opt/agent-app`을 AGENT_HOME으로 사용해 개인 홈의 탐색 권한과 공유 접근 충돌을 피한다. upload_files는 agent-common 2770, api_keys와 로그는 agent-core 2770이다. setgid와 기본 ACL로 새 파일의 그룹 및 접근 정책을 상속한다. 일반 계정의 소속 그룹은 `id`로 확인한다. 디렉토리 읽기/쓰기에 탐색(x) 권한도 필요하다.

환경 변수는 `/etc/profile.d/agent-app.sh`에 저장한다. 컨테이너 시간대는 UTC이므로 로그 시각도 UTC이다. cron은 로그인 셸 환경을 자동 상속하지 않으므로 명시적으로 이 파일을 읽는다. AGENT_LOG_DIR도 명시한다. 테스트 키 파일은 과제에서 요구한 공개 테스트 문자열이며 실제 비밀키가 아니다.

## 운영 설계와 설명

SSH 포트 변경은 기본 포트를 겨냥한 자동 스캔을 줄이지만 인증을 대신하지 않는다. Root 원격 차단은 탈취한 인증 정보로 즉시 최고 권한을 얻는 경로를 줄인다. 공개키 인증과 최소 허용 방화벽을 함께 적용한다. UFW 기본 인바운드는 deny, TCP 20022/15034만 allow이다. 기존 연결과 loopback 허용은 포트 서비스 추가 허용과 구별한다.

키와 로그는 최소 권한에 따라 core만 접근한다. 개발자는 스크립트를 작성하고 운영자는 그룹 실행 권한으로 cron에서 실행한다. monitor.sh 소유자 agent-dev, 그룹 agent-core, 모드 750이다. 로그 쓰기 때문에 root로 monitor를 실행할 필요는 없다.

프로세스와 LISTEN 포트가 없으면 관제 대상 서비스가 정상 실행 조건을 충족하지 않으므로 exit 1로 실패한다. 방화벽 비활성 및 자원 임계값 초과는 경고를 남겨 계속 자원 상태를 기록한다. 경고 때문에 기록까지 중단하면 장애 추적 자료가 사라진다.

CPU는 시스템 전체 사용률을 `/proc/stat`의 두 시점 차이로 산정한다. 메모리는 `/proc/meminfo`의 MemTotal와 MemAvailable로 사용률을 계산한다. Root partition은 `df`의 Used %를 사용한다. CPU/MEM은 시스템 전체 기준이며 앱 하나의 사용률이 아니다. 정해진 라벨과 시간 형식은 후속 report 파싱을 안정화한다. `>`는 기존 파일을 덮어쓰고 `>>`는 끝에 추가하므로 관제 기록은 `>>`로 누적한다.

로그 용량 조건은 **10MB=10,000,000 bytes, 활성 로그 포함 10개**로 해석한다. 쓰기 전에 회전하여 파일 크기 한도를 지키며 오래된 파일을 제거한다. 시간 보존은 수정 시간(mtime) 기준 7일/30일이다. 활성 로그를 압축할 때 관제 쓰기와 잠금을 공유하고 새 활성 로그를 이어서 생성해야 한다. 이 해석은 원문에서 단위·개수·경과 시간 기준이 구체적이지 않은 부분을 명시한 것이다.

## 운영 응용과 장애 대응

Nginx로 바꾸면 실제 실행 파일 식별 조건과 포트, 로그 저장 경로를 바꾸고 부하 특성에 맞게 임계값을 검토한다. 프로세스만 있고 포트가 없으면 시작 중인지, 포트 설정이 다른지, bind 주소·권한·포트 충돌이 있는지 확인한다. `ps` → 프로세스 실행 인자/환경 → `ss -ltnp` → 서비스 로그 순으로 확인한다. LISTEN 부재와 외부 접속 실패는 다르므로 포트가 열린 뒤 방화벽·네트워크 경로를 점검한다.

로그 급증 시 단기에는 `df`, 로그별 크기, 열린 삭제 파일을 확인하고 안전한 회전·압축으로 공간을 확보한다. 필요한 장애 증거를 무작정 지우지 않는다. 중기에는 용량/시간 보존 정책, 경고 알림, 과도한 로그 원인, 디스크 용량 및 외부 보관을 검토한다. 삭제된 파일을 프로세스가 계속 열고 있으면 파일 삭제만으로 공간이 즉시 반환되지 않을 수 있다.

## 검증 결과

실제 명령 출력과 기능 검증 결과는 `evidence/`에 저장한다. 제공 앱 준비 메시지 READY/REDDY 차이는 실제 실행 결과로 확인한다. 결과 확인 전에는 성공 증거로 간주하지 않는다.

## 제공 앱과 원문의 키 경로 차이

정정된 B4-1 파일은 `agent-app-linux-arm64`이다. 실제 Boot는 5단계 모두 OK와 `Agent READY`이며 0.0.0.0:15034를 연다. 평가표의 REDDY는 실제 출력과 다르다.

제공 바이너리는 AGENT_KEY_PATH에 `/opt/agent-app/api_keys` 디렉토리를 요구하고 그 아래 `secret.key`를 찾는다. 원문은 `.../t_secret.key` 파일 경로를 요구한다. 원문 설정을 profile에 보존하고 `secret.key -> t_secret.key` 별칭을 추가했다. `environment/start-app.sh`에서만 AGENT_KEY_PATH를 디렉토리로 덮어쓴다. 제공 앱은 수정하지 않았다. 이 차이는 원문 파일 경로를 그대로 사용한 실행 성공으로 간주할 수 없으며 제출 시 명시해야 한다.

```bash
docker exec -d codyssey-b4-1 bash -lc 'runuser -u agent-admin -- bash /workspace/environment/start-app.sh > /workspace/evidence/app-boot.txt 2>&1'
docker exec codyssey-b4-1 bash /workspace/environment/install-monitoring.sh
docker exec codyssey-b4-1 bash /workspace/tests/scripts-test.sh
```

방화벽 상태 조회는 일반 계정에서 root 권한이 필요하므로 `/etc/sudoers.d/agent-firewall-status`에 agent-admin의 `/usr/sbin/ufw status` 단일 읽기 명령만 허용한다. monitor는 sudo -n으로 조회하여 cron에서 암호 입력을 기다리지 않는다.
