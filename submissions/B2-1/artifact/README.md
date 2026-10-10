# 나만의 용돈 기입장

Python 3.10 이상과 표준 라이브러리만 사용하는 파일 기반 콘솔 가계부입니다.

## 실행

산출물 폴더(`artifacts/b2-1/artifact`)에서 실행합니다.

```bash
python -m budget_app --help
python -m budget_app add
```

기본 데이터 폴더는 실행 위치의 `./data`입니다. 폴더를 바꾸려면 전역 옵션을 명령 앞이나 뒤에 둡니다.

```bash
python -m budget_app --data-dir ./my-data list --limit 10
python -m budget_app list --limit 10 --data-dir ./my-data
```

모든 명령과 하위 명령은 `--help`를 지원합니다. 거래 수정은 옵션 방식으로 고정했습니다.

## 저장 파일

데이터는 UTF-8 JSONL로 저장하며, 한 줄마다 JSON 객체 하나를 씁니다.

| 파일 | 내용 |
| --- | --- |
| `transactions.jsonl` | 날짜 내림차순 거래 내역 |
| `categories.jsonl` | 등록 카테고리 |
| `budgets.jsonl` | 월별 예산 |
| `recurring.jsonl` | 반복 거래 규칙 |
| `budget.log` | 거래 추가 및 CSV 입출력 작업 시 기록되는 로그와 처리 시간 |

최초 실행 시 저장 파일과 기본 카테고리가 만들어집니다. 로그 파일은 데코레이터가 적용된 작업을 실행하면 생성됩니다. 수정·삭제·예산 갱신은 임시 파일을 작성한 뒤 원자적으로 교체합니다. 거래 조회는 JSONL을 한 줄씩 읽는 제너레이터를 사용합니다.

## 명령 예시

```bash
python -m budget_app category list
python -m budget_app category add --name hobby
python -m budget_app add
python -m budget_app list --limit 5
python -m budget_app search --from 2026-09-01 --to 2026-09-30 --type expense --tag meal
python -m budget_app summary --month 2026-09 --top 3
python -m budget_app budget set --month 2026-09 --amount 500000
python -m budget_app budget show --month 2026-09
python -m budget_app update --id TX-0123456789AB --amount 18000 --memo "저녁"
python -m budget_app delete --id TX-0123456789AB
python -m budget_app export --out ./export.csv --month 2026-09
python -m budget_app import --from ./import.csv
python -m budget_app backup
python -m budget_app recurring add --type expense --day 25 --amount 700000 --category rent --memo "월세"
python -m budget_app recurring generate --month 2026-09
```

`add`는 날짜, 타입, 카테고리, 금액, 메모, 태그를 순서대로 대화형 입력합니다. `update`에서 지정한 필드만 바꿉니다. 메모를 지우려면 `--memo ""`를 지정하세요. 태그는 쉼표로 구분합니다.

검색 결과는 날짜와 생성 시각의 최신순으로 표시됩니다. 반복 생성은 같은 규칙과 월 조합에 대해 한 번만 거래를 만듭니다. 예산 사용률은 해당 월 지출을 예산으로 나누어 계산합니다.

## CSV 가져오기·내보내기 스키마

가져오기는 UTF-8 CSV 헤더를 읽습니다. `date`, `type`, `category`, `amount`는 필수이며 `memo`, `tags`는 선택입니다. `tags`는 쉼표로 구분합니다. 날짜는 `YYYY-MM-DD`, 타입은 `income` 또는 `expense`, 금액은 양수 정수, 카테고리는 등록된 값이어야 합니다. 잘못된 행은 건너뛰고 가져온 수와 건너뛴 수를 출력합니다.

| column | required | 설명 |
| --- | --- | --- |
| `date` | Y | `YYYY-MM-DD` |
| `type` | Y | `income` 또는 `expense` |
| `category` | Y | 등록된 카테고리 |
| `amount` | Y | 양수 정수 |
| `memo` | N | 문자열 |
| `tags` | N | 쉼표(,) 구분 문자열 |

내보내기는 `--month YYYY-MM` 또는 `--from YYYY-MM-DD --to YYYY-MM-DD` 조건 중 하나를 요구하며, 같은 CSV 스키마로 저장합니다.

## 구조와 학습 포인트

- `models.py`: 타입 힌트가 있는 dataclass와 거래·예산·반복 규칙 검증
- `storage.py`: JSONL 스트리밍, 세 파일 이상 분리 저장, 임시 파일과 원자적 교체
- `service.py`: CRUD, 필터, 월 요약, CSV, 예산 및 반복 규칙 처리
- `cli.py`: argparse 명령, 대화형 입력, 테이블 출력과 오류 안내
- `decorators.py`: 작업 로그와 실행 시간 측정 데코레이터

조회 함수는 `yield`로 한 행씩 전달하므로 거래 파일 전체를 목록으로 만들지 않습니다. 수정·삭제는 데이터 정렬을 다시 맞춰 임시 파일로 기록한 뒤 교체합니다. 서비스 계층은 거래 규칙을 처리하고 저장소 계층은 JSONL 파일 접근을 맡습니다. 데코레이터는 서비스 동작의 로그와 시간을 CLI 처리 흐름에서 분리합니다.
