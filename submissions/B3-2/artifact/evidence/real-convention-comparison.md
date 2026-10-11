# 실제 AI 컨벤션 전후 비교

모델 gpt-5.4-mini, temperature 1, max_tokens 3000. 동일 합성 diff와 변경 배경을 사용하고 컨벤션만 변경했다. 각 1회 실제 호출. 이전 B3-1 저장소의 실제 PR에 적용한 증빙은 아니다.

## 기본 컨벤션
```text
--- Change Summary ---
음수 가격과 0 이하 수량을 검증해 `ValueError`를 발생시키도록 계산 로직과 문서를 갱신했습니다.

--- Commit Message ---
fix: 입력값 검증 추가

- `subtotal`에서 price가 음수이면 `ValueError`를 발생시키고, quantity가 0 이하이면 `ValueError`를 발생시키도록 추가했습니다.
- README에 음수 가격과 0 이하 수량이 허용되지 않는 동작을 문서화했습니다.
```

## B3-1 컨벤션
```text
--- Change Summary ---
README에 검증 규칙을 문서화하고 calculator.py에서 음수 가격과 0 이하 수량을 ValueError로 거부하도록 추가함. 이 변경은 음수 가격과 0 이하 수량을 거부하려는 의도로 해석된다.

--- Commit Message ---
docs(b3-1): 입력 검증 규칙 문서화

- README에 음수 가격과 0 이하 수량이 ValueError를 발생시킨다는 설명을 추가했다.
- subtotal()에서 price < 0, quantity <= 0인 경우 각각 ValueError를 발생시키도록 입력 검증을 넣었다.
```

컨벤션 적용 후 b3-1 scope가 제목에 반영됐다. 세부 표현 차이는 확률적 생성의 영향도 있을 수 있다.
