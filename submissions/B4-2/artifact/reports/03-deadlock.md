# [Bug] Deadlock - 두 워커의 반대 순서 자원 획득으로 무응답

## 1. Description (현상 설명)
MEMORY_LIMIT512, CPU_MAX_OCCUPY30을 고정하고 MULTI_THREAD_ENABLE=true로 실행했다. PID 12는 살아 있으나 두 워커의 WAITING/BLOCKED 이후 로그가 멈췄다. 같은 조건에서 false 실행은 작업 진행 로그가 계속됐다. 각각 25초와 25초의 유한 관측이다.

## 2. Evidence & Logs (증거 자료)
- [deadlock-confirmed 설정](../evidence/deadlock-confirmed/config.txt) · [실행 로그](../evidence/deadlock-confirmed/application.log) · [관제 CSV](../evidence/deadlock-confirmed/monitor.csv) · [ps 스레드](../evidence/deadlock-confirmed/process-threads.log)
- [deadlock-after 설정](../evidence/deadlock-after/config.txt) · [실행 로그](../evidence/deadlock-after/application.log) · [관제 CSV](../evidence/deadlock-after/monitor.csv) · [ps 스레드](../evidence/deadlock-after/process-threads.log)

```text
2026-10-11 15:32:42,481 [INFO] [AgentWorker] Waiting for worker threads to complete transactions...
2026-10-11 15:32:42,481 [INFO] [AgentWorker][Worker-Thread-1] LOCK ACQUIRED: [Shared_Memory_A]. (Holding...)
2026-10-11 15:32:42,481 [INFO] [AgentWorker][Worker-Thread-2] LOCK ACQUIRED: [Socket_Pool_B]. (Holding...)
2026-10-11 15:32:44,493 [INFO] [AgentWorker][Worker-Thread-2] Need resource [Shared_Memory_A] to write logs.
2026-10-11 15:32:44,493 [INFO] [AgentWorker][Worker-Thread-2] WAITING for [Shared_Memory_A]... (Status: BLOCKED)
2026-10-11 15:32:44,495 [INFO] [AgentWorker][Worker-Thread-1] Need resource [Socket_Pool_B] to finish job.
2026-10-11 15:32:44,495 [INFO] [AgentWorker][Worker-Thread-1] WAITING for [Socket_Pool_B]... (Status: BLOCKED)
```

`ps -ef` 시작 자료와 반복 `ps -p`는 PID 존재를, `ps -L`은 3개 스레드와 futex_wait_queue 대기를 보여준다. 마지막 안정 RSS는 21428KiB이고 로그가 중단된 뒤에도 관측 표본은 계속된다. %CPU 누적 평균은 감소할 수 있어 그 숫자가 정확히 같아야 정지라고 판정하지 않는다. [관제 원본](../evidence/deadlock-confirmed/monitor.csv).

## 3. Root Cause Analysis (원인 분석)
Worker1은 A(Shared_Memory_A)를 보유하고 B(Socket_Pool_B)를 기다린다. Worker2는 B를 보유하고 A를 기다린다. 따라서 W1→W2→W1 순환 대기가 생긴다. 상호 배제, 점유 대기, 자원 비선점, 순환 대기가 로그와 일치한다. 주 스레드도 워커 완료를 기다린다.
futex 대기만으로는 정상 동기화와 교착을 구별할 수 없다. PID 유지→스레드 상태→자원 점유 및 요청 로그→진행 정지→설정 대조군 순서로 증거를 결합한다. 스레드 이름과 OS TID의 개별 대응은 로그에 없으므로 특정 TID가 W1이라고 단정하지 않는다.

## 4. Workaround & Verification (조치 및 검증)
MULTI_THREAD_ENABLE true→false만 변경했다. false에서는 Scheduler All tasks completed와 MemoryWorker/CpuWorker 진행 로그가 지속되며 동일 기간의 BLOCKED가 없다. 영구 무결함을 뜻하지 않으며 다른 메모리 문제는 계속 존재한다. 두 실행은 관측 제한 종료 후 스크립트가 정리했다.
근본 조치: 모든 경로에서 A→B처럼 락 순서 통일, 락 보유 중 I/O 최소화, timeout/취소·실패 복구, 경쟁 경로 회귀 테스트를 제안한다. 멀티스레드 비활성화는 임시 회피이며 처리량 손실을 평가해야 한다.
