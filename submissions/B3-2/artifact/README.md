# AI Git 초안 생성기 · B3-2

Git 변경을 OpenAI REST API에 전달해 변경 요약, 커밋 메시지 또는 PR 제목·본문을 터미널에 출력하는 Python CLI다. Git 상태를 변경하거나 push·PR 생성을 수행하지 않는다. 생성 내용은 검토 후 직접 적용한다.

## 설치

Python 3.10 이상과 Git이 필요하다. 외부 Python 패키지는 사용하지 않는다.
이 폴더를 별도 저장소의 루트로 복사하거나, 수정 중인 Git 저장소 루트에서 이 폴더의 `main.py`를 절대 경로로 실행한다.

```bash
# 수정 중인 Git 프로젝트 루트(.git이 있는 디렉토리)에서
python3 /Users/hskim/Projects/codyssey/artifacts/b3-2/artifact/main.py --help
```

소스를 다른 위치로 복사했다면 경로를 바꾼다. `git status`에만 나타나는 미추적 파일은 `git diff`에 내용이 없으므로 사용자 검토 후 `git add <파일>`로 stage해야 한다. 도구가 자동으로 stage하지 않는다.

## API Key 설정

Key는 환경변수로만 읽는다. `.env` 자동 로드 기능은 없다. 실제 Key를 소스·설정 파일·README·Git·채팅에 넣지 않는다.

```bash
# YOUR_KEY는 실제 발급받은 값으로 로컬에서 설정
export AI_API_KEY="YOUR_KEY"
# 또는 OPENAI_API_KEY. 둘 다 있으면 AI_API_KEY가 우선한다.
```

명령행에 직접 입력하면 shell history에 남을 수 있다. 터미널의 비밀 입력이나 운영체제 비밀 관리 기능으로 환경변수를 주입하는 방식을 권장한다.

## 사용법

도구를 저장소 루트로 복사한 경우:

```bash
python3 main.py commit --why "오류 안내를 구체화"
python3 main.py pr --why "사용자의 잘못된 설정을 빠르게 해결" --test-plan "Key 누락과 정상 호출을 각각 확인"
python3 main.py pr --temperature 0.7 --max-tokens 1600 --model gpt-4.1-mini
python3 main.py commit --convention examples/b3-1-convention.json
python3 main.py pr --output /tmp/review-pr-draft.txt
```

`--output`은 새 파일만 만들고 기존 파일을 덮어쓰지 않는다. `-model`, `-temperature`, `-max-tokens`, `-safe-mode` 표기도 지원한다. 모델은 JSON object 출력과 temperature를 지원해야 한다. 기본값은 `gpt-4.1-mini`, temperature `0.2`, 출력 상한 `1200`토큰이다. CLI `--max-tokens`는 REST의 `max_completion_tokens`로 전달한다.

### 안전 모드

기본 ON이다. `--safe-mode`로 명시하거나 `--no-safe-mode`로 끈다.

- OpenAI/GitHub/AWS 형태 토큰, secret/token/password/API key 대입값, 이메일, 한국 휴대전화 번호, private key 블록을 마스킹한다.
- `.env` 계열, `.pem`·`.key`·`.p12`·`.pfx`, credentials, id_rsa/id_ed25519, 바이너리 diff를 제외한다.
- 기본 최대 **10개 diff 블록·200줄**. staged와 unstaged에 같은 파일이 있으면 두 블록으로 계산한다. `--max-files`, `--max-lines`로 조정한다.
- 마스킹은 줄 제한보다 먼저 수행한다. 일부 입력만 전달하면 최종 출력에 PARTIAL 안내를 붙인다.
- OFF에서도 현재 실행용 API Key는 마스킹한다. 그 외 개인정보·비밀 패턴과 전송량 제한은 OFF에서 적용하지 않는다.
- Git 출력·합산 diff 및 API 응답은 각각 1MB 상한이다. Git은 15초, API는 30초 제한 시간이다.

```bash
# Key 없이도 전송 예정 JSON을 점검할 수 있다. 실제 요청은 0회.
python3 main.py pr --dry-run --safe-mode --max-files 5 --max-lines 100
# 민감정보가 없는 합성 데이터로만 OFF 비교 권장
python3 main.py pr --dry-run --no-safe-mode
```

정규표현식은 모든 비밀을 탐지하지 못한다. 전송 전 `--dry-run`으로 검토하고 민감 파일은 Git 추적에서 제외한다. OFF는 검토된 비민감 diff에만 사용한다. 잘린 diff나 일부 제외 파일로 생성한 초안은 전체 변경을 대표하지 않을 수 있다.

### 출력 예시

아래는 **모의 API 응답으로 검증한 형식 예시**이며 실제 모델 생성 증빙이 아니다. `evidence/mock-commit.txt`, `evidence/mock-pr.txt`에 같은 형식 검증 결과가 있다.

```text
--- Change Summary ---
오류 안내 문구를 구체화

--- Commit Message ---
fix: API Key 누락 안내 개선

- 환경변수 설정 방법을 안내
----------------------
[REVIEW] AI 초안입니다. 변경 사실·제목·테스트 방법을 검토 후 적용하세요.
```

```text
--- PR Title ---
docs: 실행 안내 보강

--- PR Body ---
## Why
- 사용자가 실행 위치를 혼동할 수 있음

## What
- 프로젝트 루트 실행 방법을 문서화

## How to Test
- README 명령을 로컬에서 확인
```

## 오류와 비용

Key 누락, Git 루트 오류, 네트워크·인증·요청 제한 오류, 잘못된 JSON·본문·컨벤션, 잘린 응답을 안내하고 종료 코드 1로 종료한다. CLI 옵션 오류는 2다. 변경 없음·safe-mode 적용 후 입력 없음은 API 요청 없이 코드 0으로 종료한다. Key 누락 검사가 먼저이므로 일반 실행은 변경이 없어도 Key가 필요하다. `--dry-run`만 Key 없이 가능하다.

명령당 **최대 1회 호출**, 자동 재시도·자동 재생성 없음. 호출을 시도한 횟수를 성공·실패 모두 출력한다. 1회 호출은 무료를 뜻하지 않는다. 가격은 모델·입력·출력 토큰에 따라 달라지고 큰 diff는 입력 비용을 늘린다. dry-run과 낮은 출력 상한으로 확인하고 오류는 원인을 해결한 뒤 직접 재실행한다.

## 설계와 파라미터

- `gitgen/git.py`: 읽기 전용 status·staged/unstaged diff 수집. 외부 diff/textconv·fsmonitor 실행 차단. Git 자식 환경에는 API/BWS Key를 전달하지 않음.
- `gitgen/safety.py`: API 전송 이전에 파일 제외·마스킹·제한 적용.
- `gitgen/prompt.py`: 신뢰하지 않는 diff와 사용자 이유·테스트 계획·컨벤션을 구분해 요청 구성.
- `gitgen/api.py`: 승인된 HTTPS OpenAI 또는 Codyssey 주소에 JSON POST, 응답·HTTP 오류 처리. 리다이렉트 차단.
- `gitgen/formatting.py`: 필드·접두사·scope·불릿 검증, 제목 상한 후처리, 고정 PR 섹션 출력.
- `main.py`: 옵션·환경변수·실행 흐름·호출 횟수 관리.

분리하면 Git fixture, HTTP 모의 응답, 프롬프트와 포맷팅을 각각 검증할 수 있다. CLI 옵션은 실험 설정을 재현하기 위한 인터페이스다. temperature를 낮추면 더 안정된 표현을 기대하고 높이면 다양한 표현을 기대하지만, 같은 설정도 결과가 달라질 수 있다. max_completion_tokens는 글자 수가 아니라 출력 토큰 상한이다. 너무 낮으면 JSON이 중단될 수 있어 `finish_reason != stop`을 오류로 처리한다. 기본 1200은 짧은 제목·요약·세 섹션을 위한 시작값이며 실제 실험으로 조정해야 한다.

재생성 대신 후처리를 선택해 호출 비용을 제한한다. 제목은 최대 길이(커밋 72자, PR 80자)를 넘어가면 말줄임표로 줄인다. 커밋 50자 이하는 프롬프트의 권장값이다. 제목이 잘리면서 의미가 변할 수 있으므로 사용자 검토가 필요하다. 필수 내용이 없거나 prefix/scope가 틀리면 사실을 만들어 보충하지 않고 오류로 종료한다. 커밋 본문은 1~2개 불릿으로 출력하며 PR은 세 섹션을 고정 렌더링한다.

AI가 변경 배경·테스트 결과를 추측할 수 있으므로 `--why`·`--test-plan`을 제공하고 How to Test는 수행 완료 주장이 아닌 검증 제안으로 취급한다. 팀 적용 시에는 실제 diff에 없는 내용을 탐지하는 검증과 민감정보 정책을 우선 개선한다. 잘못된 변경 설명과 비밀 유출이 리뷰·운영에 직접 영향을 주기 때문이다.

## 팀 컨벤션 (보너스)

이전 B3-1 미션은 현재 codyssey 저장소에 있다. 최근 커밋은 `Use shared image popup renderer...`, `Submit B3-1 presentations...` 같은 영문 동사형이며 고정 prefix/scope는 없었다. 기존 README는 한국어, 증거·예외·정리 상태를 명시하는 문서 스타일이다. 이 관찰을 바탕으로 새 컨벤션을 정의했다:

- 허용 접두사: docs/fix/feat/refactor/test/chore.
- scope: `b3-1`.
- 한국어로 구체적인 변경 동사 사용.
- PR Why/What/How to Test 유지, 미수행 테스트를 완료로 표현하지 않음.

`--convention examples/b3-1-convention.json`으로 적용한다. 기본 컨벤션은 scope를 강제하지 않는다. 예제 JSON은 실제 키나 비밀을 포함하지 않는다. 형식 적용 전후의 **모의 응답 비교**는 `evidence/convention-comparison.md`에 있다. 실제 생성 전후 비교는 `evidence/real-convention-comparison.md`에 있다. 실제 이전 미션 PR은 아래 제출 섹션에 기록했다.

## 검증·남은 제출 증빙

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q main.py gitgen tests
```

테스트는 실제 임시 Git 저장소와 모의 HTTP 응답으로 동작하며 실제 API 비용을 발생시키지 않는다. 안전 모드 ON/OFF **실제 전처리 비교**는 `evidence/safety-comparison.md`에 있다. Codyssey 게이트웨이의 실제 모델 호출·파라미터 비교·컨벤션 비교는 검증했다. GitHub push와 이전 미션 실제 PR 증빙은 `evidence/github-delivery.md`와 `evidence/actual-pr-revisions.md`에 있다. 테스트 통과를 실제 API 성공이나 보너스 PR 완료로 간주하지 않는다.

공식 API 근거: [Chat Completions](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create), [GPT-4.1 mini](https://developers.openai.com/api/docs/models/gpt-4.1-mini).

## BWS · Codyssey 게이트웨이 사용 (실제 검증 완료)

Pi의 비밀 사용 규칙에 따라 macOS Keychain의 `bitwarden-bws-access-token`을 메모리에서만 읽고 BWS 실행 환경에 주입한다. 상속된 BWS 토큰은 사용하지 않는다. bws secret list/get으로 비밀을 출력하지 않는다.

```bash
# 변경 중인 Git 프로젝트 루트에서; Key 값은 명령에 넣지 않는다.
python3 /Users/hskim/Projects/codyssey/artifacts/b3-2/artifact/tools/bws_run.py commit
python3 /Users/hskim/Projects/codyssey/artifacts/b3-2/artifact/tools/bws_run.py pr
```

런처 기본값은 `https://copa.codyssey.kr/v1`, `gpt-5.4-mini`, temperature 1, 출력 상한 3000이다. Pi 설정에서 게이트웨이 주소와 모델 ID를 확인했다. 직접 실행 `main.py`의 OpenAI 기본값과 별개다.

- `bws run --no-inherit-env`의 소비 프로세스에서 CODEYSSEY_LLM_API를 AI_API_KEY로 연결한다. 다른 BWS 비밀과 접근 토큰은 실행 환경에서 제거한다.
- BWS stdout/stderr는 폐기한다. 소비 프로세스의 출력은 메모리에서 주입된 비밀 값과 대조한 뒤 별도 pipe로 전달한다. 일치하면 출력·저장 없이 실패한다.
- 키·토큰은 명령 인자, 파일, 증거, shell history에 기록하지 않는다. Git 자식에는 비밀 없는 환경만 전달한다.
- BWS 경로에서는 `--output`을 금지해 검사 전 파일 저장을 막는다. 필요하면 검사된 런처 표준출력을 파일로 리다이렉트한다.
- 게이트웨이는 `max_tokens`로 출력 상한을 전달하고 선택적 store/response_format 필드는 제외한다. OpenAI 직접 호출에는 기존 max_completion_tokens·JSON object 요청을 유지한다. 양쪽 모두 생성 응답 JSON과 출력 형식은 별도로 검증한다.
- API 주소는 승인된 두 HTTPS /v1 주소만 허용하며 리다이렉트도 차단한다. 다른 서비스로 키를 보내지 않는다.
- HTTP 오류 원문은 출력·저장하지 않는다. 원문을 메모리에서 정해진 단어와 비교해 고정된 오류 분류만 반환한다.

실제 증거: `evidence/real-gateway-commit.txt`, `evidence/real-gateway-pr.txt`, `evidence/real-parameter-comparison.md`, `evidence/real-convention-comparison.md`. 합성 테스트 저장소의 검토된 두 파일 diff만 전송했다. 성공 4회, 요청 형식 확인 과정에서 HTTP400 실패 4회; 각 명령은 최대 1회 호출했다. 과거 OpenAI 직접 주소의 HTTP401 시도 1회는 별도다. 해당 서버 오류 일부가 남은 로그는 폐기했고 사용자가 키를 회전했다.

정규표현식과 출력 검사가 모든 유출 경로를 차단한다고 보장하지 않는다. 비밀은 실행 중 프로세스 메모리·환경에 존재한다. 디버깅, 환경 덤프, 코어 덤프, 외부 오류 원문 기록을 사용하지 않는다.

## GitHub 제출 및 실제 이전 미션 적용

- [B3-2 소스 제출 PR](https://github.com/Logan-kim-the-philosopher/codyssey/pull/2)
- [B3-1 실제 문서 개선 PR](https://github.com/Logan-kim-the-philosopher/codyssey/pull/1)
- [AI 초안 → 최종 PR 수정 기록](evidence/actual-pr-revisions.md)

두 PR은 OPEN 상태이며 main 병합 및 발표 자료 게시 단계는 아직 수행하지 않았다.
