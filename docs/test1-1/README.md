# 홍길동 포트폴리오

순수 HTML, CSS, JavaScript로 만든 반응형 자기소개 웹페이지입니다. 사용자 이벤트가 상태를 바꾸고, 그 상태가 DOM 렌더링으로 이어지는 흐름을 한 화면에서 확인할 수 있습니다.

## 구성

- `index.html`: 시맨틱 페이지 구조
- `css/style.css`: CSS 변수, 반응형 레이아웃, 다크 테마
- `js/main.js`: DOM 이벤트, 상태 관리, GitHub API 연동
- `images/profile.svg`: 프로필 이미지

## 기능

- 모바일 햄버거 메뉴와 부드러운 앵커 스크롤
- 60px 스크롤 네비게이션 변화, 300px 상단 이동 버튼
- Intersection Observer 스크롤 애니메이션 (`threshold: 0.2`)
- 다크 모드와 `localStorage` 유지
- GitHub 저장소 로딩, 성공, 에러, 빈 상태
- 저장소 이름 검색 및 언어별 필터링
- 문의 폼 필수값/이메일 검증 및 Formspree 전송
- Hero 타이핑 효과와 시스템 다크 모드 감지

## 이벤트 -> 상태 -> 렌더링

1. 다크 모드 버튼 클릭 -> `data-theme`와 `localStorage` 변경 -> 전체 색상 토큰 변경
2. GitHub API 요청 -> loading/success/error/empty 상태 변경 -> Projects DOM 갱신
3. 폼 입력/제출 -> 유효성 상태 변경 -> 필드 근처 오류 또는 성공 메시지 갱신
4. 언어 필터 변경 -> 필터 상태 변경 -> `filter()` 결과 카드 갱신

## 실행

VS Code에서 Live Server로 `index.html`을 실행하세요. 외부 라이브러리나 프레임워크는 사용하지 않았습니다.

## 링크

- GitHub 저장소: https://github.com/Logan-kim-the-philosopher/codyssey
- GitHub Pages: https://logan-kim-the-philosopher.github.io/codyssey/test1-1/

## 제출 스크린샷

스크린샷은 `evidence/` 폴더에 데스크톱, 모바일, 다크 모드 상태로 추가할 수 있습니다.
