# [Bug] CPU Latency - 짧은 CPU 버스트와 내부 보호 정책에 따른 SIGTERM 종료

## 1. Description (현상 설명)
제공 ARM64 바이너리를 Linux 컨테이너의 일반 사용자 UID1000으로 실행했다. MEMORY_LIMIT512, MULTI_THREAD_ENABLE=false를 고정하고 CPU_MAX_OCCUPY100과10을 비교했다. 대상은 런처의 자식 PID12이며 각 컨테이너의 PID 네임스페이스는 독립적이다.
100 설정은 내부 부하값57.08%에서 CPU Threshold Violated를 기록하고 자연 종료했다. 10 설정은 45초 관측 기간 동안 생존했다. 고해상도 관제에서는 실제 CPU 사용률이 0%에 가까운 구간에서 83.33%까지 짧게 급상승했다.

## 2. Evidence & Logs (증거 자료)
- [고설정 실행 로그](../evidence/cpu-arm64-burst/application.log) · [설정·종료 원인](../evidence/cpu-arm64-burst/config.txt) · [PID 트리](../evidence/cpu-arm64-burst/process-tree-start.log)
- [고설정 원시 CPU 시간](../evidence/cpu-arm64-burst/cpu-interval.csv) · [top](../evidence/cpu-arm64-burst/top.log)
- [저설정 실행 로그](../evidence/cpu-arm64-burst-low/application.log) · [설정·정리 기록](../evidence/cpu-arm64-burst-low/config.txt) · [원시 CPU 시간](../evidence/cpu-arm64-burst-low/cpu-interval.csv)
- [재계산 검증 결과](../evidence/cpu-burst-summary.json)

```text
2026-10-11T15:43:21Z uptime=982.90->982.96 ticks+0 CPU=0.0%
2026-10-11T15:43:21Z uptime=982.96->983.01 ticks+0 CPU=0.0%
2026-10-11T15:43:21Z uptime=983.01->983.07 ticks+5 CPU=83.33%
```

최고 표본은 실제 경과 0.06초 동안 CPU 시간 5/100초가 증가한 결과다. CPU% = 100 × Δ(utime+stime) / CLK_TCK / Δ실제시간으로 계산했다. CLK_TCK=100이며 대상 PID의 `/proc/PID/stat`과 `/proc/uptime`을 직접 읽었다. 표본 간 sleep 목표는0.05초이고 명령 실행 시간이 더해져 실제 구간은 약0.06초이다. CPU%는 1코어 대비 비율이며 시스템 전체 사용률이나 cgroup 한도 대비 비율이 아니다.

```text
2026-10-11 15:43:14,997 [INFO] [CpuWorker] Current Load: 40.84%
2026-10-11 15:43:18,106 [INFO] [CpuWorker] Current Load: 49.84%
2026-10-11 15:43:21,223 [INFO] [CpuWorker] Current Load: 57.08%
2026-10-11 15:43:21,325 [CRITICAL] [CpuWorker] CPU Threshold Violated! (57.08%).
```

|CPU_MAX_OCCUPY|실제 짧은 구간 CPU 최고|내부 종료/부하 로그|관측 결과|
|---|---:|---|---|
|100|83.33%|57.08%에서 Threshold Violated|약34초 후 자연 종료143|
|10|20.0%|5~10% cooldown 반복|45초 생존; 관측 종료 후 스크립트 정리|

관측 시간은 초기화 이후 스크립트의 감지·정리까지 포함한다. 정확한 앱 사건 시점은 로그 타임스탬프를 사용한다. 고설정은 관측 종료 표식 없이 종료했고 저설정은 표식과 SIGTERM 정리 기록이 있어 두 종료143의 의미를 구별한다.

## 3. Root Cause Analysis (원인 분석)
1초 top의 낮은 수치는 짧은 CPU 버스트를 평균화한다. ps %CPU도 전체 수명 동안의 평균이므로 짧은 상승을 희석한다. 0.2초 관제의 ARM64 최고는23.81%, 같은 방식 x86 에뮬레이션은14.29%였다. 더 짧은 0.05초 ARM64 관제는 실제 버스트를 확보했다. 따라서 초기의 낮은 top 값만으로 실제 상승이 없다고 결론 낼 수 없다.
다만 내부 Current Load 값은 실제 순간 CPU 값과 같지 않다. 보호 종료는 내부 값이50을 넘었을 때 관측되었고, CPU_MAX_OCCUPY100에 도달해서 종료한 것이 아니다. 실제 버스트 83.33%와 내부57.08%는 별도 근거다. 바이너리 분석 없이 내부 계산식이나 OS 측정값을 직접 사용했는지 확정하지 않는다. 실제 WATCHDOG 문구 대신 제공 버전의 `CPU Threshold Violated` 메시지와 자연 SIGTERM 계열 종료143을 제시한다.
CPU를 많이 사용하는 작업이 runnable 상태로 CPU 기회를 소모하면 다른 요청의 대기 시간이 늘 수 있다. 문제 프로세스 종료는 전체 서비스 여유를 확보하는 보호 조치가 될 수 있다. 이번 자료는 짧은 버스트를 입증하며 지속적인50% 이상 점유나 실제 사용자 응답 지연을 측정한 자료는 아니다.

## 4. Workaround & Verification (조치 및 검증)
CPU_MAX_OCCUPY100→10 변경 후 동일 고해상도 관제에서 최고 구간 값은 83.33→20.0%였으며 45초 관측 내 보호 종료가 없었다. 메모리 누수는 저설정에서 별도로 진행하므로 장기 안정성이나 모든 워크로드의 동등성을 주장하지 않는다.
근본 조치 제안은 busy loop 제거, 이벤트 대기, 작업량·동시성 제한과 실제 CPU 시간 기반 측정이다. 연속 초과 판단을 사용해 짧은 정상 버스트와 지속 과점유를 구별한다.

재현: `CPU_SAMPLE_INTERVAL=0.05`를 컨테이너에 전달하고 `run-cpu-case.sh NAME 512 100 false 60` 또는 `NAME 512 10 false 45`를 실행한다. `verify-cpu-burst.py`가 원시 틱으로 모든 사용률을 재계산하고 상승·보호 종료·대조군 생존을 확인한다.

정밀도 한계:100Hz CPU 틱과 0.01초 uptime 분해능 때문에 약0.06초 구간 값은 거칠게 양자화된다. 83.33은 원시 기록으로 계산한 표본값이며 정밀한 순간 사용률을 뜻하지 않는다. 장기 평균과 짧은 구간 표본을 섞지 않는다.

도구 기준: [Linux proc_pid_stat 매뉴얼](https://man7.org/linux/man-pages/man5/proc_pid_stat.5.html), [ps 매뉴얼](https://man7.org/linux/man-pages/man1/ps.1.html).
