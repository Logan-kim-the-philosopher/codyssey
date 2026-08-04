# E1-1 환경 세팅

- 발표 링크: [발표용 HTML](https://Logan-kim-the-philosopher.github.io/codyssey/E1-1/)

## 챕터

- Chapter 1. 터미널 기본 조작
- Chapter 2. 파일 권한 실습
- Chapter 3. Docker 설치 및 기본 점검
- Chapter 4. Docker 컨테이너 실행 실습
- Chapter 5. Docker 기본 운영 명령
- Chapter 6. Dockerfile 기반 커스텀 이미지 제작
- Chapter 7. Docker 바인드 마운트 변경 반영
- Chapter 8. Docker 볼륨 영속성 검증
- Chapter 9. Git 설정 및 GitHub 연동
- Chapter 10. GitHub 제출 상태 확인
- Chapter 11. Docker Compose 멀티 컨테이너
- Chapter 12. 환경 변수 활용

## 실습 로그

## Chapter 1. 터미널 기본 조작

### 테마

- 상대 경로로 작업 폴더 이동
- 절대 경로로 현재 위치 확인
- 숨김 항목 포함 초기 목록 확인
- 프로젝트 디렉토리 구조 생성
- 빈 파일 생성
- 내용 파일 생성과 리다이렉션
- cat으로 파일 내용 확인
- 파일 복사와 원본 보존
- mv로 파일 이름변경
- rm으로 파일 삭제
- 삭제 후 상위 디렉토리 상태 확인
- 복사/이름변경 후 하위 디렉토리 상태 확인
- 복사본 내용 보존 확인

### 상대 경로로 작업 폴더 이동

```bash
$ cd artifacts/e1-1/work
```

### 절대 경로로 현재 위치 확인

```bash
$ pwd
/Users/hskim/.codex/.chatgpt-projects/g-p-6a68a406143081918c0b2c94f50646d9/artifacts/e1-1/work
```

### 숨김 항목 포함 초기 목록 확인

```bash
$ ls -la
total 0
drwxr-xr-x@ 2 hskim  staff   64 Aug  3 11:28 .
drwxr-xr-x@ 6 hskim  staff  192 Aug  3 11:28 ..
```

### 프로젝트 디렉토리 구조 생성

```bash
$ mkdir -p terminal-practice/subdir
```

### 빈 파일 생성

```bash
$ touch terminal-practice/empty.txt
```

### 내용 파일 생성과 리다이렉션

```bash
$ printf "Codyssey terminal practice\n" > terminal-practice/note.txt
```

### cat으로 파일 내용 확인

```bash
$ cat terminal-practice/note.txt
Codyssey terminal practice
```

### 파일 복사와 원본 보존

```bash
$ cp terminal-practice/note.txt terminal-practice/subdir/note-copy.txt
```

### mv로 파일 이름변경

```bash
$ mv terminal-practice/subdir/note-copy.txt terminal-practice/subdir/renamed-note.txt
```

### rm으로 파일 삭제

```bash
$ rm terminal-practice/empty.txt
```

### 삭제 후 상위 디렉토리 상태 확인

```bash
$ ls -la terminal-practice
total 8
drwxr-xr-x@ 4 hskim  staff  128 Aug  3 11:33 .
drwxr-xr-x@ 3 hskim  staff   96 Aug  3 11:33 ..
-rw-r--r--@ 1 hskim  staff   27 Aug  3 11:33 note.txt
drwxr-xr-x@ 3 hskim  staff   96 Aug  3 11:33 subdir
```

### 복사/이름변경 후 하위 디렉토리 상태 확인

```bash
$ ls -la terminal-practice/subdir
total 8
drwxr-xr-x@ 3 hskim  staff   96 Aug  3 11:33 .
drwxr-xr-x@ 4 hskim  staff  128 Aug  3 11:33 ..
-rw-r--r--@ 1 hskim  staff   27 Aug  3 11:33 renamed-note.txt
```

### 복사본 내용 보존 확인

```bash
$ cat terminal-practice/subdir/renamed-note.txt
Codyssey terminal practice
```

### 증빙

- submissions/E1-1/terminal-practice

## Chapter 2. 파일 권한 실습

### 테마

- 권한 비교용 디렉토리 준비
- 권한 비교용 파일 생성
- 변경 전 755/644 기본 권한 확인
- 600 파일 권한으로 소유자만 허용
- 700 디렉토리 권한으로 소유자만 허용
- 제한 후 r/w/x 권한 비트 확인
- 644 파일 권한으로 읽기 권한 복원
- 755 디렉토리 권한으로 탐색 권한 복원
- 755/644 숫자 권한 최종 비교

### 권한 비교용 디렉토리 준비

```bash
$ mkdir -p permission-practice
```

### 권한 비교용 파일 생성

```bash
$ printf "permission test\n" > permission-practice/sample.txt
```

### 변경 전 755/644 기본 권한 확인

```bash
$ ls -ld permission-practice permission-practice/sample.txt
drwxr-xr-x@ 3 hskim  staff  96 Aug  3 11:42 permission-practice
-rw-r--r--@ 1 hskim  staff  16 Aug  3 11:42 permission-practice/sample.txt
```

### 600 파일 권한으로 소유자만 허용

```bash
$ chmod 600 permission-practice/sample.txt
```

### 700 디렉토리 권한으로 소유자만 허용

```bash
$ chmod 700 permission-practice
```

### 제한 후 r/w/x 권한 비트 확인

```bash
$ ls -ld permission-practice permission-practice/sample.txt
drwx------@ 3 hskim  staff  96 Aug  3 11:42 permission-practice
-rw-------@ 1 hskim  staff  16 Aug  3 11:42 permission-practice/sample.txt
```

### 644 파일 권한으로 읽기 권한 복원

```bash
$ chmod 644 permission-practice/sample.txt
```

### 755 디렉토리 권한으로 탐색 권한 복원

```bash
$ chmod 755 permission-practice
```

### 755/644 숫자 권한 최종 비교

```bash
$ ls -ld permission-practice permission-practice/sample.txt
drwxr-xr-x@ 3 hskim  staff  96 Aug  3 11:42 permission-practice
-rw-r--r--@ 1 hskim  staff  16 Aug  3 11:42 permission-practice/sample.txt
```

### 증빙

- submissions/E1-1/permission-practice

## Chapter 3. Docker 설치 및 기본 점검

### 테마

- Docker CLI 버전 확인
- Docker 엔진/데몬 통신 상태 확인

### Docker CLI 버전 확인

```bash
$ docker --version
Docker version 29.6.2, build dfc4efb
```

### Docker 엔진/데몬 통신 상태 확인

```bash
$ docker info
Client:
 Version:    29.6.2
 Context:    desktop-linux

Server:
 Server Version: 29.6.2
 Containers: 2
 Images: 2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: aarch64
```


## Chapter 4. Docker 컨테이너 실행 실습

### 테마

- 이미지 pull과 hello-world 컨테이너 실행
- 호스트와 분리된 Ubuntu 컨테이너 내부 명령

### 이미지 pull과 hello-world 컨테이너 실행

```bash
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
Digest: sha256:ec153840d1e635ac434fab5e377081f17e0e15afab27beb3f726c3265039cfff
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

### 호스트와 분리된 Ubuntu 컨테이너 내부 명령

```bash
$ docker run --rm ubuntu bash -lc "pwd && ls && echo inside-ubuntu"
/
bin
boot
dev
etc
home
lib
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
inside-ubuntu
```


## Chapter 5. Docker 기본 운영 명령

### 테마

- 종료 컨테이너 표준출력 로그 재확인
- 실행 중 컨테이너 상태 만들기
- 실행 중 컨테이너 리소스 사용량 확인
- 실습 컨테이너 삭제 정리

### 종료 컨테이너 표준출력 로그 재확인

```bash
$ docker logs practical_perlman
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

### 실행 중 컨테이너 상태 만들기

```bash
$ docker run -d --name codyssey-stats-test ubuntu sleep 60
4558f0c41588b0fd0f1e4b0a8d8d8316c1a9f3e69e8f7efadbeef0000000000
```

### 실행 중 컨테이너 리소스 사용량 확인

```bash
$ docker stats --no-stream codyssey-stats-test
CONTAINER ID   NAME                  CPU %     MEM USAGE / LIMIT     MEM %     NET I/O       BLOCK I/O   PIDS
4558f0c41588   codyssey-stats-test   0.00%     1.633MiB / 7.75GiB   0.02%     872B / 126B   0B / 0B     1
```

### 실습 컨테이너 삭제 정리

```bash
$ docker rm -f codyssey-stats-test
codyssey-stats-test
```


## Chapter 6. Dockerfile 기반 커스텀 이미지 제작

### 테마

- 웹 서버 소스 디렉토리 생성
- 정적 HTML 소스 작성
- 정적 HTML 소스 내용 확인
- Dockerfile 작성
- Dockerfile 내용 확인
- Dockerfile 기반 커스텀 이미지 빌드
- 빌드된 이미지와 실행 전 상태 확인
- 이미지를 컨테이너로 실행
- 호스트 포트와 컨테이너 포트 매핑 확인
- 호스트 포트로 웹 서버 접속 확인

### 웹 서버 소스 디렉토리 생성

```bash
$ mkdir -p web-server/site
```

### 정적 HTML 소스 작성

```bash
$ printf '<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title>Codyssey E1-1</title>
</head>
<body>
  <h1>Codyssey E1-1 Docker Web Server</h1>
  <p>NGINX custom image is running.</p>
</body>
</html>
' > web-server/site/index.html
```

### 정적 HTML 소스 내용 확인

```bash
$ cat web-server/site/index.html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title>Codyssey E1-1</title>
</head>
<body>
  <h1>Codyssey E1-1 Docker Web Server</h1>
  <p>NGINX custom image is running.</p>
</body>
</html>
```

### Dockerfile 작성

```bash
$ printf 'FROM nginx:alpine
LABEL org.opencontainers.image.title="codyssey-e1-1-web"
ENV APP_ENV=practice
COPY site/ /usr/share/nginx/html/
' > web-server/Dockerfile
```

### Dockerfile 내용 확인

```bash
$ cat web-server/Dockerfile
FROM nginx:alpine
LABEL org.opencontainers.image.title="codyssey-e1-1-web"
ENV APP_ENV=practice
COPY site/ /usr/share/nginx/html/
```

### Dockerfile 기반 커스텀 이미지 빌드

```bash
$ docker build -t codyssey-e1-1-web:1.0 web-server
#0 building with "desktop-linux" instance using docker driver
#1 [internal] load build definition from Dockerfile
#1 DONE 0.0s
#2 [internal] load metadata for docker.io/library/nginx:alpine
#2 DONE 0.7s
#3 [internal] load build context
#3 DONE 0.0s
#4 [1/2] FROM docker.io/library/nginx:alpine
#4 DONE 0.0s
#5 [2/2] COPY site/ /usr/share/nginx/html/
#5 DONE 0.0s
#6 exporting to image
#6 naming to docker.io/library/codyssey-e1-1-web:1.0 done
#6 DONE 0.0s
```

### 빌드된 이미지와 실행 전 상태 확인

```bash
$ docker images codyssey-e1-1-web:1.0
REPOSITORY          TAG       IMAGE ID       SIZE
codyssey-e1-1-web   1.0       925866189032   92MB
```

### 이미지를 컨테이너로 실행

```bash
$ docker run -d --name codyssey-web-8080 -p 8080:80 codyssey-e1-1-web:1.0
112816b77449f08d1e445711d492e4eb42d78ca2ac5e769a341ad7b600000000
```

### 호스트 포트와 컨테이너 포트 매핑 확인

```bash
$ docker ps --filter name=codyssey-web-8080
CONTAINER ID   IMAGE                    COMMAND                  STATUS        PORTS                                      NAMES
112816b77449   codyssey-e1-1-web:1.0    "/docker-entrypoint.…"   Up 1 minute   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   codyssey-web-8080
```

### 호스트 포트로 웹 서버 접속 확인

```bash
$ curl http://localhost:8080
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title>Codyssey E1-1</title>
</head>
<body>
  <h1>Codyssey E1-1 Docker Web Server</h1>
  <p>NGINX custom image is running.</p>
</body>
</html>
```

### 증빙

- submissions/E1-1/web-server/Dockerfile
- submissions/E1-1/web-server/site/index.html
### 증빙

- submissions/E1-1/web-server
![웹 서버 컨테이너 실행과 포트 매핑 접속 증거](../../docs/E1-1/assets/log-8-2-port-8080-browser.png)

`submissions/E1-1/evidence/port-8080-browser.png`


## Chapter 7. Docker 바인드 마운트 변경 반영

### 테마

- 바인드 마운트용 호스트 폴더 준비
- 변경 전 호스트 HTML 파일 작성
- 변경 전 호스트 HTML 내용 확인
- 읽기 전용 바인드 마운트 컨테이너 실행
- 호스트 파일 변경 전 컨테이너 응답 확인
- 호스트 HTML 파일 수정
- 수정 후 호스트 HTML 내용 확인
- 호스트 변경이 컨테이너 응답에 반영됨 확인

### 바인드 마운트용 호스트 폴더 준비

```bash
$ mkdir -p bind-mount-site
```

### 변경 전 호스트 HTML 파일 작성

```bash
$ printf '<!doctype html>
<html lang="ko">
<body>
  <h1>Bind Mount Before</h1>
</body>
</html>
' > bind-mount-site/index.html
```

### 변경 전 호스트 HTML 내용 확인

```bash
$ cat bind-mount-site/index.html
<!doctype html>
<html lang="ko">
<body>
  <h1>Bind Mount Before</h1>
</body>
</html>
```

### 읽기 전용 바인드 마운트 컨테이너 실행

```bash
$ docker run -d --name codyssey-bind-8081 -p 8081:80 -v "$PWD/bind-mount-site:/usr/share/nginx/html:ro" nginx:alpine
bcbc84a0e7964dfb4db66fc3721110dd87ef5e2db1242765a1fe6f0000000000
```

### 호스트 파일 변경 전 컨테이너 응답 확인

```bash
$ curl http://localhost:8081
<!doctype html>
<html lang="ko">
<body>
  <h1>Bind Mount Before</h1>
</body>
</html>
```

### 호스트 HTML 파일 수정

```bash
$ printf '<!doctype html>
<html lang="ko">
<body>
  <h1>Bind Mount After</h1>
</body>
</html>
' > bind-mount-site/index.html
```

### 수정 후 호스트 HTML 내용 확인

```bash
$ cat bind-mount-site/index.html
<!doctype html>
<html lang="ko">
<body>
  <h1>Bind Mount After</h1>
</body>
</html>
```

### 호스트 변경이 컨테이너 응답에 반영됨 확인

```bash
$ curl http://localhost:8081
<!doctype html>
<html lang="ko">
<body>
  <h1>Bind Mount After</h1>
</body>
</html>
```

### 증빙

- submissions/E1-1/bind-mount-site/index.html
![호스트 파일 변경 전후 컨테이너 응답 비교 증거](../../docs/E1-1/assets/log-9-2-bind-mount-before.png)

`submissions/E1-1/evidence/bind-mount-before.png`

![호스트 파일 변경 전후 컨테이너 응답 비교 증거](../../docs/E1-1/assets/log-9-3-bind-mount-after.png)

`submissions/E1-1/evidence/bind-mount-after.png`


## Chapter 8. Docker 볼륨 영속성 검증

### 테마

- 컨테이너와 분리된 Docker 볼륨 생성
- 첫 컨테이너에서 볼륨 데이터 쓰기
- 데이터 작성 컨테이너 삭제
- 새 컨테이너에서 볼륨 데이터 확인
- 볼륨 검증 컨테이너 정리

### 컨테이너와 분리된 Docker 볼륨 생성

```bash
$ docker volume create codyssey-volume-data
codyssey-volume-data
```

### 첫 컨테이너에서 볼륨 데이터 쓰기

```bash
$ docker run --name codyssey-vol-1 -v codyssey-volume-data:/data ubuntu bash -lc "echo persistent-data > /data/message.txt && cat /data/message.txt"
persistent-data
```

### 데이터 작성 컨테이너 삭제

```bash
$ docker rm codyssey-vol-1
codyssey-vol-1
```

### 새 컨테이너에서 볼륨 데이터 확인

```bash
$ docker run --name codyssey-vol-2 -v codyssey-volume-data:/data ubuntu bash -lc "cat /data/message.txt"
persistent-data
```

### 볼륨 검증 컨테이너 정리

```bash
$ docker rm codyssey-vol-2
codyssey-vol-2
```


## Chapter 9. Git 설정 및 GitHub 연동

### 테마

- 로컬 Git 설치 버전 확인
- 로컬 커밋 사용자 이름 설정 확인
- 로컬 커밋 사용자 이메일 설정 확인
- 기본 브랜치 main 설정 확인
- Git 전역 설정과 개인정보 마스킹 확인
- GitHub 원격 협업 플랫폼 인증 확인
- 로컬 repository 초기화 전 상태 확인
- 원격 repository 연결 전 상태 확인
- 로컬 repository 초기화
- 로컬 main 브랜치 확인
- 커밋 전 untracked 파일 상태 확인
- 제출 제외 규칙을 .gitignore로 재현 가능하게 기록
- 제출 대상 파일을 Git index에 추가
- 스테이징된 제출 파일 확인

### 로컬 Git 설치 버전 확인

```bash
$ git --version
git version 2.55.0
```

### 로컬 커밋 사용자 이름 설정 확인

```bash
$ git config --global user.name
hskim
```

### 로컬 커밋 사용자 이메일 설정 확인

```bash
$ git config --global user.email
y***@gmail.com
```

### 기본 브랜치 main 설정 확인

```bash
$ git config --global init.defaultBranch
main
```

### Git 전역 설정과 개인정보 마스킹 확인

```bash
$ git config --list --global
init.defaultbranch=main
pull.rebase=false
core.editor=hx
user.name=hskim
user.email=y***@gmail.com
```

### GitHub 원격 협업 플랫폼 인증 확인

```bash
$ gh auth status
github.com
  ✓ Logged in to github.com account Logan-kim-the-philosopher
  - Active account: true
  - Git operations protocol: ssh
```

### 로컬 repository 초기화 전 상태 확인

```bash
$ git status
fatal: not a git repository (or any of the parent directories): .git
```

### 원격 repository 연결 전 상태 확인

```bash
$ git remote -v
fatal: not a git repository (or any of the parent directories): .git
```

### 로컬 repository 초기화

```bash
$ git init
Initialized empty Git repository in /Users/hskim/.codex/.chatgpt-projects/g-p-6a68a406143081918c0b2c94f50646d9/.git/
```

### 로컬 main 브랜치 확인

```bash
$ git branch --show-current
main
```

### 커밋 전 untracked 파일 상태 확인

```bash
$ git status --short
?? .gitignore
?? README.md
?? submissions/
?? docs/
```

### 제출 제외 규칙을 .gitignore로 재현 가능하게 기록

```bash
$ printf '.omx/
AGENTS.md
codyssey/
submissions/E1-1/checklist.txt
' > .gitignore
```

### 제출 대상 파일을 Git index에 추가

```bash
$ git add README.md docs/ submissions/E1-1 .gitignore
```

### 스테이징된 제출 파일 확인

```bash
$ git status --short
A  .gitignore
A  README.md
A  submissions/E1-1/README.md
A  submissions/E1-1/checklist.txt
A  submissions/E1-1/logs/practice.jsonl
A  submissions/E1-1/web-server/Dockerfile
A  docs/E1-1/index.html
A  docs/index.html
```

### 증빙

![Git 버전과 전역 설정 확인 증거](../../docs/E1-1/assets/log-11-1-vscode-github-link.png)

`submissions/E1-1/evidence/vscode-github-link.png`

### 증빙

- .gitignore
- README.md
- docs/index.html

## Chapter 10. GitHub 제출 상태 확인

### 테마

- push 후 작업 트리 정리 상태 확인
- 제출 기준 커밋 확인
- Git 원격 저장소 연결 확인
- GitHub 공개 repository 상태 확인
- GitHub Pages 배포 설정 확인
- GitHub Pages 루트 URL 응답 확인
- 과제별 발표 URL 응답 확인

### push 후 작업 트리 정리 상태 확인

```bash
$ git status --short
```

### 제출 기준 커밋 확인

```bash
$ git log -1 --oneline
300d1a3 Add E1-1 submission verification
```

### Git 원격 저장소 연결 확인

```bash
$ git remote -v
origin	git@github.com:Logan-kim-the-philosopher/codyssey.git (fetch)
origin	git@github.com:Logan-kim-the-philosopher/codyssey.git (push)
```

### GitHub 공개 repository 상태 확인

```bash
$ gh repo view Logan-kim-the-philosopher/codyssey --json nameWithOwner,url,visibility,defaultBranchRef
{"defaultBranchRef":{"name":"main"},"nameWithOwner":"Logan-kim-the-philosopher/codyssey","url":"https://github.com/Logan-kim-the-philosopher/codyssey","visibility":"PUBLIC"}
```

### GitHub Pages 배포 설정 확인

```bash
$ gh api repos/Logan-kim-the-philosopher/codyssey/pages
{"status":"built","html_url":"https://logan-kim-the-philosopher.github.io/codyssey/","source":{"branch":"main","path":"/docs"},"public":true}
```

### GitHub Pages 루트 URL 응답 확인

```bash
$ curl -I https://logan-kim-the-philosopher.github.io/codyssey/
HTTP/2 200
```

### 과제별 발표 URL 응답 확인

```bash
$ curl -I https://logan-kim-the-philosopher.github.io/codyssey/E1-1/
HTTP/2 200
```


## Chapter 11. Docker Compose 멀티 컨테이너

### 테마

- Compose 작업 폴더 준비
- 웹 서비스 정적 HTML 작성
- 웹 서비스 정적 HTML 내용 확인
- 멀티 서비스 compose.yml 작성
- Compose 설정 내용 확인
- Compose 멀티 컨테이너 실행
- Compose 서비스 상태 확인
- Compose 웹 서비스 응답 확인
- Compose 서비스 로그 확인
- Compose 멀티 컨테이너 정리

### Compose 작업 폴더 준비

```bash
$ mkdir -p compose-bonus/web
```

### 웹 서비스 정적 HTML 작성

```bash
$ printf '<!doctype html>
<html lang="ko">
<body>
  <h1>Compose Web</h1>
  <p>multi-container bonus</p>
</body>
</html>
' > compose-bonus/web/index.html
```

### 웹 서비스 정적 HTML 내용 확인

```bash
$ cat compose-bonus/web/index.html
<!doctype html>
<html lang="ko">
<body>
  <h1>Compose Web</h1>
  <p>multi-container bonus</p>
</body>
</html>
```

### 멀티 서비스 compose.yml 작성

```bash
$ printf 'services:
  web:
    image: nginx:alpine
    ports:
      - "8082:80"
    volumes:
      - ./web:/usr/share/nginx/html:ro
    depends_on:
      - helper
  helper:
    image: ubuntu:latest
    command: sleep infinity
' > compose-bonus/compose.yml
```

### Compose 설정 내용 확인

```bash
$ cat compose-bonus/compose.yml
services:
  web:
    image: nginx:alpine
    ports:
      - "8082:80"
    volumes:
      - ./web:/usr/share/nginx/html:ro
    depends_on:
      - helper
  helper:
    image: ubuntu:latest
    command: sleep infinity
```

### Compose 멀티 컨테이너 실행

```bash
$ docker compose -f compose-bonus/compose.yml up -d
Network compose-bonus_default Created
Container compose-bonus-helper-1 Created
Container compose-bonus-web-1 Created
Container compose-bonus-helper-1 Started
Container compose-bonus-web-1 Started
```

### Compose 서비스 상태 확인

```bash
$ docker compose -f compose-bonus/compose.yml ps
NAME                     IMAGE           COMMAND                  SERVICE   CREATED          STATUS          PORTS
compose-bonus-helper-1   ubuntu:latest   "sleep infinity"         helper    27 seconds ago   Up 26 seconds   
compose-bonus-web-1      nginx:alpine    "/docker-entrypoint.…"   web       27 seconds ago   Up 26 seconds   0.0.0.0:8082->80/tcp, [::]:8082->80/tcp
```

### Compose 웹 서비스 응답 확인

```bash
$ curl http://localhost:8082
<!doctype html>
<html lang="ko">
<body>
  <h1>Compose Web</h1>
  <p>multi-container bonus</p>
</body>
</html>
```

### Compose 서비스 로그 확인

```bash
$ docker compose -f compose-bonus/compose.yml logs --tail=20
web-1  | /docker-entrypoint.sh: Configuration complete; ready for start up
web-1  | 2026/08/03 10:11:07 [notice] 1#1: nginx/1.31.3
web-1  | 192.168.65.1 - - [03/Aug/2026:10:11:57 +0000] "GET / HTTP/1.1" 200 110 "-" "curl/8.7.1" "-"
```

### Compose 멀티 컨테이너 정리

```bash
$ docker compose -f compose-bonus/compose.yml down
Container compose-bonus-web-1 Removed
Container compose-bonus-helper-1 Removed
Network compose-bonus_default Removed
```


## Chapter 12. 환경 변수 활용

### 테마

- 환경 변수 실습 폴더 준비
- 환경 변수 compose.yml 작성
- 환경 변수 compose.yml 내용 확인
- 초기 Compose 문법 오류 확인
- Compose config로 오류 위치 확인
- command 한 줄화로 YAML 구조 수정
- Compose config로 변수 치환 상태 확인
- 환경 변수 Compose 서비스 실행
- 초기 웹 응답에서 변수 미확장 확인
- 셸 변수 확장 가능하도록 command 수정
- 설정 수정 후 컨테이너 재생성과 응답 재확인
- 환경 변수 Compose 정리

### 환경 변수 실습 폴더 준비

```bash
$ mkdir -p env-bonus
```

### 환경 변수 compose.yml 작성

```bash
$ printf ... > env-bonus/compose.yml
```

### 환경 변수 compose.yml 내용 확인

```bash
$ cat env-bonus/compose.yml
services:
  web:
    image: nginx:alpine
    ports:
      - "8083:80"
    environment:
      APP_MODE: bonus-env
    command: /bin/sh -c "printf "<!doctype html>\n<html lang=\"ko\">\n<body>\n  <h1>Env Bonus</h1>\n  <p>APP_MODE=$${APP_MODE}</p>\n</body>\n</html>\n" > /usr/share/nginx/html/index.html && exec nginx -g 'daemon off;'"
```

### 초기 Compose 문법 오류 확인

```bash
$ docker compose -f env-bonus/compose.yml up -d
go-yaml load error in scanner (while scanning a simple key) at L10.C1-L11.C1: could not find expected ":"
```

### Compose config로 오류 위치 확인

```bash
$ docker compose -f env-bonus/compose.yml config
go-yaml load error in scanner (while scanning a simple key) at L10.C1-L11.C1: could not find expected ":"
```

### command 한 줄화로 YAML 구조 수정

```bash
$ cat env-bonus/compose.yml
services:
  web:
    image: nginx:alpine
    ports:
      - "8083:80"
    environment:
      APP_MODE: bonus-env
    command: /bin/sh -c "printf "<!doctype html>\n<html lang=\"ko\">\n<body>\n  <h1>Env Bonus</h1>\n  <p>APP_MODE=$${APP_MODE}</p>\n</body>\n</html>\n" > /usr/share/nginx/html/index.html && exec nginx -g 'daemon off;'"
```

### Compose config로 변수 치환 상태 확인

```bash
$ docker compose -f env-bonus/compose.yml config
name: env-bonus
services:
  web:
    command:
      - /bin/sh
      - -c
      - |-
        printf "<!doctype html>
        <html lang="ko">
        <body>
          <h1>Env Bonus</h1>
          <p>APP_MODE=$${APP_MODE}</p>
        </body>
        </html>
        " > /usr/share/nginx/html/index.html && exec nginx -g 'daemon off;'
    environment:
      APP_MODE: bonus-env
    image: nginx:alpine
    ports:
      - mode: ingress
        target: 80
        published: "8083"
        protocol: tcp
```

### 환경 변수 Compose 서비스 실행

```bash
$ docker compose -f env-bonus/compose.yml up -d
Network env-bonus_default Created
Container env-bonus-web-1 Created
Container env-bonus-web-1 Started
```

### 초기 웹 응답에서 변수 미확장 확인

```bash
$ curl http://localhost:8083
<!doctype html>
<html lang="ko">
<body>
  <h1>Env Bonus</h1>
  <p>APP_MODE=${APP_MODE}</p>
</body>
</html>
```

### 셸 변수 확장 가능하도록 command 수정

```bash
$ cat env-bonus/compose.yml
services:
  web:
    image: nginx:alpine
    ports:
      - "8083:80"
    environment:
      APP_MODE: bonus-env
    command: /bin/sh -c "printf "<!doctype html>\n<html lang=\"ko\">\n<body>\n  <h1>Env Bonus</h1>\n  <p>APP_MODE=$${APP_MODE}</p>\n</body>\n</html>\n" > /usr/share/nginx/html/index.html && exec nginx -g 'daemon off;'"
```

### 설정 수정 후 컨테이너 재생성과 응답 재확인

```bash
$ docker compose -f env-bonus/compose.yml down && docker compose -f env-bonus/compose.yml up -d && curl http://localhost:8083
Container env-bonus-web-1 Removed
Network env-bonus_default Removed
Network env-bonus_default Created
Container env-bonus-web-1 Created
Container env-bonus-web-1 Started
<!doctype html>
<html lang="ko">
<body>
  <h1>Env Bonus</h1>
  <p>APP_MODE=bonus-env</p>
</body>
</html>
```

### 환경 변수 Compose 정리

```bash
$ docker compose -f env-bonus/compose.yml down
Container env-bonus-web-1 Removed
Network env-bonus_default Removed
```


