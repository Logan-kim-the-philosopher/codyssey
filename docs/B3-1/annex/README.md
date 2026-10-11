# B3-1 웹사이트를 인터넷에 올려 누구나 쓰게 하기

과제 요구사항과 구현 근거를 정리한 발표 자료입니다.

## 요구사항

| ID | 제목 | 상태 |
|---|---|---|
| REQ-001 | AWS・서울 리전・비루트 계정 사용 | fulfilled |
| REQ-002 | 프리 티어 범위 준수 | fulfilled |
| REQ-003 | VPC와 인터넷 연결 구성 | fulfilled |
| REQ-004 | EC2와 웹 서버 배포 | fulfilled |
| REQ-005 | 보안 그룹 최소 포트와 SSH 소스 제한 | fulfilled |
| REQ-006 | IAM 최소권한 적용 | fulfilled |
| REQ-007 | 외부 접속 검증과 README 증빙 | fulfilled |
| REQ-008 | 아키텍처 다이어그램 제출 | fulfilled |
| REQ-009 | 근거 기반 트러블슈팅 보고서 | fulfilled |
| REQ-010 | 리소스 추적과 종료 후 정리 | fulfilled |
| REQ-011 | 네트워크 흐름과 외부 도달 조건 설명 | fulfilled |
| REQ-012 | 보안 책임과 최소권한 설명 | fulfilled |
| REQ-013 | 외부 접속 장애 점검 순서 설명 | fulfilled |
| REQ-014 | IAM 권한 부족 해결 전략 설명 | fulfilled |
| REQ-015 | 인스턴스 확장 시 병목과 구성 설명 | fulfilled |
| REQ-016 | 과금 원인 추적과 정리 순서 설명 | fulfilled |
| REQ-017 | HTTPS 적용 | fulfilled |
| REQ-018 | Docker 웹 서비스 배포 | fulfilled |

## 발표 설계

### AWS・서울 리전・비루트 계정 사용

현재 프로젝트 조건을 확인하고 승인된 리전 예외를 투명하게 밝힌다.

#### 실습 환경과 리전 예외

**핵심 메시지:** 현재 프로젝트 조건을 확인하고 승인된 리전 예외를 투명하게 밝힌다.

AWS 환경, 비루트 접근, 시드니 선택 사유를 함께 설명한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 실제 시드니 수행과 승인 예외를 원문 서울 요구와 구분한다.

**자료:** 발표 슬라이드와 코드 근거

### 프리 티어 범위 준수

무료 플랜 적용 여부를 확인한 뒤 최소 구성으로 실습한다.

#### 무료 플랜 안에서 실습하기

**핵심 메시지:** 무료 플랜 적용 여부를 확인한 뒤 최소 구성으로 실습한다.

플랜·크레딧 확인과 자원 선택의 비용 경계를 설명한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 활성 무료 플랜을 확인하고 실습 규모를 제한했다.

**자료:** 발표 슬라이드와 코드 근거

### VPC와 인터넷 연결 구성

인터넷 연결은 Subnet 이름이 아니라 IGW와 라우팅 구성으로 만들어진다.

#### 인터넷으로 연결되는 네트워크 구성

**핵심 메시지:** 인터넷 연결은 Subnet 이름이 아니라 IGW와 라우팅 구성으로 만들어진다.

VPC·Subnet 생성부터 IGW 연결과 기본 경로, 아웃바운드까지 설명한다.

**코드 근거:**
- `infra/provision.py:36-38` VPC와 Subnet의 주소 공간 생성: 실습용 VPC 안에 한 개의 Subnet을 만들고 생성 ID를 기록한다.
- `infra/provision.py:39-43` IGW와 기본 경로를 Subnet에 연결: 실습 Subnet의 인터넷 목적지 트래픽을 VPC에 붙인 IGW로 전달한다.

**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 하나의 실습 네트워크에서 인터넷 통신에 성공했다.

**자료:** 발표 슬라이드와 코드 근거

### EC2와 웹 서버 배포

서버 생성 이후 접속·초기화·서비스 준비가 이어져야 응답할 수 있다.

#### EC2에서 웹 서버 실행하기

**핵심 메시지:** 서버 생성 이후 접속·초기화·서비스 준비가 이어져야 응답할 수 있다.

EC2 생성부터 SSH와 웹 서버 준비, 내부 응답까지 배포 흐름을 설명한다.

**코드 근거:**
- `infra/provision.py:31-35` EC2의 배치와 실행 조건: SSH 키와 네트워크·스토리지 조건을 지정해 실습 EC2 한 대를 생성한다.
- `infra/provision.py:47-49` EC2의 배치와 실행 조건: SSH 키와 네트워크·스토리지 조건을 지정해 실습 EC2 한 대를 생성한다.
- `infra/bootstrap.sh:1-7` 초기 부팅에서 Docker와 배포 경로 준비: Amazon Linux 부팅 시 Docker를 실행하고 웹 파일을 복사할 디렉터리를 만든다.
- `web/nginx.conf:1-12` Nginx 정적 페이지와 고정 health 응답: 80 포트에서 웹 파일을 제공하고 /health 요청에 고정 200 응답을 반환한다.

**핵심 개념:**
- 별도 개념 없음

**구현 결과:** SSH와 내부 정상 응답을 확인했다.

**자료:** 발표 슬라이드와 코드 근거

### 보안 그룹 최소 포트와 SSH 소스 제한

공개 서비스 포트와 관리 포트에는 서로 다른 허용 범위를 적용한다.

#### 서비스는 공개하고 관리는 제한하기

**핵심 메시지:** 공개 서비스 포트와 관리 포트에는 서로 다른 허용 범위를 적용한다.

HTTP/HTTPS 공개와 SSH 출발지 제한, 전체 포트 미허용을 설명한다.

**코드 근거:**
- `infra/provision.py:26-30` 관리자 IP의 SSH와 공개 웹 포트: SSH는 관리자 공용 IP 하나에 제한하고 HTTP와 HTTPS만 인터넷에 공개한다.
- `infra/provision.py:44-46` 관리자 IP의 SSH와 공개 웹 포트: SSH는 관리자 공용 IP 하나에 제한하고 HTTP와 HTTPS만 인터넷에 공개한다.

**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 필요한 인바운드만 허용하고 SSH는 특정 IP로 제한했다.

**자료:** 발표 슬라이드와 코드 근거

### IAM 최소권한 적용

실습에 필요한 API 작업만 별도 역할에 부여한다.

#### 실습 전용 최소권한 역할

**핵심 메시지:** 실습에 필요한 API 작업만 별도 역할에 부여한다.

역할 신뢰 관계와 EC2/VPC 액션·리전·인스턴스 유형 제한을 설명한다.

**코드 근거:**
- `infra/trust-policy.json:1-12` 실습 역할을 누가 사용할 수 있는가: 관리형 로그인 역할이 실습 역할을 AssumeRole할 수 있도록 신뢰 관계를 설정한다.
- `infra/deployment-policy.json:1-52` 실습 API 목록과 시드니 리전 제한: 실습 역할이 사용할 EC2/VPC API를 명시하고 요청 리전을 시드니로 제한한다.
- `infra/deployment-policy.json:53-64` EC2 실행을 t3.micro로 제한: 실습 역할의 새 인스턴스 실행을 시드니 계정의 t3.micro로 제한한다.
- `infra/deployment-policy.json:65-84` EC2 실행에 필요한 연관 자원 허용: EC2 생성이 함께 사용하는 AMI·Subnet·SG·키·인터페이스·볼륨의 권한을 제공한다.
- `infra/provision.py:2-4` 실습 역할의 임시 자격 증명으로 실행: 로그인 프로필로 실습 역할을 맡은 뒤 이후 AWS 작업을 그 역할의 임시 자격 증명으로 실행한다.
- `infra/provision.py:8-18` 실습 역할의 임시 자격 증명으로 실행: 로그인 프로필로 실습 역할을 맡은 뒤 이후 AWS 작업을 그 역할의 임시 자격 증명으로 실행한다.

**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 실습 역할에는 무관한 서비스와 AdministratorAccess 권한을 부여하지 않았다.

**자료:** 발표 슬라이드와 코드 근거

### 외부 접속 검증과 README 증빙

외부 접속은 공개 주소에 대한 실제 요청과 결과로 설명한다.

#### 외부 요청에 정상 응답하기

**핵심 메시지:** 외부 접속은 공개 주소에 대한 실제 요청과 결과로 설명한다.

B 방식 선택, 구성 이유, README 기록과 접속 화면을 연결한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 외부에서 200과 고정 응답 OK를 확인했다.

**자료:** 발표 슬라이드와 코드 근거

### 아키텍처 다이어그램 제출

아키텍처 다이어그램은 구성요소와 연결 관계를 한눈에 보여준다.

#### 전체 구조를 한 장으로 표현하기

**핵심 메시지:** 아키텍처 다이어그램은 구성요소와 연결 관계를 한눈에 보여준다.

필수 구성요소와 외부 트래픽 경로를 다이어그램 표현 관점에서 설명한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 필수 요소와 요청 흐름을 포함한 다이어그램을 제출한다.

**자료:** 발표 슬라이드와 코드 근거

### 근거 기반 트러블슈팅 보고서

오류는 가설을 세우고 관찰 결과로 좁힌 뒤 수정한다.

#### 실제 오류를 근거로 해결하기

**핵심 메시지:** 오류는 가설을 세우고 관찰 결과로 좁힌 뒤 수정한다.

초기화 경로 오류와 서비스 시작 직후 오류를 증상부터 재발방지까지 설명한다.

**코드 근거:**
- `infra/start-web.sh:5-7` 기존 컨테이너 재사용과 준비 상태 재시도: 기존 컨테이너를 재사용하고 health 요청이 성공할 때까지 제한된 횟수로 기다린다.
- `infra/start-web.sh:13-19` 기존 컨테이너 재사용과 준비 상태 재시도: 기존 컨테이너를 재사용하고 health 요청이 성공할 때까지 제한된 횟수로 기다린다.

**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 두 실제 오류를 해결하고 수정 후 정상 응답을 확인했다.

**자료:** 발표 슬라이드와 코드 근거

### 리소스 추적과 종료 후 정리

생성 때 기록한 식별자를 기준으로 의존성 순서대로 정리한다.

#### 만든 리소스를 추적하고 정리하기

**핵심 메시지:** 생성 때 기록한 식별자를 기준으로 의존성 순서대로 정리한다.

태그·ID 추적, 삭제 결과, 미생성 항목 구분까지 설명한다.

**코드 근거:**
- `infra/provision.py:1-1` 생성한 리소스 ID를 즉시 기록: 중복 생성을 막고 생성 ID와 실습 태그를 남겨 정리 대상을 추적한다.
- `infra/provision.py:5-7` 생성한 리소스 ID를 즉시 기록: 중복 생성을 막고 생성 ID와 실습 태그를 남겨 정리 대상을 추적한다.
- `infra/provision.py:19-25` 생성한 리소스 ID를 즉시 기록: 중복 생성을 막고 생성 ID와 실습 태그를 남겨 정리 대상을 추적한다.
- `infra/cleanup.py:1-31` 기록한 실습 자원만 순서대로 정리: 실습 인스턴스 태그를 확인하고 기록된 ID를 의존성 순서에 따라 삭제한다.

**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 실습 EC2와 네트워크를 정리하고 잔여 자원을 확인했다.

**자료:** 발표 슬라이드와 코드 근거

### 네트워크 흐름과 외부 도달 조건 설명

라우팅·주소·보안 허용·서버 준비가 함께 맞아야 요청이 도달한다.

#### 외부 요청이 서버에 도달하는 조건

**핵심 메시지:** 라우팅·주소·보안 허용·서버 준비가 함께 맞아야 요청이 도달한다.

네트워크 요소 역할과 기본 경로의 이유를 실제 흐름에 연결한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 외부 요청 도달 조건과 응답 경로를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 보안 책임과 최소권한 설명

SG는 트래픽을, IAM은 AWS 작업 권한을 제어한다.

#### 네트워크 보안과 API 권한 구분하기

**핵심 메시지:** SG는 트래픽을, IAM은 AWS 작업 권한을 제어한다.

책임 차이, 포트 선정 이유, SSH/DB 공개 위험과 대안을 설명한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 네트워크 허용과 API 권한을 각각 최소화한 이유를 설명한다.

**자료:** 발표 슬라이드와 코드 근거

### 외부 접속 장애 점검 순서 설명

네트워크 경계에서 서버 내부까지 순서대로 확인하면 원인을 좁힐 수 있다.

#### 접속 장애를 순서대로 좁히기

**핵심 메시지:** 네트워크 경계에서 서버 내부까지 순서대로 확인하면 원인을 좁힐 수 있다.

라우팅→SG→퍼블릭 IP/DNS→서버 프로세스·로그 점검을 설명한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 외부와 내부 응답을 비교하며 장애 점검 순서를 제시한다.

**자료:** 발표 슬라이드와 코드 근거

### IAM 권한 부족 해결 전략 설명

권한 실패는 필요한 작업과 정책 조건을 확인해 좁게 해결한다.

#### 권한 부족을 최소 범위로 해결하기

**핵심 메시지:** 권한 실패는 필요한 작업과 정책 조건을 확인해 좁게 해결한다.

API·리소스·리전과 IAM/SCP/경계/세션 정책을 구분하는 전략을 설명한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 무작정 관리자 권한을 부여하지 않는 대응 절차를 제시한다.

**자료:** 발표 슬라이드와 코드 근거

### 인스턴스 확장 시 병목과 구성 설명

단일 서버 병목과 단일 장애 지점을 줄이려면 요청 분배와 상태 관리를 고려한다.

#### 서버 두 대로 확장한다면

**핵심 메시지:** 단일 서버 병목과 단일 장애 지점을 줄이려면 요청 분배와 상태 관리를 고려한다.

두 대 확장 가정에서 ALB·상태 검사·배포·상태 저장 구성을 설명한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 실제 추가 배포 없이 확장 설계와 비용 영향을 설명한다.

**자료:** 발표 슬라이드와 코드 근거

### 과금 원인 추적과 정리 순서 설명

서버 종료만으로 모든 과금 자원이 사라지지 않는다.

#### 비용을 추적하고 안전하게 종료하기

**핵심 메시지:** 서버 종료만으로 모든 과금 자원이 사라지지 않는다.

과금 요인, 정리 순서의 이유와 예상 밖 비용 추적 방법을 설명한다.

**코드 근거:**


**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 비용 원인과 잔여 리소스 확인 방법을 제시한다.

**자료:** 발표 슬라이드와 코드 근거

### HTTPS 적용

DNS 이름과 인증서 발급을 연결해 암호화 접속을 제공한다.

#### 무료 DNS와 HTTPS 연결

**핵심 메시지:** DNS 이름과 인증서 발급을 연결해 암호화 접속을 제공한다.

무료 이름의 IP 해석부터 TLS 검증과 HTTPS 응답까지 구현 흐름을 설명한다.

**코드 근거:**
- `infra/Caddyfile:1-12` 무료 DNS 이름과 TLS 발급 설정: 무료 DNS 이름의 HTTPS 요청을 받아 인증서를 발급하고 내부 Nginx로 전달한다.
- `infra/start-https.sh:1-9` HTTPS 컨테이너와 443 포트 연결: Caddy 컨테이너를 443에 공개하고 호스트 연결과 인증서 저장 볼륨을 지정한다.

**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 공개 인증서 검증을 포함한 HTTPS 정상 응답을 확인했다.

**자료:** 발표 슬라이드와 코드 근거

### Docker 웹 서비스 배포

이미지와 포트 매핑을 명시하면 실행 환경과 외부 접속을 연결할 수 있다.

#### Docker로 실행 환경 고정하기

**핵심 메시지:** 이미지와 포트 매핑을 명시하면 실행 환경과 외부 접속을 연결할 수 있다.

Docker 설치·컨테이너 실행·이미지 식별·포트 매핑과 실제 결과를 설명한다.

**코드 근거:**
- `web/index.html:1-33` 웹 페이지의 정보와 상태 버튼: 요청 경로와 실제 리전을 보여주고 JavaScript가 제어할 상태 표시와 버튼을 제공한다.
- `web/style.css:1-12` 페이지 구조와 상태 영역의 스타일: 읽기 쉬운 페이지 폭과 대비를 만들고 버튼의 대기·키보드 포커스 상태를 표현한다.
- `web/app.js:1-8` 버튼 입력에서 health 요청까지: 상태 확인 클릭을 받아 중복 입력을 막고 시간 제한이 있는 health 요청을 보낸다.
- `web/app.js:9-16` 정상·오류 응답과 버튼 상태 복구: 200 계열 상태와 OK 본문을 확인해 결과를 표시하고 성공·실패 모두 버튼을 다시 활성화한다.
- `infra/start-web.sh:1-4` 웹 이미지와 포트 매핑으로 실행: Nginx 이미지에 웹 파일과 설정을 읽기 전용으로 연결하고 호스트 80 포트로 공개한다.
- `infra/start-web.sh:8-12` 웹 이미지와 포트 매핑으로 실행: Nginx 이미지에 웹 파일과 설정을 읽기 전용으로 연결하고 호스트 80 포트로 공개한다.

**핵심 개념:**
- 별도 개념 없음

**구현 결과:** 컨테이너 Up, 내부·외부 응답과 두 종류 스크린샷을 기록했다.

**자료:** 발표 슬라이드와 코드 근거

## 슬라이드별 자료

### AWS・서울 리전・비루트 계정 사용

#### 실습 환경과 리전 예외

- **AWS 실습 환경과 승인된 리전 예외** (chapter-cover) · 요구사항: REQ-001

undefined

- **시드니 프로젝트에서 수행한 리전 예외** (text) · 요구사항: REQ-001

원문은 서울(ap-northeast-2) 리전을 요구한다.

새 AWS 경험의 프로젝트 cdsy는 시드니(ap-southeast-2)에 배정되어, 현재 프로젝트 모드를 유지하는 범위에서는 서울 리소스를 생성할 수 없었다. CLI의 기본 리전 설정만 바꾸어도 이 제한은 해제되지 않는다.

고급 기능 활성화에는 유료 플랜 전환과 되돌릴 수 없는 변경이 수반된다. 이를 수행하지 않고, 사용자 승인에 따라 시드니에서 동일한 네트워크·보안·배포 실습을 진행했다.

서울에서 수행했다는 뜻이 아니라, 환경 제약을 명시한 승인 예외로 완료 기준을 대체한 것이다. 원문과 원래 기준은 보존했다.

- **루트 대신 역할로 접근한 실습 환경** (text) · 요구사항: REQ-001

AWS 로그인 프로필 codyssey로 프로젝트 cdsy에 접근했다. 루트 계정으로 실습하지 않았다.

관리형 AccountFullAccessRole은 실습 역할 생성과 정리를 위한 관리 접근에 사용했다. 실제 네트워크와 EC2 생성은 codyssey-b3-1-deployer 역할을 AssumeRole한 임시 자격 증명으로 수행했다.

실습 역할에는 EC2/VPC에 필요한 작업, 시드니 리전, t3.micro 실행 조건을 부여했다. 관리 역할과 실습 역할의 권한 범위는 서로 다르다.

### 프리 티어 범위 준수

#### 무료 플랜 안에서 실습하기

- **프리 티어 범위 준수** (chapter-cover) · 요구사항: REQ-002

undefined

- **무료 플랜과 잔여 크레딧 확인** (terminal) · 요구사항: REQ-002

`aws freetier get-account-plan-state --profile codyssey --region ap-southeast-2`

```text
{
    "accountId": "888782968605",
    "accountPlanType": "FREE",
    "accountPlanStatus": "ACTIVE",
    "accountPlanRemainingCredits": {
        "amount": 100.0,
        "unit": "USD"
    },
    "accountPlanExpirationDate": "2027-04-09T12:14:00.628000+00:00"
}
```

### VPC와 인터넷 연결 구성

#### 인터넷으로 연결되는 네트워크 구성

- **VPC와 인터넷 연결 구성** (chapter-cover) · 요구사항: REQ-003

undefined

- **VPC와 Subnet의 주소 공간 생성** (code) · 요구사항: REQ-003

- `infra/provision.py:36-38` VPC와 Subnet의 주소 공간 생성

- **IGW와 기본 경로를 Subnet에 연결** (code) · 요구사항: REQ-003

- `infra/provision.py:39-43` IGW와 기본 경로를 Subnet에 연결

- **EC2에서 외부 인터넷으로 통신 성공** (terminal) · 요구사항: REQ-003

`curl -I https://example.com`

```text
HTTP/2 200 
date: Sat, 10 Oct 2026 06:08:04 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Fri, 09 Oct 2026 20:18:28 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 4673
cf-cache-status: HIT
cf-ray: a48372cbab41d5df-SYD
alt-svc: h3=":443"; ma=86400
```

### EC2와 웹 서버 배포

#### EC2에서 웹 서버 실행하기

- **EC2와 웹 서버 배포** (chapter-cover) · 요구사항: REQ-004

undefined

- **EC2의 배치와 실행 조건** (code) · 요구사항: REQ-004

- `infra/provision.py:31-35` EC2의 배치와 실행 조건
- `infra/provision.py:47-49` EC2의 배치와 실행 조건

- **초기 부팅에서 Docker와 배포 경로 준비** (code) · 요구사항: REQ-004

- `infra/bootstrap.sh:1-7` 초기 부팅에서 Docker와 배포 경로 준비

- **Nginx 정적 페이지와 고정 health 응답** (code) · 요구사항: REQ-004

- `web/nginx.conf:1-12` Nginx 정적 페이지와 고정 health 응답

- **AWS 원본 콘솔에서 확인한 EC2 실행 상태** (image) · 요구사항: REQ-004

이미지 자료: evidence/recheck/ec2-console-running.jpg (AWS 공식 EC2 콘솔의 실제 인스턴스 ID·시드니 리전·공용 IP·running 상태)

증거 보강 재검증: i-0cf8f875fa410d4b2 / 3.106.167.194. 최초 배포와 별도 실행이다. 내부 HTTP와 Docker 결과는 마지막 장의 실제 CloudShell SSH 화면으로 대조한다.

### 보안 그룹 최소 포트와 SSH 소스 제한

#### 서비스는 공개하고 관리는 제한하기

- **보안 그룹 최소 포트와 SSH 소스 제한** (chapter-cover) · 요구사항: REQ-005

undefined

- **관리자 IP의 SSH와 공개 웹 포트** (code) · 요구사항: REQ-005

- `infra/provision.py:26-30` 관리자 IP의 SSH와 공개 웹 포트
- `infra/provision.py:44-46` 관리자 IP의 SSH와 공개 웹 포트

- **임시 SSH 접근 제거 후 실제 최소 포트 규칙** (image) · 요구사항: REQ-005

이미지 자료: evidence/recheck/cloudshell-security-group.jpg (AWS CloudShell에서 실제 조회한 TCP 22의 관리자 IP /32와 80·443 공개 규칙)

재검증 SG sg-0c72c40bab7bdcfc2. 캡처용 CloudShell /32 규칙을 제거한 뒤 조회했다. 원본 화면이며 발표 HTML에 로그를 재출력한 캡처가 아니다.

### IAM 최소권한 적용

#### 실습 전용 최소권한 역할

- **IAM 최소권한 적용** (chapter-cover) · 요구사항: REQ-006

undefined

- **실습 역할을 누가 사용할 수 있는가** (code) · 요구사항: REQ-006

- `infra/trust-policy.json:1-12` 실습 역할을 누가 사용할 수 있는가

- **실습 API 목록과 시드니 리전 제한** (code) · 요구사항: REQ-006

- `infra/deployment-policy.json:1-52` 실습 API 목록과 시드니 리전 제한

- **EC2 실행을 t3.micro로 제한** (code) · 요구사항: REQ-006

- `infra/deployment-policy.json:53-64` EC2 실행을 t3.micro로 제한

- **EC2 실행에 필요한 연관 자원 허용** (code) · 요구사항: REQ-006

- `infra/deployment-policy.json:65-84` EC2 실행에 필요한 연관 자원 허용

- **실습 역할의 임시 자격 증명으로 실행** (code) · 요구사항: REQ-006

- `infra/provision.py:2-4` 실습 역할의 임시 자격 증명으로 실행
- `infra/provision.py:8-18` 실습 역할의 임시 자격 증명으로 실행

### 외부 접속 검증과 README 증빙

#### 외부 요청에 정상 응답하기

- **외부 접속 검증과 README 증빙** (chapter-cover) · 요구사항: REQ-007

undefined

- **외부 공용 IP에서 받은 200과 OK** (terminal) · 요구사항: REQ-007

`curl -i http://13.236.1.62/health`

```text
HTTP/1.1 200 OK
Server: nginx/1.28.3
Date: Sat, 10 Oct 2026 06:06:52 GMT
Content-Type: text/plain
Content-Length: 3
Connection: keep-alive
Cache-Control: no-store

OK

```

- **외부 브라우저에서 확인한 서비스 상태** (image) · 요구사항: REQ-007

이미지 자료: evidence/external-browser.jpg (EC2 공용 IP의 웹 페이지와 health 상태 200 OK를 확인한 브라우저 화면)

실제 외부 접속 시점의 화면. 검증 후 실습 자원을 정리했다.

- **B 방식과 접속 정보를 남긴 README** (text) · 요구사항: REQ-007

검증 방식 B: 공개 IP의 /health에 요청해 HTTP 200과 고정 본문 OK를 확인했다.

README에는 HTTP·HTTPS 주소, 원본 curl 출력, 브라우저 화면, Docker 이미지·digest·포트 매핑과 실행 명령을 함께 기록했다. VPC·Subnet·SG와 별도 실습 역할도 설명했다.

단일 EC2에 Nginx를 배포해 최소 구성의 요청 흐름을 확인했다. HTTPS는 Caddy와 무료 DNS 이름으로 추가했다.

접속 주소는 증빙 수집 당시 주소다. 과제의 종료 후 정리 요구에 따라 리소스를 삭제했고 현재 상시 운영 중인 사이트로 소개하지 않는다.

원본 증거 보강: 별도 재검증의 AWS 콘솔·CloudShell SSH·외부 HTTPS 화면을 evidence/recheck에 보관했다. 기존 HTML 출력 캡처는 실행 증거로 사용하지 않는다.

### 아키텍처 다이어그램 제출

#### 전체 구조를 한 장으로 표현하기

- **아키텍처 다이어그램 제출** (chapter-cover) · 요구사항: REQ-008

undefined

- **VPC부터 웹 서비스까지 전체 구성** (image) · 요구사항: REQ-008

이미지 자료: docs/architecture.png (시드니의 VPC, Public Subnet, IGW, 라우팅 테이블, SG, EC2와 Nginx·Caddy 연결 관계)

인터넷 → IGW·라우팅 → SG → EC2. HTTP는 Nginx 80, HTTPS는 Caddy 443에서 받아 내부 HTTP로 전달한다. SSH 출발지는 관리자 IP /32로 제한했다.

### 근거 기반 트러블슈팅 보고서

#### 실제 오류를 근거로 해결하기

- **근거 기반 트러블슈팅 보고서** (chapter-cover) · 요구사항: REQ-009

undefined

- **초기화 중 배포 경로가 없었던 오류** (text) · 요구사항: REQ-009

증상: SCP가 remote mkdir "/opt/b3-1/web/": No such file or directory로 실패했다.

가설: SSH는 가능하지만 cloud-init의 Docker 설치가 끝나지 않아 배포 경로 준비까지 도달하지 않았다.

근거: SSH 접속은 성공했고 cloud-init-output.log에는 패키지 설치가 진행 중이었다. 경로 부재와 초기화 상태를 함께 확인했다.

조치: sudo install -d -o ec2-user -g ec2-user /opt/b3-1/web으로 경로와 복사 권한을 준비한 뒤 SCP를 재시도해 종료 코드 0을 확인했다.

재발 방지: 경로 준비 → 파일 전송을 순서대로 실행하고 Docker 사용 전 cloud-init 완료와 서비스 active를 확인한다.

- **Nginx 준비 전에 도착한 첫 요청** (terminal) · 요구사항: REQ-009

`sudo bash /opt/b3-1/start-web.sh  # 최초 배포본 실행`

```text
Digest: sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236
Status: Downloaded newer image for nginx:1.28-alpine
f49305c0fcf26846e23b6ee188626fa3d97a6fe44349f8240444c6ad314730e4
  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                 Dload  Upload  Total   Spent   Left   Speed

  0      0   0      0   0      0      0      0                              0
curl: (56) Recv failure: Connection reset by peer

```

- **기존 컨테이너 재사용과 준비 상태 재시도** (code) · 요구사항: REQ-009

- `infra/start-web.sh:5-7` 기존 컨테이너 재사용과 준비 상태 재시도
- `infra/start-web.sh:13-19` 기존 컨테이너 재사용과 준비 상태 재시도

- **수정 후 내부 요청의 정상 응답** (terminal) · 요구사항: REQ-009

`sudo bash /opt/b3-1/start-web.sh`

```text
OK

```

### 리소스 추적과 종료 후 정리

#### 만든 리소스를 추적하고 정리하기

- **리소스 추적과 종료 후 정리** (chapter-cover) · 요구사항: REQ-010

undefined

- **생성한 리소스 ID를 즉시 기록** (code) · 요구사항: REQ-010

- `infra/provision.py:1-1` 생성한 리소스 ID를 즉시 기록
- `infra/provision.py:5-7` 생성한 리소스 ID를 즉시 기록
- `infra/provision.py:19-25` 생성한 리소스 ID를 즉시 기록

- **기록한 실습 자원만 순서대로 정리** (code) · 요구사항: REQ-010

- `infra/cleanup.py:1-31` 기록한 실습 자원만 순서대로 정리

- **실제 AWS 터미널에서 확인한 종료와 잔여 없음** (image) · 요구사항: REQ-010

이미지 자료: evidence/recheck/cloudshell-cleanup.jpg (AWS CloudShell에서 실제 조회한 재검증 EC2 terminated와 Volumes·Vpcs·InternetGateways·Addresses 빈 목록)

재검증 EC2 i-0cf8f875fa410d4b2의 종료 상태와 실습 태그 잔여 조회. 최초 실행 기록과 구분하며 미생성 EIP를 삭제 성공이라고 표시하지 않는다.

- **미생성 자원과 정리 결과를 구분** (text) · 요구사항: REQ-010

EC2: terminated 상태 확인.
EBS: 루트 DeleteOnTermination 적용, 실습 태그 볼륨 잔여 없음.
VPC·IGW: 실습 태그 잔여 없음.
Subnet·라우팅 테이블·SG·등록 키: 저장 ID 삭제 성공.
실습 IAM 역할·인라인 정책: 삭제 성공.

Elastic IP·NAT Gateway·ALB·RDS는 만들지 않았다. 미생성 항목을 삭제 성공으로 표시하지 않는다.

EC2 종료로 Nginx·Caddy와 루트 디스크의 인증서 저장 공간도 제거됐다. URL은 검증 당시 증거이며 현재 서비스를 제공하지 않는다. 최종 청구 금액은 반영 지연 때문에 0원으로 단정하지 않는다.

### 네트워크 흐름과 외부 도달 조건 설명

#### 외부 요청이 서버에 도달하는 조건

- **네트워크 흐름과 외부 도달 조건 설명** (chapter-cover) · 요구사항: REQ-011

undefined

- **VPC·Subnet·라우팅·IGW의 역할** (text) · 요구사항: REQ-011

VPC 10.31.0.0/16: 실습의 사설 주소 공간과 네트워크 격리 경계.
Subnet 10.31.1.0/24: EC2 인터페이스가 위치한 하위 주소 공간.
라우팅 테이블: 목적지 주소에 따라 다음 경로를 선택. VPC 내부는 로컬 경로, 다른 IPv4 목적지는 0.0.0.0/0 → IGW.
IGW: VPC에 연결되어 공용 IPv4와 인터넷 사이의 통신을 제공.

Public Subnet이라는 이름만 붙여도 인터넷 연결이 생기는 것은 아니다. Subnet에 연결된 테이블의 IGW 경로와 VPC의 IGW 연결을 함께 확인해야 한다.

- **퍼블릭 IP부터 서버 응답까지 필요한 조건** (text) · 요구사항: REQ-011

외부 요청: 공개 DNS 이름 또는 공용 IPv4 → IGW → EC2 인터페이스 → SG 허용 → 호스트 포트 → 컨테이너 서버.

공용 IP가 있어도 SG가 요청 포트를 허용하지 않으면 도달하지 않는다. SG가 허용해도 서버가 해당 포트에서 듣지 않으면 응답하지 않는다.

HTTP는 호스트 80에서 Nginx 80으로, HTTPS는 호스트 443에서 Caddy 443으로 전달한다. Caddy는 내부 HTTP 서버에 요청을 프록시한다.

응답과 아웃바운드 요청은 Subnet 라우팅 테이블의 인터넷 목적지 경로를 사용한다. 내부 curl과 외부 curl을 따로 확인하면 서버 내부 문제와 네트워크 경계 문제를 좁힐 수 있다.

### 보안 책임과 최소권한 설명

#### 네트워크 보안과 API 권한 구분하기

- **보안 책임과 최소권한 설명** (chapter-cover) · 요구사항: REQ-012

undefined

- **SG와 IAM의 서로 다른 책임** (text) · 요구사항: REQ-012

SG: EC2 인터페이스의 트래픽을 제어한다. TCP 80·443 공개와 SSH 22의 /32 출발지 제한이 여기에 해당한다.

IAM: AWS API에서 누가 어떤 작업을 할 수 있는지 제어한다. 실습 역할의 EC2/VPC API 목록, 시드니 리전 조건과 t3.micro 실행 조건이 여기에 해당한다.

SG에서 80을 열어도 EC2 생성 권한이 생기지 않는다. IAM에서 RunInstances를 허용해도 외부 HTTP 접속 포트가 열리지 않는다.

관리 로그인 역할은 실습 역할을 준비하는 데 사용했다. 실제 생성은 별도 역할의 임시 자격 증명으로 수행했다. 일부 네트워크 작업의 Resource * 범위는 추가로 좁힐 여지가 있다.

- **SSH와 DB 포트 공개의 위험과 대안** (text) · 요구사항: REQ-012

HTTP 80은 과제의 공용 IP 접속 검증, HTTPS 443은 암호화 접속과 인증서 검증에 필요하다. SSH 22는 관리 접속용이므로 관리자 공용 IP /32에 한정했다.

SSH와 DB 포트를 0.0.0.0/0에 열면 전 세계에서 무차별 인증 시도와 취약점 탐색을 할 수 있다. 이 구성은 DB 포트와 전체 포트 인바운드를 열지 않았다.

관리 대안: 출발지 IP 제한 또는 필요한 IAM·네트워크 설정을 갖춘 Systems Manager 접속.
DB 대안: 사설 네트워크 배치와 애플리케이션 SG를 소스로 지정.

SSM과 DB는 이번 실습에 구축하지 않았으며 개선 대안으로 설명한다. 관리자 IP가 바뀌면 SSH 허용 CIDR도 갱신해야 한다.

### 외부 접속 장애 점검 순서 설명

#### 접속 장애를 순서대로 좁히기

- **외부 접속 장애 점검 순서 설명** (chapter-cover) · 요구사항: REQ-013

undefined

- **라우팅에서 서버 로그까지 점검하는 순서** (text) · 요구사항: REQ-013

1. 라우팅: Subnet 연결 테이블, 0.0.0.0/0 → IGW, IGW의 VPC 연결 확인.
2. SG: 실제 서비스 포트와 요청 출발지 CIDR 확인. SSH는 현재 관리자 IP와 /32 값 비교.
3. 공용 IP·DNS: EC2 주소와 DNS 해석 결과 비교. 자동 공용 IPv4는 stop/start 뒤 바뀔 수 있음.
4. 서버: cloud-init 완료, Docker 서비스, docker ps·logs, 포트 리스닝과 내부 curl 확인.

내부 curl 성공·외부 실패면 네트워크 경계와 주소 설정을 우선 조사한다. 내부도 실패하면 서버 초기화·서비스 준비·설정 오류를 조사한다.

관찰된 증상에 맞는 가설 하나를 세우고 해당 설정만 수정한 뒤 같은 요청으로 재확인한다. 실제 사례에서는 컨테이너 Up 표시만으로 Nginx 준비 완료를 판단하지 않았다.

### IAM 권한 부족 해결 전략 설명

#### 권한 부족을 최소 범위로 해결하기

- **IAM 권한 부족 해결 전략 설명** (chapter-cover) · 요구사항: REQ-014

undefined

- **실패한 API에 필요한 최소 권한 찾기** (text) · 요구사항: REQ-014

권한 오류가 발생할 때의 해결 전략이다. 실제 실습에서 이 오류를 재현했다고 주장하지 않는다.

오류 메시지에서 API 액션, 사용한 역할, 요청 리전·리소스 ARN·조건을 수집한다. AWS 서비스 권한 표에서 필요한 액션과 지원 자원·조건을 찾아 정책과 대조한다.

역할 정책뿐 아니라 SCP, permissions boundary, 세션 정책의 제한을 확인한다. 명시적 Deny는 Allow 추가로 우회되지 않는다. 관리형 프로젝트의 보호 규칙도 관리자 역할의 Allow만으로 해제되지 않는다.

필요한 단일 액션과 자원 범위를 좁게 허용하고 같은 요청을 재시도한다. AdministratorAccess 추가로 문제를 덮지 않는다.

### 인스턴스 확장 시 병목과 구성 설명

#### 서버 두 대로 확장한다면

- **인스턴스 확장 시 병목과 구성 설명** (chapter-cover) · 요구사항: REQ-015

undefined

- **서버 두 대와 ALB를 가정한 확장 설계** (text) · 요구사항: REQ-015

현재 단일 EC2는 CPU·메모리·처리량의 용량 한계와 단일 장애 지점을 가진다. 공용 IP 직접 접속은 서버를 두 대 만들어도 요청을 자동 분배하지 않는다.

확장 가정: ALB → Target Group → 두 AZ의 EC2 또는 Auto Scaling Group. /health 상태 검사를 통해 응답 가능한 대상에 요청을 분배한다. 현재 고정 OK는 HTTP 프로세스의 응답 확인이며 더 깊은 애플리케이션 상태 검사로 보완할 수 있다.

동일 이미지와 설정으로 배포를 맞추고, 세션·업로드·공유 데이터가 생기면 서버 외부 저장소를 고려한다. 각 서버의 로컬 상태만 사용하면 요청 대상에 따라 결과가 달라질 수 있다.

ALB·두 번째 EC2·공유 저장소는 이번 실습에 생성하지 않았다. 추가 비용을 고려해야 하는 확장 설계로 설명한다.

### 과금 원인 추적과 정리 순서 설명

#### 비용을 추적하고 안전하게 종료하기

- **과금 원인 추적과 정리 순서 설명** (chapter-cover) · 요구사항: REQ-016

undefined

- **EC2를 꺼도 남을 수 있는 비용** (text) · 요구사항: REQ-016

과금 요인: EC2 실행 시간, 초과 CPU 크레딧, EBS 용량, 공용 IPv4, 데이터 전송, NAT Gateway·ALB 등. 무료 플랜 크레딧과 서비스 자체의 가격은 구분한다.

이번 구성: t3.micro 한 대, 8 GiB gp3, 자동 공용 IPv4. T3 standard 모드로 초과 CPU 크레딧 비용을 피하고 EIP·NAT·ALB·RDS는 생성하지 않았다.

EC2 stop만 하면 EBS가 남는다. 자동 공용 IPv4는 중지 시 해제되지만 별도 Elastic IP를 할당한 구성이라면 주소 자원도 확인해야 한다.

이번 실습은 terminate와 루트 DeleteOnTermination을 적용하고 잔여 볼륨·주소를 조회했다. 청구 반영 지연이 있어 최종 비용 0원으로 단정하지 않는다.

- **예상 밖 비용의 추적과 안전한 정리 순서** (text) · 요구사항: REQ-016

비용 추적: AWS Settings의 Billing에서 서비스·리전별 사용 내역을 확인하고, Assignment=B3-1 태그와 저장된 자원 ID를 대조한다. 무료 플랜과 크레딧 적용 상태도 확인한다.

정리 순서: EC2 종료 대기 → SG·키 정리 → 라우팅 연결 해제 → Subnet·사용자 라우팅 테이블 삭제 → IGW 분리·삭제 → VPC 삭제. 그 뒤 EBS·주소 잔여와 실습 IAM 정책·역할 정리를 확인한다.

연결 의존성을 먼저 해소하면 사용 중인 자원 삭제 오류를 줄일 수 있다. ID 기록으로 이번 실습 자원만 지정하고 다른 프로젝트 자원을 일괄 삭제하지 않는다.

종료 상태와 잔여 조회는 삭제 증거다. 최종 청구 상태는 Billing의 후속 반영 결과로 확인해야 한다.

### HTTPS 적용

#### 무료 DNS와 HTTPS 연결

- **보너스: HTTPS 적용** (chapter-cover) · 요구사항: REQ-017

undefined

- **무료 DNS 이름과 TLS 발급 설정** (code) · 요구사항: REQ-017

- `infra/Caddyfile:1-12` 무료 DNS 이름과 TLS 발급 설정

- **HTTPS 컨테이너와 443 포트 연결** (code) · 요구사항: REQ-017

- `infra/start-https.sh:1-9` HTTPS 컨테이너와 443 포트 연결

- **실제 CloudShell에서 성공한 외부 HTTPS 요청** (image) · 요구사항: REQ-017

이미지 자료: evidence/recheck/cloudshell-external-https.jpg (AWS CloudShell의 실제 curl HTTPS 명령 줄과 HTTP/2 200 및 OK)

재검증 이름 b3-1.3-106-167-194.sslip.io. -k 없이 인증서 검증을 통과한 실제 실행 화면. 기존 배포 이름과 구분한다.

- **재검증 HTTPS 브라우저의 정상 서비스 상태** (image) · 요구사항: REQ-017

이미지 자료: evidence/recheck/https-browser.jpg (재검증 무료 DNS 이름으로 실제 접속해 상태 200 OK를 확인한 웹 화면)

2026-10-10 증거 보강 재검증 화면. 실제 배포 파일과 Docker 이미지는 같고 공용 IP·DNS 이름은 새로 배정됐다. 증빙 수집 후 정리한다.

### Docker 웹 서비스 배포

#### Docker로 실행 환경 고정하기

- **보너스: Docker 웹 서비스 배포** (chapter-cover) · 요구사항: REQ-018

undefined

- **웹 페이지의 정보와 상태 버튼** (code) · 요구사항: REQ-018

- `web/index.html:1-33` 웹 페이지의 정보와 상태 버튼

- **페이지 구조와 상태 영역의 스타일** (code) · 요구사항: REQ-018

- `web/style.css:1-12` 페이지 구조와 상태 영역의 스타일

- **버튼 입력에서 health 요청까지** (code) · 요구사항: REQ-018

- `web/app.js:1-8` 버튼 입력에서 health 요청까지

- **정상·오류 응답과 버튼 상태 복구** (code) · 요구사항: REQ-018

- `web/app.js:9-16` 정상·오류 응답과 버튼 상태 복구

- **웹 이미지와 포트 매핑으로 실행** (code) · 요구사항: REQ-018

- `infra/start-web.sh:1-4` 웹 이미지와 포트 매핑으로 실행
- `infra/start-web.sh:8-12` 웹 이미지와 포트 매핑으로 실행

- **실행 중인 컨테이너와 이미지 digest** (terminal) · 요구사항: REQ-018

`docker ps
docker image inspect nginx:1.28-alpine --format '{{json .RepoDigests}}'
docker image inspect caddy:2.10-alpine --format '{{json .RepoDigests}}'`

```text
CONTAINER ID   IMAGE               COMMAND                  CREATED              STATUS              PORTS                                                              NAMES
8e5535359fff   caddy:2.10-alpine   "caddy run --config …"   56 seconds ago       Up 51 seconds       80/tcp, 2019/tcp, 443/udp, 0.0.0.0:443->443/tcp, :::443->443/tcp   b3-1-https
f49305c0fcf2   nginx:1.28-alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:80->80/tcp, :::80->80/tcp                                  b3-1-web
["nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236"]
["caddy@sha256:4c6e91c6ed0e2fa03efd5b44747b625fec79bc9cd06ac5235a779726618e530d"]
```

- **실제 CloudShell SSH의 Docker Up과 내부 응답** (image) · 요구사항: REQ-018

이미지 자료: evidence/recheck/cloudshell-docker-health.jpg (AWS CloudShell에서 EC2에 SSH 접속하여 직접 실행한 docker ps와 curl 결과)

재검증 EC2의 실제 서버 프롬프트·명령·실행 시각·컨테이너 Up·내부 200 OK 원본 화면. 기존 HTML 재출력 캡처는 증빙에서 제외했다.
