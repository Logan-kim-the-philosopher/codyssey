# [Analysis] 로그 패턴 분석을 통한 스케줄링 알고리즘 추론

## 1. 로그 관찰 개요
MULTI_THREAD_ENABLE=false 정상 진행 구간의 워커 로그를 사용했다. [원본](../evidence/deadlock-after/application.log), [OS 정책](../evidence/deadlock-after/scheduling-policy.log).

## 2. 증거 자료
```text
2026-10-11 15:32:41,013 [INFO] [Scheduler] Task Scheduler Initialized.
2026-10-11 15:32:41,014 [INFO] [Scheduler] Registered Tasks: ['Thread-A', 'Thread-B', 'Thread-C']
2026-10-11 15:32:41,014 [INFO] [Scheduler] Starting task execution...
2026-10-11 15:32:41,014 [INFO] [Thread-A] Task Started. Calculating... (20%)
2026-10-11 15:32:41,066 [INFO] [Thread-A] Calculating... (40%)
2026-10-11 15:32:41,121 [INFO] [Thread-A] Preempted. Progress saved at (40%)
2026-10-11 15:32:41,176 [INFO] [Thread-B] Task Started. Calculating... (20%)
2026-10-11 15:32:41,230 [INFO] [Thread-B] Calculating... (40%)
2026-10-11 15:32:41,281 [INFO] [Thread-B] Preempted. Progress saved at (40%)
2026-10-11 15:32:41,333 [INFO] [Thread-C] Task Started. Calculating... (20%)
2026-10-11 15:32:41,385 [INFO] [Thread-C] Calculating... (40%)
2026-10-11 15:32:41,436 [INFO] [Thread-C] Preempted. Progress saved at (40%)
2026-10-11 15:32:41,487 [INFO] [Thread-A] Resumed. Calculating... (60%)
2026-10-11 15:32:41,542 [INFO] [Thread-A] Calculating... (80%)
2026-10-11 15:32:41,597 [INFO] [Thread-A] Preempted. Progress saved at (80%)
2026-10-11 15:32:41,653 [INFO] [Thread-B] Resumed. Calculating... (60%)
2026-10-11 15:32:41,707 [INFO] [Thread-B] Calculating... (80%)
2026-10-11 15:32:41,763 [INFO] [Thread-B] Preempted. Progress saved at (80%)
2026-10-11 15:32:41,817 [INFO] [Thread-C] Resumed. Calculating... (60%)
2026-10-11 15:32:41,873 [INFO] [Thread-C] Calculating... (80%)
2026-10-11 15:32:41,926 [INFO] [Thread-C] Preempted. Progress saved at (80%)
2026-10-11 15:32:41,977 [INFO] [Thread-A] Resumed. Calculating... (100%)
2026-10-11 15:32:42,033 [INFO] [Thread-B] Resumed. Calculating... (100%)
2026-10-11 15:32:42,085 [INFO] [Thread-C] Resumed. Calculating... (100%)
2026-10-11 15:32:42,136 [INFO] [Scheduler] All tasks completed.
```

## 3. 패턴 분석 및 결론
A→B→C가 각각 진행률40%에서 Preempted된 뒤 같은 순서로60~80%, 마지막100%까지 재개한다. 시작 순서대로 한 작업을 끝내는 FCFS와 다르고 특정 작업의 우선 독점도 관측되지 않는다. 후보 중 **애플리케이션 로그상의 작업 교대 모델은 Round-Robin이 가장 부합**한다. 약50ms 간격의 로그와 세 메시지 묶음은 작업 로그 패턴이지 커널의 정확한 시간 할당량 측정은 아니다.
OS ps 정책은 TS(일반 시분할), nice10이다. Linux SCHED_RR 실시간 정책이 설정됐다는 결론은 지지하지 않는다. [Linux sched 공식 매뉴얼](https://man7.org/linux/man-pages/man7/sched.7.html).

## 4. 장단점 및 적합한 서비스
RR 모델은 작업 간 기회를 나누어 짧은 요청의 기다림을 줄일 수 있다. 교체 비용과 시간 할당량 선택에 민감하며 긴 작업의 전체 완료 시간이 늘어날 수 있다. 상호작용 웹 요청에 공정한 응답을 제공하려는 구조에 적합하고, 교체 비용을 최소화할 배치에서는 FCFS형 순차 처리가 적합할 수 있다. 엄격한 실시간 보장은 로그 교대만으로 얻지 못하며 우선순위·데드라인 설계가 별도로 필요하다.
