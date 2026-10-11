# 실제 트러블슈팅 기록

## 초기화 도중 웹 파일 전송 실패

- 증상: 첫 SCP 실행이 `remote mkdir "/opt/b3-1/web/": No such file or directory`로 실패했다.
- 가설: EC2의 cloud-init Docker 설치가 아직 진행 중이어서 뒤에 실행할 배포 경로 준비가 완료되지 않았다.
- 검증: SSH 접속은 성공했고 `/var/log/cloud-init-output.log`에는 Docker 관련 패키지 설치 트랜잭션이 실행 중이었다. 파일 경로 부재와 초기화 대기 상태가 일치했다.
- 조치: SSH에서 `sudo install -d -o ec2-user -g ec2-user /opt/b3-1/web`로 배포 디렉터리를 명시적으로 생성한 뒤 파일 전송을 재시도했다.
- 결과: 재시도 SCP가 종료 코드 0으로 성공했다. 웹 파일 배포 경로를 확보했다.
- 재발 방지: 경로 준비와 파일 전송을 순차 실행한다. Docker 실행은 cloud-init 완료와 Docker 서비스 active를 확인한 후 진행한다.

## Nginx 컨테이너 시작 직후 curl 실패

- 증상: docker run 성공 직후 curl이 `Recv failure: Connection reset by peer`로 실패했다.
- 가설: 컨테이너 생성과 Nginx 포트 준비 사이의 짧은 지연이다.
- 검증: docker ps는 Up이었고 로그에 Nginx worker 시작이 기록됐다. 같은 내부 /health 요청을 다시 실행하니 200 / OK를 반환했다.
- 조치: start-web.sh에 최대 10회·2초 간격 readiness 재시도를 추가하고, 이미 존재하는 컨테이너는 재사용하도록 수정했다.
- 결과: 수정본의 실제 재실행 결과는 evidence/readiness-fix.txt의 OK다. 외부 HTTP/HTTPS도 200을 반환했다.
- 재발 방지: docker run의 성공을 서비스 준비 완료로 간주하지 않고 health 응답을 확인한다. 실패 시 docker ps와 logs를 함께 조사한다.
