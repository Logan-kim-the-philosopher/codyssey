# 실제 게이트웨이 파라미터 비교

모델 gpt-5.4-mini, temperature 1, 동일한 합성 Git diff·why·test-plan, 각 1회 호출.

| CLI 출력 상한 | 생성 초안 글자 수 | 결과 |
| --- | ---: | --- |
| 3000 | 540 | 성공 |
| 800 | 548 | 성공 |

요청 상한은 게이트웨이에 max_tokens로 전달했다. 글자 수는 변경 요약·제목·본문 구간이며 토큰 수가 아니다. 두 실행의 표현·길이가 달랐다. 확률적 생성이므로 이 1회 비교만으로 차이가 전부 출력 상한 때문이라고 단정하지 않는다.

## 3000
```text
--- Change Summary ---
README와 subtotal 로직에 입력 검증을 추가해 음수 가격과 0 이하 수량을 거부하도록 변경했습니다. 합계 계산의 잘못된 결과를 막기 위한 조치로 보입니다.

--- PR Title ---
fix: subtotal 입력 검증 추가

--- PR Body ---
## Why
- 음수 가격과 0 이하 수량으로 잘못된 합계가 생성되는 것을 방지합니다.
- 문서에 허용되지 않는 입력 조건을 명시해 사용자가 동작을 쉽게 이해하도록 합니다.

## What
- calculator.py의 subtotal에 price < 0 및 quantity <= 0 검사를 추가하고 각각 ValueError를 발생시킵니다.
- README.md에 음수 가격과 비양수 수량에서 ValueError가 발생한다는 설명을 추가했습니다.

## How to Test
- subtotal(10, 2)가 20을 반환하는지 확인합니다.
- subtotal(-1, 2)와 subtotal(10, 0)이 각각 ValueError를 발생시키는지 확인합니다.
```

## 800
```text
--- Change Summary ---
음수 가격과 0 이하 수량 입력을 거부하도록 subtotal 검증을 추가하고, README에 동작을 문서화했습니다.

--- PR Title ---
fix: subtotal 입력 검증 추가

--- PR Body ---
## Why
- 음수 가격과 0 이하 수량으로 잘못된 합계가 생성되는 것을 방지하기 위함입니다.
- README와 구현의 동작을 맞춰 사용자가 유효 입력 조건을 알 수 있도록 하기 위한 것으로 보입니다.

## What
- calculator.py의 subtotal에 price < 0이면 ValueError, quantity <= 0이면 ValueError를 발생시키는 검증을 추가했습니다.
- README.md에 음수 가격과 nonpositive 수량은 ValueError가 발생한다고 설명을 보강했습니다.

## How to Test
- subtotal(10, 2)가 20을 반환하는지 확인합니다.
- subtotal(-1, 2)와 subtotal(10, 0)이 각각 ValueError를 발생시키는지 확인합니다.
```
