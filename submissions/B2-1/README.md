# B2-1 나만의 용돈 기입장

- [서비스 체험](https://allowance-b2-1.vercel.app/)
- [발표자료](https://allowance-b2-1.vercel.app/presentation/index.html)
- [Python 소스코드](artifact/budget_app)

Python으로 수입·지출을 기록하고 월별 소비와 예산을 확인하는 콘솔 프로그램입니다.
JSONL 파일에 데이터를 저장하며, 기존 Python 기능을 브라우저에서 체험하는 웹 화면도 제공합니다.

## 주요 기능

| 기능 | 콘솔 프로그램 | 웹 체험 |
| --- | --- | --- |
| 거래 관리 | 추가·조회·검색·수정·삭제 | 추가·월별 조회·검색·삭제 |
| 월별 요약 | 수입·지출·잔액·카테고리별 지출 | 요약 카드와 카테고리별 지출 |
| 예산 | 월 예산 설정·조회·사용률·초과 안내 | 월 예산 설정·사용률 |
| 카테고리 | 추가·조회·삭제 및 사용 중 삭제 방지 | 기본 카테고리 선택 |
| CSV | 가져오기·기간별 내보내기 | 제공하지 않음 |
| 반복 거래·백업 | 반복 규칙 등록·월별 생성·파일 백업 | 현재 기록 JSON 다운로드 |

## 빠른 시작

### 웹에서 체험

[서비스 체험](https://allowance-b2-1.vercel.app/)에 접속해 거래를 입력하세요.
**입력 예시 → 기록 저장**으로 시작할 수 있습니다. Python 설치 없이 사용할 수 있습니다.

### 콘솔 실행

Python 3.10 이상이 필요하며 외부 패키지는 사용하지 않습니다.
저장소를 복제한 뒤 아래 명령을 실행하세요.

```bash
git clone https://github.com/Logan-kim-the-philosopher/codyssey.git
cd codyssey/submissions/B2-1/artifact
python3 -m budget_app --help
python3 -m budget_app add
python3 -m budget_app list --limit 5
python3 -m budget_app summary --month 2026-10
```

`add`는 날짜, 수입·지출 구분, 카테고리, 금액, 메모, 태그를 차례로 입력받습니다.
명령마다 실행하고 종료하며, 기본 데이터는 실행 폴더의 `data/`에 저장됩니다.
다른 폴더를 사용하려면 `--data-dir`을 지정하세요.

```bash
python3 -m budget_app category list
python3 -m budget_app budget set --month 2026-10 --amount 100000
python3 -m budget_app --data-dir ./my-data list
```

전체 명령과 CSV 형식은 [콘솔 사용 설명서](artifact/README.md)를 참고하세요.

### 웹 화면을 로컬에서 실행

저장소 루트에서 다음을 실행하고 `http://127.0.0.1:8872`에 접속하세요.

```bash
cd submissions/B2-1/web-demo
python3 prepare.py
python3 dev.py
```

배포 설정은 [web-demo/vercel.json](web-demo/vercel.json), 상세 안내는 [웹 사용 설명서](web-demo/README.md)에 있습니다.

## 폴더 구조

```text
B2-1/
├── README.md
├── artifact/                # 제출용 콘솔 프로그램
│   ├── README.md
│   └── budget_app/           # Python 소스 패키지
└── web-demo/                # 웹 체험 및 Vercel 배포
    ├── api/budget.py        # 기존 Python 기능을 호출하는 API
    ├── budget_app/          # 배포용 원본 패키지 복사본
    ├── public/              # 입력 화면과 발표자료
    ├── tests/test_api.py    # 웹 API 검증
    ├── prepare.py           # 배포용 소스·자료 준비
    └── dev.py               # 로컬 웹 서버
```

`artifact/budget_app`이 콘솔 소스 원본입니다. `web-demo/budget_app`은 Vercel이 단독으로
배포할 수 있도록 포함한 복사본이며 `prepare.py`가 원본에서 갱신합니다.

## 구현 구조

| 파일 | 역할 |
| --- | --- |
| `cli.py` | 명령 해석, 대화형 입력, 결과·오류 출력 |
| `models.py` | 거래·예산·반복 규칙 모델과 값 검증 |
| `service.py` | 거래 처리, 검색·요약, CSV, 예산·반복 규칙 |
| `storage.py` | JSONL 읽기·쓰기, 최신순 정렬, 원자적 파일 교체 |
| `decorators.py` | 작업 로그와 실행 시간 기록 |

콘솔은 거래·카테고리·예산·반복 규칙을 각각 별도 JSONL 파일로 저장합니다.
웹 API도 기존 서비스와 저장소를 호출하므로 계산과 입력 검증은 Python에서 수행합니다.

## 웹 데이터 저장 방식

웹 데이터는 **현재 브라우저의 localStorage**에 저장됩니다. 요청마다 데이터를 API에 전달하고,
API는 요청별 임시 폴더의 JSONL 파일로 처리한 뒤 결과를 반환합니다. 서버에는 요청 간 데이터가 남지 않습니다.

- 다른 브라우저나 기기와 기록이 공유되지 않습니다.
- 사이트 데이터를 삭제하면 기록도 사라집니다.
- **백업 다운로드**로 JSON을 보관할 수 있습니다. 웹 백업 복원 기능은 제공하지 않습니다.
- 웹은 주요 기능 체험용입니다. CSV·거래 수정·반복 거래 등은 콘솔에서 사용하세요.

## 검증

구현 시 독립 CLI 프로세스 기능 검사 **87개**, 파일 오류 처리 검사 **5개**를 통과했습니다.
콘솔 실행 검증은 Python 3.14 환경에서 수행했으며 Python 3.10 직접 실행은 확인하지 않았습니다.
Vercel 배포는 Python 3.12로 빌드되었습니다.

웹 API 테스트 **4개**는 거래·예산·삭제와 재조회, 잘못된 입력 시 원본 보존,
동시 요청 간 격리, 저장 금액 형식 검증을 다룹니다. 다음 명령으로 다시 실행할 수 있습니다.

```bash
cd submissions/B2-1/web-demo
python3 -m unittest discover -s tests -v
node --check public/app.js
```

Node.js 명령은 웹 JavaScript 문법 검사에만 사용합니다. 콘솔과 로컬 웹 실행에는 필요하지 않습니다.
배포된 서비스에서도 거래 추가·새로고침 후 기록 유지·삭제를 확인했습니다.

## 발표자료

[메인 발표자료](https://allowance-b2-1.vercel.app/presentation/index.html)는 평가 질문 16개를 다루며
코드보기에서 줄별 설명과 해당 코드 강조를 함께 제공합니다.

| 키 | 동작 |
| --- | --- |
| ← / → | 슬라이드 이동, 코드보기에서는 코드 탭 이동 |
| W | 코드보기 열기·닫기 |
| ↑ / ↓ | 코드 설명 또는 열린 목차 항목 선택 |
| E | 목차 열기·닫기 |
| Enter | 선택한 목차 페이지로 이동 |
| Q | 메인·별첨 전환 |

마지막 슬라이드에서 서비스 체험과 GitHub 소스코드로 바로 이동할 수 있습니다.
