# B3-1 · Hello Cloud

Docker Nginx 웹 서비스와 Caddy HTTPS를 AWS 프로젝트 cdsy의 시드니 리전에 배포하고 외부 접속을 검증했다. 실습 종료 리소스 정리는 `docs/cleanup-checklist.md`에서 확인한다.

## 외부 접속 증빙

아래 주소는 **최초 배포 증빙의 주소**이며 현재 운영 서비스가 아니다. 최초 배포와 별도 재검증을 구분한다.

| 증거 구분 | 당시 공용 IP | 상태·상세 |
| --- | --- | --- |
| 최초 배포 | 13.236.1.62 | 최초 외부 접속 증빙; 정리 후 접속 불가 |
| 별도 재검증 | 3.106.167.194 | 재검증 후 자원 삭제; `docs/evidence-provenance.md` 참조 |

선택 방식은 **B**이다. `GET http://13.236.1.62/health`가 **HTTP 200**, 고정 응답 **OK**를 반환했다.
- HTTP 페이지: http://13.236.1.62/
- HTTPS 페이지: https://b3-1.13-236-1-62.sslip.io/
- 외부 HTTP 원본: `evidence/external-http.txt`
- 외부 HTTPS 원본: `evidence/external-https.txt` (curl 인증서 검증을 생략하지 않음)
- HTTP 스크린샷: `evidence/external-browser.jpg`
- HTTPS 스크린샷: `evidence/https-browser.jpg`

접속 주소는 증빙 수집 시점의 주소다. 리소스 정리 이후에는 응답하지 않는다.

## Docker 실행

- 웹 이미지: `nginx:1.28-alpine`
- digest: `sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236`
- TLS 이미지: `caddy:2.10-alpine`
- digest: `sha256:4c6e91c6ed0e2fa03efd5b44747b625fec79bc9cd06ac5235a779726618e530d`
- HTTP 포트: 호스트 80 → Nginx 80
- HTTPS 포트: 호스트 443 → Caddy 443 → 내부 HTTP 서비스
- 실행 방식: `sudo bash /opt/b3-1/start-web.sh`, `sudo bash /opt/b3-1/start-https.sh`
- 내부 curl 및 Docker 출력 원본: `evidence/docker-and-network.txt`
- Docker Up 원본 화면: `evidence/recheck/cloudshell-docker-health.jpg` (별도 재검증에서 AWS CloudShell SSH로 직접 실행한 화면)
- 기존 `evidence/docker-ps.jpg`는 HTML 로그 표시 화면이므로 실행 증거에서 제외한다.
- 외부 접속 스크린샷: `evidence/external-browser.jpg`

## 네트워크와 보안

VPC 10.31.0.0/16, Public Subnet 10.31.1.0/24, IGW 기본 경로, EC2 t3.micro 1대와 암호화 8GiB gp3를 사용했다. SSH는 운영자 IP /32만, HTTP/HTTPS는 공개했다. IMDSv2 필수, T3 standard credits, EBS DeleteOnTermination을 설정했다. EIP/NAT/ALB/RDS는 생성하지 않았다.
실제 배포는 별도 EC2/VPC 전용 `codyssey-b3-1-deployer` 역할로 수행했다. 실습 역할에는 AdministratorAccess, S3, RDS, IAM 권한을 부여하지 않았다. 정책과 실제 설정은 `infra/deployment-policy.json`, `evidence/`에 보관했다.

## HTTPS

무료 DNS 이름 b3-1.13-236-1-62.sslip.io가 공용 IP를 가리킨다. Caddy의 Let's Encrypt TLS-ALPN-01 검증을 443에서 수행했다. HTTP는 과제의 공용 IP /health 검증용으로 유지한다. DNS 서비스 의존성과 공용 IP 변경 시 이름 변경이 필요한 한계가 있다.

## 제출 문서

- `docs/architecture.png`
- `docs/troubleshooting.md`
- `docs/cleanup-checklist.md`
- `docs/design-and-operations.md`
- `docs/environment-exception.md`

## 요구사항 예외

원문의 서울(ap-northeast-2) 리전 요구는 충족하지 못했다. 사용자가 프로젝트 제한을 고려해 시드니(ap-southeast-2) 진행을 승인했다. 이를 서울 요구사항 통과로 표시하지 않는다.

## 원본 실행 증거 보강

증거 보강 재검증은 최초 실습과 별도 실행이다. EC2 i-0cf8f875fa410d4b2, 공용 IP 3.106.167.194, HTTPS 이름 b3-1.3-106-167-194.sslip.io를 사용했다. 실제 AWS 콘솔·CloudShell 명령·SSH Docker 화면·외부 HTTPS 화면을 `evidence/recheck/`에 저장했다. 원본 PTY 세션의 출력·시각·종료 코드도 보존했다.

CloudShell 캡처용 SSH /32와 임시 키는 캡처 직후 제거했다. 재검증 자원과 IAM 역할·정책도 삭제하고 EC2 terminated 및 실습 EBS·주소·VPC·IGW 잔여 없음으로 확인했다. 최초 실습의 자원 기록과 혼합하지 않는다. 자세한 출처는 `docs/evidence-provenance.md`를 참조한다.
