# B2-1 웹 체험

기존 Python BudgetService와 JsonlBudgetStore를 그대로 사용하는 발표용 화면입니다.
거래 추가·삭제·조회, 월 요약, 월 예산 설정을 지원합니다. 거래 검색은 현재 월의 화면 목록을 필터링합니다.

## 로컬 실행

```bash
cd /Users/hskim/Projects/codyssey/artifacts/b2-1/web-demo
python3 prepare.py
python3 dev.py
```

http://127.0.0.1:8872 접속. 외부 Python 패키지가 필요하지 않습니다.

## 저장 방식

브라우저 localStorage에 거래와 예산을 저장하고 요청마다 Python API에 전달합니다.
API는 요청별 임시 폴더의 JSONL 파일을 통해 기존 서비스로 처리한 후 결과를 반환합니다.
요청 간 서버 데이터는 보관하지 않으며, 브라우저/기기가 다르면 서로 다른 기록입니다.
사이트 데이터 삭제 시 기록도 사라지므로 백업 다운로드로 JSON을 보관할 수 있습니다.
이 UI는 콘솔의 전체 명령을 대체하지 않습니다. CSV·반복 거래·수정 등은 콘솔에서 사용합니다.

## Vercel 배포

```bash
npx --yes vercel login
npx --yes vercel --prod --yes
```

이 디렉터리를 프로젝트 루트로 사용합니다. public에 화면과 발표자료가 있으며 /api/budget은 Python 함수입니다.
prepare.py는 로컬 원본이 있으면 배포용 복사본을 갱신하고, 독립 배포 환경에서는 기존 복사본을 사용합니다.
원본 budget_app은 수정하지 않았으며 복사본과 일치합니다.

## 검증

```bash
python3 -m unittest discover -s tests -v
node --check public/app.js
```

API 테스트는 거래 재조회·월 요약·예산·삭제, 잘못된 입력과 원본 데이터 보존,
동시 요청 간 격리, 저장 금액 형식 검증을 포함합니다.

배포 주소: https://allowance-b2-1.vercel.app
발표자료: https://allowance-b2-1.vercel.app/presentation/index.html
