# safe-mode 실제 전처리 비교

입력은 합성 fixture이고 비밀은 가짜다. API 호출 0회. 모델 결과 비교가 아니다.
정책: 10개 diff 블록, 200줄; 마스킹·제외 상세는 README 참조.

## ON
```diff
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1 +1,3 @@
-old=1
+token=[REDACTED SECRET]
+email="[REDACTED EMAIL]"
+value=2
```

## OFF
```diff
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1 +1,3 @@
-old=1
+token="FAKE_TEST_ONLY"
+email="fixture@example.invalid"
+value=2

```
