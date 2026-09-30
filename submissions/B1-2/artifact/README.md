# B1-2 · 요즘 웹사이트 만들기

## pulse·note

Google 로그인으로 하루의 기록을 작성하고 관리하는 React SPA입니다. 이 README는 [발표 자료](https://logan-kim-the-philosopher.github.io/codyssey/B1-2/)의 요약본이며, 과제에서 다룬 구조와 구현 흐름을 챕터별로 정리합니다.

- 서비스: [pulse·note](https://pulse-note-b1-2.vercel.app/items)
- 발표: [HTML 발표 자료](https://logan-kim-the-philosopher.github.io/codyssey/B1-2/)
- 소스 코드: [GitHub 저장소](https://github.com/Logan-kim-the-philosopher/codyssey/tree/main/submissions/B1-2)

## 발표 요약

### 1. React 앱의 구조와 공통 화면
- **실행 가능한 React 구조와 역할 분리**: HTML 진입점에서 React 앱을 시작하고, 전역 스타일과 공통 화면의 책임을 나눕니다.
- **주요 화면을 잇는 공통 레이아웃**: 페이지가 바뀌어도 탐색 요소가 일관되게 유지되는 구조를 살펴봅니다.

### 2. 라우팅으로 연결된 SPA 흐름
- **주요 라우트와 목록·상세 이동**: URL에 따라 홈, 목록, 상세, 작성 화면을 연결합니다.
- **잘못된 주소를 처리하는 Not Found**: 등록되지 않은 경로에도 사용자가 이해할 수 있는 화면을 제공합니다.

### 3. 재사용 가능한 UI 컴포넌트
- **props로 달라지는 재사용 컴포넌트**: 버튼 등 공통 UI가 전달받은 값에 따라 다르게 동작합니다.
- **공통 상태 UI로 일관성 유지**: 상태 메시지를 재사용해 화면별 표현 차이를 줄입니다.

### 4. React 상태와 데이터 흐름
- **controlled input과 폼 상태**: 입력값을 React state로 관리해 입력과 화면을 동기화합니다.
- **목록·상세·로딩·에러 상태**: 데이터와 요청 상태를 화면에 연결합니다.
- **커스텀 훅으로 데이터 흐름 분리**: 페이지 표시와 기록 조회·갱신 로직의 역할을 나눕니다.

### 5. Firebase 기반 CRUD
- **Firebase 원격 조회와 상세 데이터**: 로그인 사용자에 속한 기록을 Firestore에서 가져옵니다.
- **등록·수정·삭제 후 화면 갱신**: 원격 데이터 변경 결과가 목록과 상세 화면에 반영되는 흐름을 다룹니다.

### 6. 폼 검증과 비동기 UX
- **필수값 검증과 가까운 오류 메시지**: 제목과 내용이 비어 있는 제출을 막고 수정 방법을 안내합니다.
- **제출 중 상태와 요청 실패 피드백**: 요청 진행 여부와 실패 결과를 사용자에게 보여줍니다.

### 7. 로딩·성공·실패·빈 상태
- **로딩에서 정상 데이터까지**: 요청 전후 상태에 맞춰 목록 화면을 전환합니다.
- **실패와 빈 결과의 구분**: 불러오기 실패와 아직 기록이 없는 상황을 별도로 표현합니다.

### 8. 이벤트에서 렌더링까지
- **사용자 이벤트와 데이터 변경**: 검색 입력과 기록 삭제가 상태 또는 데이터 갱신으로 이어집니다.
- **변경 결과가 다시 렌더링되는 지점**: React가 바뀐 상태를 화면에 반영하는 과정을 확인합니다.

### 9. 배포와 보안 가능한 전달
- **외부 배포에서 핵심 흐름 확인**: 배포된 서비스에서 기록 관리 흐름을 사용할 수 있습니다.
- **저장소·README·환경변수 보안**: 실행 안내를 제공하고 Firebase 설정값은 환경변수로 관리합니다.

### 10. 전역 상태로 공유하는 사용자 맥락
- **전역 상태 제공과 화면 소비**: 인증 사용자 정보를 여러 화면에서 공유합니다.

### 11. 필요한 곳의 성능 최적화
- **불필요한 렌더링 줄이기**: 검색 결과 계산을 `useMemo`로 메모이제이션합니다.

### 12. 인증과 보호 라우트
- **로그인과 로그아웃 흐름**: Firebase Google 인증으로 사용자를 식별합니다.
- **보호 라우트와 접근 제어**: 로그인 상태에 따라 보호된 화면의 접근을 제어합니다.

## 기술 스택

React, Vite, React Router, Firebase Authentication, Cloud Firestore, CSS

## 로컬 실행

Node.js와 npm이 필요합니다. Firebase 웹 앱 설정을 `.env`에 입력한 뒤 실행합니다.

```bash
npm ci
cp .env.example .env
npm run dev
```

`.env`에 다음 환경변수를 설정하세요.

```dotenv
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_STORAGE_BUCKET=
VITE_FIREBASE_MESSAGING_SENDER_ID=
VITE_FIREBASE_APP_ID=
```

Firebase Console에서 Google 로그인을 활성화하고, Cloud Firestore를 설정해야 합니다. `.env`에는 실제 설정값이 포함될 수 있으므로 저장소에 커밋하지 마세요. 배포 환경변수는 Vercel 프로젝트 설정에서 관리합니다.

프로덕션 빌드는 `npm run build`, 로컬 미리보기는 `npm run preview`로 실행합니다.
