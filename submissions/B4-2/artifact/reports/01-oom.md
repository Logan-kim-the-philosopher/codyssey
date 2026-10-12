# [Bug] OOM Crash - MemoryGuard의 힙 한도 도달에 따른 자체 종료

## 1. Description (현상 설명)
Linux 일반 사용자(UID1000)로 제공 앱을 실행했다. MEMORY_LIMIT=50에서 PID 13는 약 6초 후 종료했고, 150으로 변경한 PID 59는 약 18초 후 종료했다. CPU100, MULTI_THREAD_ENABLE=false는 동일하다. 시간은 실행 초기화 1초 이후부터 측정한 관측·정리 시간이며 로그 기반 한도 도달 간격도 함께 확인한다.

## 2. Evidence & Logs (증거 자료)
- [oom-before 설정](../evidence/oom-before/config.txt) · [실행 로그](../evidence/oom-before/application.log) · [관제 CSV](../evidence/oom-before/monitor.csv) · [ps 스레드](../evidence/oom-before/process-threads.log)
- [oom-after 설정](../evidence/oom-after/config.txt) · [실행 로그](../evidence/oom-after/application.log) · [관제 CSV](../evidence/oom-after/monitor.csv) · [ps 스레드](../evidence/oom-after/process-threads.log)

```text
2026-10-11 15:29:53,789 [INFO] [MemoryWorker] Current Heap: 25MB
2026-10-11 15:29:56,811 [INFO] [MemoryWorker] Current Heap: 50MB
2026-10-11 15:29:56,812 [CRITICAL] [MemoryGuard] Memory limit exceeded (50MB >= 50MB) / (Recommend Over 256MB)
2026-10-11 15:29:56,812 [CRITICAL] [MemoryGuard] Self-terminating process 13 to prevent system instability.
2026-10-11 15:30:00,839 [INFO] [MemoryWorker] Current Heap: 25MB
2026-10-11 15:30:03,860 [INFO] [MemoryWorker] Current Heap: 50MB
2026-10-11 15:30:06,884 [INFO] [MemoryWorker] Current Heap: 75MB
2026-10-11 15:30:09,908 [INFO] [MemoryWorker] Current Heap: 100MB
2026-10-11 15:30:12,930 [INFO] [MemoryWorker] Current Heap: 125MB
2026-10-11 15:30:15,954 [INFO] [MemoryWorker] Current Heap: 150MB
2026-10-11 15:30:15,954 [CRITICAL] [MemoryGuard] Memory limit exceeded (150MB >= 150MB) / (Recommend Over 256MB)
2026-10-11 15:30:15,954 [CRITICAL] [MemoryGuard] Self-terminating process 59 to prevent system instability.
```

|설정|관측 시간|RSS 최소→최대 KiB|종료 코드|
|---|---:|---:|---:|
|50MB|6초|18268→43872|137|
|150MB|18초|18396→146416|137|

약 3초마다 앱 힙이 25MB씩 증가한다. RSS도 대응하는 계단 형태로 증가하며 평균 추세가 선형이다. 최고 RSS 표본은 종료 직전 마지막 할당을 놓칠 수 있어 내부 한도 숫자와 같다고 주장하지 않는다.

## 3. Root Cause Analysis (원인 분석)
힙에 데이터를 계속 유지하는 누수/무제한 누적이 관측된다는 추론이다. 바이너리를 분석하지 않았으므로 구체적인 객체·소스 위치는 알 수 없다. 힙은 동적 데이터, 스택은 호출 프레임, 코드 영역은 명령어를 보관한다. 누수로 RSS가 증가하면 다른 프로세스의 메모리 여유를 줄이고 reclaim·swap·OOM 위험을 높일 수 있다.
MemoryGuard는 내부 힙 값이 설정 한도에 도달한 뒤 해당 PID를 자체 종료했다. 종료 코드137은 SIGKILL 계열 결과와 일치하나 이것만으로 커널 OOM Killer라고 할 수 없다. 직접 찍힌 MemoryGuard 로그가 앱 보호 종료의 근거다. SELF-TERMINATED 문구는 이번 바이너리에서 출력되지 않았고 대체 핵심 메시지를 원문 그대로 제시한다.

## 4. Workaround & Verification (조치 및 검증)
MEMORY_LIMIT 50→150으로 변경해 생존 관측 시간이 약 6→18초로 증가했다. 한도 증가는 누수를 해결하지 않으며 결국 재종료했다. 실제 가용 메모리를 새로 만드는 조치가 아니다. 소스 접근이 허용된다면 불필요한 참조 해제, 캐시/큐 크기 제한, 수명 추적 및 장시간 메모리 회귀 검사를 제안한다.

측정 방법: `ps -p PID -o rss=,%mem=,...`에서 RSS는 KiB이며 %MEM은 노출된 시스템 메모리 대비 비율이다. 컨테이너 768MiB 한도 대비 비율과 구별한다. [ps 공식 매뉴얼](https://man7.org/linux/man-pages/man1/ps.1.html).
