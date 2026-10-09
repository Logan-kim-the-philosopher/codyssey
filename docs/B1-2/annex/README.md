# B1-2 요즘 웹사이트 만들기

과제 요구사항과 구현 근거를 정리한 발표 자료입니다.

## 요구사항

| ID | 제목 | 상태 |
|---|---|---|
| REQ-001 | React 구조와 레이아웃 | fulfilled |
| REQ-002 | 라우팅과 Not Found | fulfilled |
| REQ-003 | 재사용 컴포넌트 | fulfilled |
| REQ-004 | React 상태와 커스텀 훅 | fulfilled |
| REQ-005 | Supabase 또는 Firebase CRUD | fulfilled |
| REQ-006 | 폼 검증과 비동기 상태 UX | fulfilled |
| REQ-007 | 일관된 로딩·에러·빈 상태 | fulfilled |
| REQ-008 | 이벤트에서 렌더링으로 이어지는 흐름 | fulfilled |
| REQ-009 | 배포·README·보안 | fulfilled |
| REQ-010 | 전역 상태 도입 | fulfilled |
| REQ-011 | 성능 최적화 | fulfilled |
| REQ-012 | 인증과 보호 라우트 | fulfilled |

## 발표 설계

### React 앱의 구조와 공통 화면

서비스가 React의 컴포넌트 구조와 공통 레이아웃 위에서 동작한다는 출발점을 설명한다.

#### 실행 가능한 React 구조와 역할 분리

**핵심 메시지:** 앱 진입점과 pages, components, hooks/lib가 역할별로 분리되어 있다.

구조 분리는 화면 단위와 재사용 로직의 책임을 나누고 이후 상태 흐름을 추적할 수 있게 한다.

**코드 근거:**
- `index.html:1-2` 브라우저가 React 진입점으로 들어오는 지점: 구조 분리는 화면 단위와 재사용 로직의 책임을 나누고 이후 상태 흐름을 추적할 수 있게 한다.
- `src/main.jsx:1-29` 브라우저가 React 진입점으로 들어오는 지점: 구조 분리는 화면 단위와 재사용 로직의 책임을 나누고 이후 상태 흐름을 추적할 수 있게 한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 프로젝트 구조와 실행 흐름을 한눈에 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 주요 화면을 잇는 공통 레이아웃

**핵심 메시지:** 헤더와 네비게이션이 주요 페이지에 공통으로 적용된다.

공통 레이아웃을 분리하면 페이지가 바뀌어도 사용자의 이동 맥락과 내비게이션 경험이 유지된다.

**코드 근거:**
- `src/main.jsx:30-71` 공통 레이아웃과 전체 화면 스타일: Auth 컨텍스트에서 사용자와 로그아웃 동작을 가져와 공통 헤더·내비게이션·라우트를 렌더링하는 Layout 컴포넌트를 구성합니다.
- `src/styles.css:17-80` 공통 레이아웃과 전체 화면 스타일: 공통 레이아웃을 분리하면 페이지가 바뀌어도 사용자의 이동 맥락과 내비게이션 경험이 유지된다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 페이지별 화면과 공통 UI의 경계를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 라우팅으로 연결된 SPA 흐름

서비스의 주요 URL과 목록·상세·예외 화면이 하나의 SPA 흐름으로 연결되는 과정을 설명한다.

#### 주요 라우트와 목록·상세 이동

**핵심 메시지:** 네비게이션에서 주요 라우트로 이동하고 목록에서 특정 상세 화면으로 이어진다.

라우트는 사용자의 의도를 URL과 페이지 컴포넌트에 연결하며 목록과 상세는 파라미터를 통해 같은 데이터 흐름을 공유한다.

**코드 근거:**
- `src/pages/Home.jsx:1-21` 홈에서 목록과 상세로 이어지는 이동: 라우트는 사용자의 의도를 URL과 페이지 컴포넌트에 연결하며 목록과 상세는 파라미터를 통해 같은 데이터 흐름을 공유한다.
- `src/components/ItemCard.jsx:1-13` 기록 내용을 상세 링크 카드로 렌더링: item.id로 상세 URL을 만들고 ItemMeta, 제목, 본문을 하나의 클릭 가능한 카드에 담는다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 주소 변화와 화면 변화의 관계를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 잘못된 주소를 처리하는 Not Found

**핵심 메시지:** 등록되지 않은 주소도 일관된 Not Found 화면으로 처리된다.

예외 라우트를 명시하면 사용자가 길을 잃지 않고 서비스의 경계를 이해할 수 있다.

**코드 근거:**
- `src/pages/NotFound.jsx:1-12` 등록되지 않은 주소의 fallback 화면: 예외 라우트를 명시하면 사용자가 길을 잃지 않고 서비스의 경계를 이해할 수 있다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 정상 라우트와 예외 라우트의 역할을 구분할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 재사용 가능한 UI 컴포넌트

props에 따라 달라지는 입력·목록·상태 UI를 작은 컴포넌트로 나누고 조립하는 기준을 설명한다.

#### props를 받아 조립하는 공통 UI

**핵심 메시지:** 페이지마다 반복되는 제목·검색·폼·목록 UI를 작은 컴포넌트로 나누고 props로 조합한다.

컴포넌트는 화면 모양과 입력 계약을 캡슐화한다. 부모 페이지는 데이터를 전달하고, 각 UI 조각은 그 값에 맞는 화면을 반환한다.

**코드 근거:**
- `src/components/Button.jsx:1-7` props로 변형되는 공통 버튼: 재사용 컴포넌트는 반복을 줄이는 것뿐 아니라 화면 간 UI 계약을 일정하게 만든다.
- `src/components/SectionHeading.jsx:1-11` 페이지 제목과 action을 받는 공통 헤더: 제목 정보와 페이지별 action을 props로 받아 같은 헤더 구조로 조립한다.
- `src/components/SearchField.jsx:1-11` 부모 상태와 연결된 검색 입력 컴포넌트: controlled input의 값과 변경 이벤트를 부모에게서 받아 여러 페이지에서 재사용한다.
- `src/components/FormField.jsx:1-8` 필드 이름과 입력 요소를 묶는 컴포넌트: label과 children을 받아 입력 필드 구조를 재사용한다.
- `src/components/ItemList.jsx:1-11` 기록 데이터를 카드 목록으로 변환: 배열을 순회해 각 항목을 ItemCard에 전달하고 그리드로 구성한다.
- `src/components/ItemMeta.jsx:1-16` 화면 종류에 따라 달라지는 기록 메타정보: variant에 따라 카드형과 상세형 메타 UI 중 하나를 반환한다.
- `src/styles.css:85-90` 공통 보조 제목의 타이포그래피: 여러 컴포넌트가 공유하는 eyebrow 클래스의 글자 스타일을 지정한다.
- `src/styles.css:114-119` 페이지 제목과 action의 가로 배치: page-head 클래스로 제목과 action을 양 끝에 정렬한다.
- `src/styles.css:126-134` 검색 입력창의 공통 스타일: search 클래스에 폭, 하단선, 여백과 글꼴 상속을 적용한다.
- `src/styles.css:135-174` 카드 목록 그리드와 카드 내부 스타일: 그리드 열, 카드 상호작용, 메타정보와 카드 내용을 정의한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 각 컴포넌트가 어떤 props를 받고 어느 페이지에서 어떻게 조립되는지 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 공통 상태 UI로 일관성 유지

**핵심 메시지:** 로딩·에러·빈 상태를 공통 컴포넌트로 표현한다.

같은 비동기 상태를 화면마다 따로 구현하지 않으면 서비스 전체의 피드백이 일관된다.

**코드 근거:**
- `src/components/Status.jsx:1-3` 공통 상태 메시지 컴포넌트: 같은 비동기 상태를 화면마다 따로 구현하지 않으면 서비스 전체의 피드백이 일관된다.
- `src/styles.css:176-190` 공통 상태 메시지 컴포넌트: 같은 비동기 상태를 화면마다 따로 구현하지 않으면 서비스 전체의 피드백이 일관된다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 상태 표현 컴포넌트가 여러 화면에서 재사용되는 이유를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### React 상태와 데이터 흐름

입력 상태, 조회 상태, 비동기 상태가 어디에 놓이고 어떤 이벤트로 바뀌는지 설명한다.

#### controlled input과 폼 상태

**핵심 메시지:** 폼 입력값은 React state가 단일 진실 공급원으로 관리한다.

입력 이벤트가 state를 바꾸고 state가 다시 input과 미리보기를 갱신하는 흐름을 보여준다.

**코드 근거:**
- `src/pages/Form.jsx:8-16` 수정 대상과 폼 입력 상태 준비: URL ID로 수정할 기록을 찾고 기존 값 또는 새 입력 기본값을 state에 둔다.
- `src/pages/Form.jsx:36-42` 제목 label과 input: title 값을 읽고 입력 변경으로 폼 state를 갱신한다.
- `src/pages/Form.jsx:43-52` 분류 select와 options: tag 값을 선택 컨트롤과 동기화한다.
- `src/pages/Form.jsx:53-60` 본문 textarea: body 값을 여러 줄 입력 컨트롤과 동기화한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 입력 이벤트에서 렌더링 변화까지의 흐름을 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 목록·상세·로딩·에러 상태

**핵심 메시지:** 데이터 상태와 요청 상태를 분리해 화면의 각 상태를 선언적으로 표현한다.

React는 현재 상태 조합에 따라 로딩, 성공, 실패, 빈 화면을 렌더링한다.

**코드 근거:**
- `src/pages/Detail.jsx:1-21` 상세 화면의 파라미터와 상태 분기: React는 현재 상태 조합에 따라 로딩, 성공, 실패, 빈 화면을 렌더링한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 비동기 데이터 상태가 UI로 바뀌는 조건을 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 커스텀 훅으로 데이터 흐름 분리

**핵심 메시지:** 반복되는 조회·갱신 로직을 커스텀 훅으로 묶어 페이지는 화면 흐름에 집중한다.

훅은 데이터 요청과 상태 전이를 재사용 가능한 단위로 추출한다.

**코드 근거:**
- `src/hooks/useItems.js:1-125` Firestore 데이터 흐름을 소유하는 커스텀 훅: 사용자별 조회와 등록·수정·삭제, 요청 상태를 커스텀 훅이 관리하고 Provider가 여러 화면에 공유한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 페이지와 데이터 로직의 책임 분리를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### Firebase 기반 CRUD

원격 데이터가 목록·상세 조회와 등록·수정·삭제로 이어지는 전체 흐름을 설명한다.

#### Firebase 원격 조회와 상세 데이터

**핵심 메시지:** Firebase를 기준으로 목록과 특정 기록의 상세 데이터를 원격에서 조회한다.

로컬 임시 데이터가 아니라 원격 저장소를 읽고 화면 상태로 반영하는 과정을 보여준다.

**코드 근거:**
- `src/lib/firebase.js:1-16` Firebase 연결과 사용자별 조회: 로컬 임시 데이터가 아니라 원격 저장소를 읽고 화면 상태로 반영하는 과정을 보여준다.
- `src/hooks/useItems.js:23-61` Firebase 연결과 사용자별 조회: useItems는 로그인 사용자의 uid로 Firestore items를 조회해 목록 상태로 반영하고, 로그아웃·오류·비동기 요청 정리를 관리합니다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 원격 데이터 기준의 목록·상세 조회를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 등록·수정·삭제 후 화면 갱신

**핵심 메시지:** 변경 성공 후 이동하거나 목록을 갱신해 CRUD 결과를 즉시 확인한다.

쓰기 작업의 완료 지점과 후속 UI 갱신을 연결해야 사용자는 저장 결과를 신뢰할 수 있다.

**코드 근거:**
- `src/hooks/useItems.js:63-122` 저장·삭제 후 목록 상태 갱신: 로그인 사용자의 기록을 Firestore에 추가·수정·삭제하고 각 결과를 로컬 목록에 즉시 반영하면서 진행 상태와 오류를 관리합니다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** CRUD 이벤트와 화면 갱신의 연결을 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 폼 검증과 비동기 UX

사용자 입력 오류와 요청 진행·실패를 폼 UI에서 어떻게 안내하는지 설명한다.

#### 필수값 검증과 가까운 오류 메시지

**핵심 메시지:** 필수 입력이 빠지면 제출을 막고 사용자가 수정할 위치를 알 수 있게 표시한다.

검증 결과를 React 상태로 관리하면 제출 전후 오류 표시를 일관되게 제어할 수 있다.

**코드 근거:**
- `src/pages/Form.jsx:17-26` 폼 제출과 필수값 검증: 비어 있는 입력을 거절하고 유효한 폼만 비동기 저장 함수에 전달한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 검증 실패가 제출 차단과 오류 표시로 이어지는 이유를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 제출 중 상태와 요청 실패 피드백

**핵심 메시지:** 제출 중에는 중복 요청을 막고, 실패하면 사용자가 재시도할 수 있는 메시지를 보여준다.

비동기 요청의 진행·실패 상태를 화면에 노출해야 사용자는 시스템이 멈춘 것으로 오해하지 않는다.

**코드 근거:**
- `src/pages/Form.jsx:35-35` 저장 실패를 form 가까이에 표시: 폼 검증 오류 또는 저장 오류가 있을 때 Status error UI를 렌더링한다.
- `src/pages/Form.jsx:61-61` 저장 중 버튼 상태 표현: busy 상태에 따라 버튼을 비활성화하고 레이블을 바꾼다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 폼 비동기 상태를 UI로 표현하는 방식을 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 로딩·성공·실패·빈 상태

핵심 화면에서 비동기 요청의 모든 결과를 빠짐없이 표현하는 기준을 설명한다.

#### 로딩에서 정상 데이터까지

**핵심 메시지:** 요청 중에는 로딩을, 데이터가 도착하면 성공 화면을 보여준다.

비동기 상태를 명시하면 화면이 순간적으로 비어 보이는 문제를 줄이고 데이터 도착을 설명할 수 있다.

**코드 근거:**
- `src/pages/Items.jsx:36-39` 목록 불러오기 실패와 진행 상태: loadError와 busy 값을 분기해 사용자에게 오류 또는 로딩 UI를 보여준다.
- `src/pages/Items.jsx:40-41` 검색 결과가 있는 경우 ItemList 표시: 필터 결과가 하나 이상이면 목록 컴포넌트에 전달한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 요청 생명주기 중 로딩과 성공의 렌더링을 구분할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 실패와 빈 결과의 구분

**핵심 메시지:** 요청 실패와 데이터가 없는 정상 결과를 서로 다른 메시지로 구분한다.

실패와 빈 상태는 사용자가 취할 다음 행동이 다르므로 별도의 상태로 다뤄야 한다.

**코드 근거:**
- `src/pages/Items.jsx:42-46` 빈 목록과 검색 결과 없음 구분: 원본 배열과 필터 배열을 비교해 서로 다른 안내 문구를 선택한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 실패와 빈 결과를 일관되게 안내하는 기준을 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 이벤트에서 렌더링까지

사용자 이벤트가 상태 또는 원격 데이터를 바꾸고 화면을 다시 그리는 연결을 설명한다.

#### 사용자 이벤트와 데이터 변경

**핵심 메시지:** 클릭·입력·제출 이벤트가 React state 또는 Firebase 변경으로 이어진다.

선언적 UI의 핵심은 이벤트 핸들러가 화면을 직접 조작하는 대신 상태를 바꾸는 데 있다.

**코드 근거:**
- `src/pages/Detail.jsx:22-37` 삭제 이벤트가 데이터를 바꾸는 지점: 선언적 UI의 핵심은 이벤트 핸들러가 화면을 직접 조작하는 대신 상태를 바꾸는 데 있다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 사용자 행동에서 데이터 변경까지의 경로를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 변경 결과가 다시 렌더링되는 지점

**핵심 메시지:** 상태가 바뀌면 목록·미리보기·알림 등 관찰 가능한 UI가 다시 렌더링된다.

상태 변화와 화면 변화를 구체적인 세 지점 이상으로 연결해 React의 동작을 확인한다.

**코드 근거:**
- `src/pages/Items.jsx:9-11` 목록 데이터와 검색어 상태 초기화: 커스텀 훅에서 기록을 받고 검색어를 React state로 시작한다.
- `src/pages/Items.jsx:31-35` 검색 입력 이벤트가 q 상태를 갱신: SearchField에 현재 검색어와 변경 이벤트를 전달한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 이벤트 → 상태 → 렌더링의 연결을 세 가지 이상 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 배포와 보안 가능한 전달

외부에서 실행 가능한 서비스와 재현 가능한 소스·환경 설정을 전달하는 기준을 설명한다.

#### 외부 배포에서 핵심 흐름 확인

**핵심 메시지:** 배포된 URL에서도 목록·상세·등록·수정·삭제가 동작해야 한다.

로컬 성공만으로는 충분하지 않으므로 배포 환경의 설정과 실제 CRUD 흐름을 함께 확인한다.

**코드 근거:**
- `vercel.json:1-3` Vercel 배포를 SPA로 연결하는 설정: 로컬 성공만으로는 충분하지 않으므로 배포 환경의 설정과 실제 CRUD 흐름을 함께 확인한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 배포 URL에서 확인해야 할 사용자 흐름을 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 저장소·README·환경변수 보안

**핵심 메시지:** 소스 저장소, 실행 문서, 환경변수 보호를 함께 갖춰 재현 가능하고 안전하게 공유한다.

배포 산출물은 코드뿐 아니라 실행 방법과 비밀값 노출 방지까지 포함해야 한다.

**코드 근거:**
- `README.md:1-10` 실행 문서와 환경변수 템플릿: 배포 산출물은 코드뿐 아니라 실행 방법과 비밀값 노출 방지까지 포함해야 한다.
- `.env.example:1-3` 실행 문서와 환경변수 템플릿: 배포 산출물은 코드뿐 아니라 실행 방법과 비밀값 노출 방지까지 포함해야 한다.
- `.gitignore:1-3` 실행 문서와 환경변수 템플릿: 배포 산출물은 코드뿐 아니라 실행 방법과 비밀값 노출 방지까지 포함해야 한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 제출에 필요한 저장소·문서·보안 점검을 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 전역 상태로 공유하는 사용자 맥락

여러 화면에서 함께 필요한 사용자·테마·알림 상태를 전역으로 공유하는 선택을 설명한다.

#### 전역 상태 제공과 화면 소비

**핵심 메시지:** 공유 상태를 전역으로 제공하고 관련 화면과 컴포넌트가 같은 값을 소비한다.

페이지 간 공통 맥락을 props로 계속 전달하는 대신 적절한 범위에서 전역 상태를 사용한다.

**코드 근거:**
- `src/lib/auth.js:1-2` 전역 Context 제공과 소비: 페이지 간 공통 맥락을 props로 계속 전달하는 대신 적절한 범위에서 전역 상태를 사용한다.
- `src/lib/store.js:1-2` 전역 Context 제공과 소비: 페이지 간 공통 맥락을 props로 계속 전달하는 대신 적절한 범위에서 전역 상태를 사용한다.
- `src/pages/Profile.jsx:1-21` 전역 Context 제공과 소비: 페이지 간 공통 맥락을 props로 계속 전달하는 대신 적절한 범위에서 전역 상태를 사용한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 전역 상태를 도입할 때의 범위와 소비 지점을 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 필요한 곳의 성능 최적화

실제 반복 렌더링이나 계산 비용이 있는 지점에 최적화 API를 적용한 근거를 설명한다.

#### 불필요한 렌더링 줄이기

**핵심 메시지:** 실제 코드의 반복 렌더링 비용이 있는 컴포넌트에 메모이제이션을 적용한다.

최적화는 API를 사용했다는 사실보다 어떤 재렌더링을 줄였고 왜 필요한지가 중요하다.

**코드 근거:**
- `src/pages/Items.jsx:12-18` 검색어와 목록에 따라 필터 결과 계산: items 또는 q가 바뀔 때 제목·본문·태그 검색을 다시 실행한다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 최적화 대상과 적용 효과를 근거와 함께 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

### 인증과 보호 라우트

로그인 상태가 인증 사용자 흐름과 보호된 화면 접근을 어떻게 제어하는지 설명한다.

#### 로그인과 로그아웃 흐름

**핵심 메시지:** 사용자는 로그인하고 로그아웃할 수 있으며 인증 상태가 앱에 반영된다.

인증 이벤트는 사용자 맥락을 만들고 이후 데이터 접근의 전제가 된다.

**코드 근거:**
- `src/main.jsx:21-29` Google 로그인과 인증 상태 반영: AuthProvider가 Firebase 인증 상태를 구독하고 Google 로그인·로그아웃 동작과 현재 사용자를 앱 전체에 제공합니다.
- `src/pages/Login.jsx:1-33` Google 로그인과 인증 상태 반영: 인증 이벤트는 사용자 맥락을 만들고 이후 데이터 접근의 전제가 된다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 인증 이벤트와 사용자 상태의 관계를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

#### 보호 라우트와 접근 제어

**핵심 메시지:** 인증되지 않은 사용자는 보호된 화면에 접근하지 못하고 로그인 흐름으로 안내된다.

보호 라우트는 인증 상태와 라우팅을 연결해 데이터 화면의 접근 경계를 만든다.

**코드 근거:**
- `src/components/ProtectedRoute.jsx:1-18` 인증 여부로 보호 화면을 가르는 라우트: 보호 라우트는 인증 상태와 라우팅을 연결해 데이터 화면의 접근 경계를 만든다.

**핵심 개념:**
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined
- **undefined:** undefined

**구현 결과:** 인증 상태에 따른 라우트 접근 제어를 설명할 수 있다.

**자료:** 발표 슬라이드와 코드 근거

## 슬라이드별 자료

### React 앱의 구조와 공통 화면

#### 실행 가능한 React 구조와 역할 분리

- **React 앱의 구조와 공통 화면** (chapter-cover) · 요구사항: REQ-001

undefined

- **브라우저가 React 진입점으로 들어오는 지점: index.html** (code) · 요구사항: REQ-001

- `index.html:1-2` 브라우저가 React 진입점으로 들어오는 지점

- **브라우저가 React 진입점으로 들어오는 지점: src/main.jsx** (code) · 요구사항: REQ-001

- `src/main.jsx:1-29` 브라우저가 React 진입점으로 들어오는 지점

#### 주요 화면을 잇는 공통 레이아웃

- **공통 레이아웃과 전체 화면 스타일: src/main.jsx** (code) · 요구사항: REQ-001

- `src/main.jsx:30-71` 공통 레이아웃과 전체 화면 스타일

- **공통 레이아웃과 전체 화면 스타일: src/styles.css** (code) · 요구사항: REQ-001

- `src/styles.css:17-80` 공통 레이아웃과 전체 화면 스타일

### 라우팅으로 연결된 SPA 흐름

#### 주요 라우트와 목록·상세 이동

- **라우팅으로 연결된 SPA 흐름** (chapter-cover) · 요구사항: REQ-002

undefined

- **홈에서 목록과 상세로 이어지는 이동: src/pages/Home.jsx** (code) · 요구사항: REQ-002

- `src/pages/Home.jsx:1-21` 홈에서 목록과 상세로 이어지는 이동

- **ItemCard: 기록 카드를 상세 경로로 연결** (code) · 요구사항: REQ-002, REQ-003

- `src/components/ItemCard.jsx:1-13` 기록 내용을 상세 링크 카드로 렌더링

#### 잘못된 주소를 처리하는 Not Found

- **등록되지 않은 주소의 fallback 화면: src/pages/NotFound.jsx** (code) · 요구사항: REQ-002

- `src/pages/NotFound.jsx:1-12` 등록되지 않은 주소의 fallback 화면

### 재사용 가능한 UI 컴포넌트

#### props를 받아 조립하는 공통 UI

- **재사용 가능한 UI 컴포넌트** (chapter-cover) · 요구사항: REQ-003

undefined

- **props로 변형되는 공통 버튼: src/components/Button.jsx** (code) · 요구사항: REQ-003

- `src/components/Button.jsx:1-7` props로 변형되는 공통 버튼

- **SectionHeading: 제목과 페이지별 동작을 한 줄로 조립** (code) · 요구사항: REQ-003

- `src/components/SectionHeading.jsx:1-11` 페이지 제목과 action을 받는 공통 헤더

- **SearchField: 부모의 검색 상태를 입력창에 연결** (code) · 요구사항: REQ-003

- `src/components/SearchField.jsx:1-11` 부모 상태와 연결된 검색 입력 컴포넌트

- **FormField: 입력 컨트롤과 이름을 label로 묶기** (code) · 요구사항: REQ-003

- `src/components/FormField.jsx:1-8` 필드 이름과 입력 요소를 묶는 컴포넌트

- **ItemList: 기록 배열을 카드 목록으로 바꾸기** (code) · 요구사항: REQ-003

- `src/components/ItemList.jsx:1-11` 기록 데이터를 카드 목록으로 변환

- **ItemMeta: 카드와 상세 화면에 맞춰 메타 정보 표시** (code) · 요구사항: REQ-003

- `src/components/ItemMeta.jsx:1-16` 화면 종류에 따라 달라지는 기록 메타정보

- **공통 컴포넌트가 공유하는 검색·목록 스타일** (code) · 요구사항: REQ-003

- `src/styles.css:85-90` 공통 보조 제목의 타이포그래피
- `src/styles.css:114-119` 페이지 제목과 action의 가로 배치
- `src/styles.css:126-134` 검색 입력창의 공통 스타일
- `src/styles.css:135-174` 카드 목록 그리드와 카드 내부 스타일

#### 공통 상태 UI로 일관성 유지

- **공통 상태 메시지 컴포넌트: src/components/Status.jsx** (code) · 요구사항: REQ-003

- `src/components/Status.jsx:1-3` 공통 상태 메시지 컴포넌트

- **공통 상태 메시지 컴포넌트: src/styles.css** (code) · 요구사항: REQ-003

- `src/styles.css:176-190` 공통 상태 메시지 컴포넌트

### React 상태와 데이터 흐름

#### controlled input과 폼 상태

- **React 상태와 데이터 흐름** (chapter-cover) · 요구사항: REQ-004

undefined

- **폼 입력값을 React state로 고정하는 화면: src/pages/Form.jsx** (code) · 요구사항: REQ-004

- `src/pages/Form.jsx:8-16` 수정 대상과 폼 입력 상태 준비

- **폼 입력값을 React state로 고정하는 화면: src/pages/Form.jsx** (code) · 요구사항: REQ-004

- `src/pages/Form.jsx:36-42` 제목 label과 input
- `src/pages/Form.jsx:43-52` 분류 select와 options
- `src/pages/Form.jsx:53-60` 본문 textarea

#### 목록·상세·로딩·에러 상태

- **상세 화면의 파라미터와 상태 분기: src/pages/Detail.jsx** (code) · 요구사항: REQ-004

- `src/pages/Detail.jsx:1-21` 상세 화면의 파라미터와 상태 분기

#### 커스텀 훅으로 데이터 흐름 분리

- **Firestore 데이터 흐름을 소유하는 훅: src/hooks/useItems.js** (code) · 요구사항: REQ-004

- `src/hooks/useItems.js:1-125` Firestore 데이터 흐름을 소유하는 커스텀 훅

### Firebase 기반 CRUD

#### Firebase 원격 조회와 상세 데이터

- **Firebase 기반 CRUD** (chapter-cover) · 요구사항: REQ-005

undefined

- **Firebase 연결과 사용자별 조회: src/lib/firebase.js** (code) · 요구사항: REQ-005

- `src/lib/firebase.js:1-16` Firebase 연결과 사용자별 조회

- **Firebase 연결과 사용자별 조회: src/hooks/useItems.js** (code) · 요구사항: REQ-005

- `src/hooks/useItems.js:23-61` Firebase 연결과 사용자별 조회

#### 등록·수정·삭제 후 화면 갱신

- **저장·삭제 후 목록 상태 갱신: src/hooks/useItems.js** (code) · 요구사항: REQ-005

- `src/hooks/useItems.js:63-122` 저장·삭제 후 목록 상태 갱신

### 폼 검증과 비동기 UX

#### 필수값 검증과 가까운 오류 메시지

- **폼 검증과 비동기 UX** (chapter-cover) · 요구사항: REQ-006

undefined

- **제출 전 필수값 검증: src/pages/Form.jsx** (code) · 요구사항: REQ-006

- `src/pages/Form.jsx:17-26` 폼 제출과 필수값 검증

#### 제출 중 상태와 요청 실패 피드백

- **제출 중 버튼과 실패 메시지: src/pages/Form.jsx** (code) · 요구사항: REQ-006

- `src/pages/Form.jsx:35-35` 저장 실패를 form 가까이에 표시

- **제출 중 버튼과 실패 메시지: src/pages/Form.jsx** (code) · 요구사항: REQ-006

- `src/pages/Form.jsx:61-61` 저장 중 버튼 상태 표현

### 로딩·성공·실패·빈 상태

#### 로딩에서 정상 데이터까지

- **로딩·성공·실패·빈 상태** (chapter-cover) · 요구사항: REQ-007

undefined

- **목록 화면의 로딩과 성공 렌더링: src/pages/Items.jsx** (code) · 요구사항: REQ-007

- `src/pages/Items.jsx:36-39` 목록 불러오기 실패와 진행 상태

- **목록 화면의 로딩과 성공 렌더링: src/pages/Items.jsx** (code) · 요구사항: REQ-007

- `src/pages/Items.jsx:40-41` 검색 결과가 있는 경우 ItemList 표시

#### 실패와 빈 결과의 구분

- **실패와 빈 결과를 분리하는 조건 렌더링: src/pages/Items.jsx** (code) · 요구사항: REQ-007

- `src/pages/Items.jsx:42-46` 빈 목록과 검색 결과 없음 구분

### 이벤트에서 렌더링까지

#### 사용자 이벤트와 데이터 변경

- **이벤트에서 렌더링까지** (chapter-cover) · 요구사항: REQ-008

undefined

- **삭제 이벤트가 데이터를 바꾸는 지점: src/pages/Detail.jsx** (code) · 요구사항: REQ-008

- `src/pages/Detail.jsx:22-37` 삭제 이벤트가 데이터를 바꾸는 지점

#### 변경 결과가 다시 렌더링되는 지점

- **입력 상태가 화면을 다시 렌더링하는 지점: src/pages/Items.jsx** (code) · 요구사항: REQ-008

- `src/pages/Items.jsx:9-11` 목록 데이터와 검색어 상태 초기화

- **입력 상태가 화면을 다시 렌더링하는 지점: src/pages/Items.jsx** (code) · 요구사항: REQ-008

- `src/pages/Items.jsx:31-35` 검색 입력 이벤트가 q 상태를 갱신

### 배포와 보안 가능한 전달

#### 외부 배포에서 핵심 흐름 확인

- **배포와 보안 가능한 전달** (chapter-cover) · 요구사항: REQ-009

undefined

- **Vercel 배포를 SPA로 연결하는 설정: vercel.json** (code) · 요구사항: REQ-009

- `vercel.json:1-3` Vercel 배포를 SPA로 연결하는 설정

#### 저장소·README·환경변수 보안

- **실행 문서와 환경변수 템플릿: README.md** (code) · 요구사항: REQ-009

- `README.md:1-10` 실행 문서와 환경변수 템플릿

- **실행 문서와 환경변수 템플릿: .env.example** (code) · 요구사항: REQ-009

- `.env.example:1-3` 실행 문서와 환경변수 템플릿

- **실행 문서와 환경변수 템플릿: .gitignore** (code) · 요구사항: REQ-009

- `.gitignore:1-3` 실행 문서와 환경변수 템플릿

### 전역 상태로 공유하는 사용자 맥락

#### 전역 상태 제공과 화면 소비

- **전역 상태로 공유하는 사용자 맥락** (chapter-cover) · 요구사항: REQ-010

undefined

- **전역 Context 제공과 소비: src/lib/auth.js** (code) · 요구사항: REQ-010

- `src/lib/auth.js:1-2` 전역 Context 제공과 소비

- **전역 Context 제공과 소비: src/lib/store.js** (code) · 요구사항: REQ-010

- `src/lib/store.js:1-2` 전역 Context 제공과 소비

- **전역 Context 제공과 소비: src/pages/Profile.jsx** (code) · 요구사항: REQ-010

- `src/pages/Profile.jsx:1-21` 전역 Context 제공과 소비

### 필요한 곳의 성능 최적화

#### 불필요한 렌더링 줄이기

- **필요한 곳의 성능 최적화** (chapter-cover) · 요구사항: REQ-011

undefined

- **검색 필터 계산을 useMemo로 제한: src/pages/Items.jsx** (code) · 요구사항: REQ-011

- `src/pages/Items.jsx:12-18` 검색어와 목록에 따라 필터 결과 계산

### 인증과 보호 라우트

#### 로그인과 로그아웃 흐름

- **인증과 보호 라우트** (chapter-cover) · 요구사항: REQ-012

undefined

- **Google 로그인과 인증 상태 반영: src/main.jsx** (code) · 요구사항: REQ-012

- `src/main.jsx:21-29` Google 로그인과 인증 상태 반영

- **Google 로그인과 인증 상태 반영: src/pages/Login.jsx** (code) · 요구사항: REQ-012

- `src/pages/Login.jsx:1-33` Google 로그인과 인증 상태 반영

#### 보호 라우트와 접근 제어

- **인증 여부로 보호 화면을 가르는 라우트: src/components/ProtectedRoute.jsx** (code) · 요구사항: REQ-012

- `src/components/ProtectedRoute.jsx:1-18` 인증 여부로 보호 화면을 가르는 라우트
