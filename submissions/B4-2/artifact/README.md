# B4-2 시스템 장애 분석

제공 ARM64 Linux 바이너리를 수정·디컴파일하지 않고 일반 사용자로 실행한 실제 관측 자료입니다.

- [OOM 리포트](reports/01-oom.md)
- [CPU 리포트](reports/02-cpu.md)
- [Deadlock 리포트](reports/03-deadlock.md)
- [스케줄링 보너스](reports/04-scheduling.md)
- [운영 개선·회고](reports/05-operations.md)
- [측정 요약](evidence/summary.json)
- [CPU 추가 검증](evidence/cpu-burst-summary.json)

## 실행 환경과 재현

Docker Linux 6.12.76-linuxkit, aarch64, procps-ng 4.0.4.
Ubuntu 이미지: `ubuntu@sha256:3131b4cc82a783df6c9df078f86e01819a13594b865c2cad47bd1bca2b7063bb`.
컨테이너는 UID 1000, 메모리 상한 768MiB, CPU 상한 1코어, 네트워크 격리이며 호스트에 포트를 공개하지 않습니다. 로그 시간은 UTC이며 한국 시간은 +9시간입니다.

이 폴더에서 다음을 실행합니다. 기존 케이스 이름 대신 새 이름을 사용해 증거를 보존하세요.

```bash
docker run --rm --user 1000:1000 --memory 768m --cpus 1 --network none \
  -v "$PWD:/work" \
  ubuntu@sha256:3131b4cc82a783df6c9df078f86e01819a13594b865c2cad47bd1bca2b7063bb \
  bash /work/scripts/run-case.sh new-oom 50 100 false 30
```

`run-case.sh NAME MEMORY_LIMIT CPU_MAX_OCCUPY MULTI_THREAD_ENABLE SECONDS`.
실제 비교값: OOM 50→150 / CPU 100→10 / Deadlock true→false(메모리512, CPU30 고정).

`run-case.sh`는 실행 조건·부모/자식 PID·전체 실행 로그·CSV·스레드 스냅샷·top을 저장합니다. 관측 제한에 도달한 살아 있는 프로세스는 스크립트가 정리하며, 이를 `config.txt`에 명시합니다. 종료 코드 143만으로 Watchdog이라고 판단하지 않습니다.
`monitor.sh`는 제공 ZIP에 없어 직접 작성했습니다. 1초마다 ps의 RSS(KiB), %MEM, 누적 평균 %CPU, 경과시간, 스레드수, 상태를 CSV로 추출합니다. 부모 런처가 아니라 실제 자식 PID를 관측합니다.

## 증거 범위

`evidence/probe`와 `evidence/initial-runs`는 초기 측정·실패 기록이며 최종 판정에 사용하지 않습니다. `deadlock-before`는 CPU100이 교착 경로를 가리는 탐색 실행입니다. 교착 증거는 `deadlock-confirmed`와 `deadlock-after`입니다.

CPU 내부 로그 값과 OS 측정값은 구별합니다. 추가 고해상도 관제에서 실제 짧은 CPU 버스트83.33%를 확보했고 내부 보호 종료 및 저설정 대조군과 함께 검증했습니다. 자세한 원시 데이터와 측정 정밀도 한계는 CPU 리포트에 있습니다. 스크린샷 대신 원본 로그를 사용했습니다. GitHub Issue 게시·Git push·배포는 수행하지 않았습니다.
