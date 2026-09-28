# pulse·note

Google 로그인으로 접속해 하루의 기록을 작성하고 관리하는 React SPA입니다. 기록은 Firebase Authentication 사용자별로 구분해 Cloud Firestore에 저장합니다.

- 서비스: https://pulse-note-b1-2.vercel.app/items
- 소스 코드: https://github.com/Logan-kim-the-philosopher/codyssey/tree/main/submissions/B1-2

## 주요 기능

- 기록 목록, 상세 조회, 새 기록 작성, 수정 및 삭제
- Google 로그인과 로그아웃, 인증이 필요한 프로필 경로 보호
- 폼 필수값 검증과 제출 중·오류·빈 목록 상태 표시
- 기록 제목과 내용을 검색하고 기록 카드에서 상세 화면으로 이동

## 기술 스택

- React 19.3, Vite 8.3
- React Router 7.18
- Firebase 12.19 (Authentication/Google 및 Cloud Firestore)
- 순수 CSS

## 로컬 실행

Node.js 20.19.0 이상 또는 22.12.0 이상과 npm이 필요합니다.

```bash
npm ci
cp .env.example .env
npm run dev
```

`.env`에 Firebase 웹 앱 설정의 값을 채워야 로그인과 Firestore 기능이 동작합니다.

```dotenv
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_STORAGE_BUCKET=
VITE_FIREBASE_MESSAGING_SENDER_ID=
VITE_FIREBASE_APP_ID=
```

Firebase Console에서 Google 로그인 제공업체와 Cloud Firestore를 활성화하세요. 배포 도메인에서 Google 로그인을 사용하려면 해당 도메인을 Firebase Authentication의 승인된 도메인에도 등록해야 합니다. Firestore 보안 규칙은 로그인한 사용자가 본인의 기록만 읽고 쓰도록 설정해야 합니다.

## 빌드

```bash
npm run build
npm run preview
```

`.env`는 저장소에 커밋하지 마세요. 환경변수는 로컬 `.env`와 Vercel 프로젝트 설정에서 별도로 관리합니다.
