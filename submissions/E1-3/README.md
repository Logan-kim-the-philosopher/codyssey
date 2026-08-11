# E1-3 작은 계산기 만들기

- 발표 링크: 발표용 HTML 링크 준비 중

## 챕터

- Chapter 1. 1. 개발 환경과 data.json 확인
- Chapter 2. 2. 2차원 배열과 MAC 핵심 연산
- Chapter 3. 3. data.json 키 규칙과 epsilon 기반 판정
- Chapter 4. 4. MAC 평균 시간과 O(N^2) 성능 분석
- Chapter 5. 5. 3x3 사용자 입력 검증과 최종 판정

## 실습 로그

## Chapter 1. 1. 개발 환경과 data.json 확인

### 테마

- 작업 폴더와 입력 데이터 위치 확인
- Python 버전과 과제 workDir 확인
- 첨부 data.json 배치와 JSON 최상위 키 확인
- main.py와 README.md 초기 파일 생성

### 작업 폴더와 입력 데이터 위치 확인

```bash
$ pwd
/Users/hskim/Projects/codyssey/artifacts/e1-3/work
```

### 작업 폴더와 입력 데이터 위치 확인

```bash
$ ls -la
total 48
drwxr-xr-x@ 3 hskim  staff     96 Aug  8 15:46 .
drwxr-xr-x@ 9 hskim  staff    288 Aug  8 15:48 ..
-rw-r--r--@ 1 hskim  staff  20738 Aug  8 15:46 data.json
```

### 작업 폴더와 입력 데이터 위치 확인

```bash
$ head -n 20 data.json
{
    "meta": {
        "version": "1.0",
        "type": "json"
    },
    "filters": {
        "size_5": {
            "cross": [
                [0.0, 0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0, 0.0],
                [1.0, 1.0, 0.9, 1.0, 1.0],
                [0.0, 0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0, 0.0]
            ],
            "x": [
                [0.1, 0.0, 0.0, 0.0, 0.1],
                [0.0, 0.1, 0.0, 0.1, 0.0],
                [0.0, 0.0, 0.1, 0.0, 0.0],
                [0.0, 0.1, 0.0, 0.1, 0.0],
                [0.1, 0.0, 0.0, 0.0, 0.1]
```

### Python 버전과 과제 workDir 확인

```bash
$ python3 --version
Python 3.14.6
```

### 첨부 data.json 배치와 JSON 최상위 키 확인

```bash
$ python3 -c "import json; print(list(json.load(open('data.json')).keys()))"
['meta', 'filters', 'patterns']
```

### main.py와 README.md 초기 파일 생성

```bash
$ touch main.py README.md
```

### main.py와 README.md 초기 파일 생성

```bash
$ ls -la
total 48
drwxr-xr-x@ 5 hskim  staff    160 Aug 10 13:05 .
drwxr-xr-x@ 9 hskim  staff    288 Aug  8 15:48 ..
-rw-r--r--@ 1 hskim  staff      0 Aug 10 13:05 README.md
-rw-r--r--@ 1 hskim  staff  20738 Aug  8 15:46 data.json
-rw-r--r--@ 1 hskim  staff      0 Aug 10 13:05 main.py
```


## Chapter 2. 2. 2차원 배열과 MAC 핵심 연산

### 테마

- n x n 2차원 배열 크기 검증
- 위치별 곱셈과 누적 합산 MAC 반복문
- Cross 필터와 X 필터 예시 행렬 분리
- 입력 패턴 검증과 Cross/X 점수 비교 출력
- 3x3 Cross/X 손계산 예시와 함수 결과 비교
- Cross/X/UNDECIDED 판정 함수 단위 검증

### n x n 2차원 배열 크기 검증

`main.py`

#### 추가된 코드

```python
def validate_square_matrix(matrix, expected_size):
    if len(matrix) != expected_size:
        return False

    for row in matrix:
        if len(row) != expected_size:
            return False

    return True


feature = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
]

print(validate_square_matrix(feature, 3))
```

### n x n 2차원 배열 크기 검증

```bash
$ python3 main.py
True
```

### 위치별 곱셈과 누적 합산 MAC 반복문

`main.py`

#### 추가된 코드

```python
def mac(matrix_a, matrix_b):
    size = len(matrix_a)
    score = 0.0

    for row_index in range(size):
        for col_index in range(size):
            score += matrix_a[row_index][col_index] * matrix_b[row_index][col_index]

    return score

```

### 위치별 곱셈과 누적 합산 MAC 반복문

`main.py`

#### 추가된 코드

```python

weight = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
]

print(mac(feature, weight))
```

### 위치별 곱셈과 누적 합산 MAC 반복문

```bash
$ python3 main.py
True
5.0
```

### Cross 필터와 X 필터 예시 행렬 분리

`main.py`

#### 삭제된 코드

```python
feature = [
...
print(validate_square_matrix(feature, 3))
```

#### 추가된 코드

```python
cross_filter = [
...
x_filter = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
]
```

### 입력 패턴 검증과 Cross/X 점수 비교 출력

`main.py`

#### 삭제된 코드

```python
weight = [
...
print(mac(feature, weight))
```

#### 추가된 코드

```python
pattern = [
...
print(validate_square_matrix(pattern, 3))
print(validate_square_matrix(cross_filter, 3))
print(validate_square_matrix(x_filter, 3))
print(f"Cross score: {mac(pattern, cross_filter)}")
print(f"X score: {mac(pattern, x_filter)}")
```

### 3x3 Cross/X 손계산 예시와 함수 결과 비교

```bash
$ python3 main.py
True
True
True
Cross score: 5.0
X score: 1.0
```

### Cross/X/UNDECIDED 판정 함수 단위 검증

`main.py`

#### 추가된 코드

```python
def decide_label(cross_score, x_score, epsilon=1e-9):
    if abs(cross_score - x_score) < epsilon:
        return "UNDECIDED"

    if cross_score > x_score:
        return "Cross"

    return "X"

```

### Cross/X/UNDECIDED 판정 함수 단위 검증

`main.py`

#### 삭제된 코드

```python
print(f"Cross score: {mac(pattern, cross_filter)}")
print(f"X score: {mac(pattern, x_filter)}")
```

#### 추가된 코드

```python
cross_score = mac(pattern, cross_filter)
x_score = mac(pattern, x_filter)
label = decide_label(cross_score, x_score)

print(f"Cross score: {cross_score}")
print(f"X score: {x_score}")
print(f"Label: {label}")
```

### Cross/X/UNDECIDED 판정 함수 단위 검증

```bash
$ python3 main.py
True
True
True
Cross score: 5.0
X score: 1.0
Label: Cross
```


## Chapter 3. 3. data.json 키 규칙과 epsilon 기반 판정

### 테마

- patterns 키 규칙과 expected 정규화 기반 PASS/FAIL 분석
- expected 기호를 Cross/X 라벨로 정규화
- data.json 로드 함수 추가
- patterns 순회와 size_N 필터 선택 후 predicted/expected 계산
- PASS/FAIL 집계와 요약 출력 연결
- data.json 모드 main 진입점 연결

### patterns 키 규칙과 expected 정규화 기반 PASS/FAIL 분석

`main.py`

#### 추가된 코드

```python
import json

```

### expected 기호를 Cross/X 라벨로 정규화

`main.py`

#### 추가된 코드

```python
def normalize_label(label):
    normalized = str(label).strip().lower()

    if normalized in {"+", "cross"}:
        return "Cross"

    if normalized == "x":
        return "X"

    return label

```

### data.json 로드 함수 추가

`main.py`

#### 추가된 코드

```python
def load_data(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

```

### patterns 순회와 size_N 필터 선택 후 predicted/expected 계산

`main.py`

#### 삭제된 코드

```python
cross_filter = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
]
...
x_filter = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
]

pattern = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
]
```

#### 추가된 코드

```python
def run_json_mode(data):
    total_count = 0
    pass_count = 0
    fail_count = 0
    failed_cases = []
...
    for pattern_key, pattern_info in data["patterns"].items():
        parts = pattern_key.split("_")
        filter_key = f"size_{parts[1]}"
        selected_filters = data["filters"][filter_key]
        pattern_input = pattern_info["input"]
        cross_score = mac(pattern_input, selected_filters["cross"])
        x_score = mac(pattern_input, selected_filters["x"])
        predicted = decide_label(cross_score, x_score)
        expected = normalize_label(pattern_info["expected"])
        total_count += 1
```

### PASS/FAIL 집계와 요약 출력 연결

`main.py`

#### 삭제된 코드

```python
print(validate_square_matrix(pattern, 3))
print(validate_square_matrix(cross_filter, 3))
print(validate_square_matrix(x_filter, 3))
cross_score = mac(pattern, cross_filter)
x_score = mac(pattern, x_filter)
label = decide_label(cross_score, x_score)
...
print(f"Cross score: {cross_score}")
print(f"X score: {x_score}")
print(f"Label: {label}")
```

#### 추가된 코드

```python
        if predicted == expected:
            pass_count += 1
        else:
            fail_count += 1
            failed_cases.append(f"{pattern_key}: predicted={predicted}, expected={expected}")
        print(pattern_key, predicted, expected, "PASS" if predicted == expected else "FAIL")
...
    print(f"Total: {total_count}")
    print(f"Pass: {pass_count}")
    print(f"Fail: {fail_count}")
    print("Failed cases:")
    for failed_case in failed_cases:
        print(failed_case)
```

### data.json 모드 main 진입점 연결

`main.py`

#### 추가된 코드

```python


def main():
    data = load_data("data.json")
    run_json_mode(data)


if __name__ == "__main__":
    main()
```

### patterns 키 규칙과 expected 정규화 기반 PASS/FAIL 분석

```bash
$ python3 main.py
size_5_1 UNDECIDED X FAIL
size_5_2 Cross Cross PASS
size_13_1 X X PASS
size_13_2 UNDECIDED Cross FAIL
size_25_1 UNDECIDED X FAIL
size_25_2 Cross Cross PASS
Total: 6
Pass: 3
Fail: 3
Failed cases:
size_5_1: predicted=UNDECIDED, expected=X
size_13_2: predicted=UNDECIDED, expected=Cross
size_25_1: predicted=UNDECIDED, expected=X
```


## Chapter 4. 4. MAC 평균 시간과 O(N^2) 성능 분석

### 테마

- 크기별 평균 시간과 N^2 연산 횟수 성능 요약
- MAC 평균 실행 시간을 재는 helper 함수 추가
- 대표 sample의 Average MAC ms 출력 추가
- 5x5·13x13·25x25 성능 요약 루프 추가

### 크기별 평균 시간과 N^2 연산 횟수 성능 요약

`main.py`

#### 추가된 코드

```python
import time
```

### MAC 평균 실행 시간을 재는 helper 함수 추가

`main.py`

#### 추가된 코드

```python
def measure_average_mac_ms(pattern_matrix, filter_matrix, repeat=10):
    durations = []

    for _ in range(repeat):
        start_time = time.perf_counter()
        mac(pattern_matrix, filter_matrix)
        end_time = time.perf_counter()
        durations.append((end_time - start_time) * 1000)

    return sum(durations) / len(durations)

```

### 대표 sample의 Average MAC ms 출력 추가

`main.py`

#### 추가된 코드

```python
    sample_input = data["patterns"]["size_5_1"]["input"]
    sample_cross_filter = data["filters"]["size_5"]["cross"]
    print(f"Average MAC ms (10 runs): {measure_average_mac_ms(sample_input, sample_cross_filter)}")
...
```

### 5x5·13x13·25x25 성능 요약 루프 추가

`main.py`

#### 추가된 코드

```python
    print("Performance summary:")
    print("Size Average(ms) Operations")
    for pattern_key in ["size_5_1", "size_13_1", "size_25_1"]:
        parts = pattern_key.split("_")
        size = int(parts[1])
        filter_key = f"size_{size}"
        pattern_input = data["patterns"][pattern_key]["input"]
        filter_matrix = data["filters"][filter_key]["cross"]
        average_ms = measure_average_mac_ms(pattern_input, filter_matrix)
        print(f"{size}x{size} {average_ms:.6f} {size * size}")
...
```

### 크기별 평균 시간과 N^2 연산 횟수 성능 요약

```bash
$ python3 main.py
size_5_1 UNDECIDED X FAIL
size_5_2 Cross Cross PASS
size_13_1 X X PASS
size_13_2 UNDECIDED Cross FAIL
size_25_1 UNDECIDED X FAIL
size_25_2 Cross Cross PASS
Total: 6
Pass: 3
Fail: 3
Failed cases:
size_5_1: predicted=UNDECIDED, expected=X
size_13_2: predicted=UNDECIDED, expected=Cross
size_25_1: predicted=UNDECIDED, expected=X
Average MAC ms (10 runs): 0.0009542040061205626
Performance summary:
Size Average(ms) Operations
5x5 0.000875 25
13x13 0.004196 169
25x25 0.013792 625
```


## Chapter 5. 5. 3x3 사용자 입력 검증과 최종 판정

### 테마

- 3x3 입력 함수와 길이 검증 완성
- 필터 A/B와 패턴을 받아 점수와 라벨을 계산하는 수동 모드 추가
- 메뉴 출력과 모드 입력을 받는 main 기본형 구성
- mode 1/2 분기와 미구현 안내 추가
- 3x3 사용자 입력과 형식 오류 재입력 후 A/B 점수 및 최종 판정

### 3x3 입력 함수와 길이 검증 완성

`main.py`

#### 추가된 코드

```python
def read_matrix_from_input(size, title):
    print(title)
    matrix = []

    for _ in range(size):
        while True:
            try:
                row = list(map(float, input().split()))
            except ValueError:
                print(f"입력 형식 오류: 각 줄에 {size}개의 숫자를 공백으로 구분해 입력하세요.")
                continue

            if len(row) != size:
                print(f"입력 형식 오류: 각 줄에 {size}개의 숫자를 공백으로 구분해 입력하세요.")
                continue

            matrix.append(row)
            break

    return matrix

```

### 필터 A/B와 패턴을 받아 점수와 라벨을 계산하는 수동 모드 추가

`main.py`

#### 추가된 코드

```python
def run_manual_mode():
    filter_a = read_matrix_from_input(3, "필터 A (3줄 입력, 공백 구분)")
    filter_b = read_matrix_from_input(3, "필터 B (3줄 입력, 공백 구분)")
    pattern_input = read_matrix_from_input(3, "패턴 (3줄 입력, 공백 구분)")

    print(filter_a)
    print(filter_b)
    print(pattern_input)
    print(validate_square_matrix(filter_a, 3))
    print(validate_square_matrix(filter_b, 3))
    print(validate_square_matrix(pattern_input, 3))
    score_a = mac(pattern_input, filter_a)
    score_b = mac(pattern_input, filter_b)
    print(f"A score: {score_a}")
    print(f"B score: {score_b}")
    label = decide_label(score_a, score_b)
    print(f"Label: {label}")

```

### 메뉴 출력과 모드 입력을 받는 main 기본형 구성

`main.py`

#### 추가된 코드

```python

    print("=== Mini NPU Simulator ===")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")
    mode = input("선택: ")
    print(f"선택한 모드: {mode}")
```

### mode 1/2 분기와 미구현 안내 추가

`main.py`

#### 삭제된 코드

```python
    run_json_mode(data)
```

#### 추가된 코드

```python
    if mode == "1":
        run_manual_mode()
        return
...
    if mode == "2":
        run_json_mode(data)
        return
...
    print("아직 구현되지 않은 모드입니다.")

```

### 3x3 사용자 입력과 형식 오류 재입력 후 A/B 점수 및 최종 판정

```bash
$ python3 main.py
=== Mini NPU Simulator ===
1. 사용자 입력 (3x3)
2. data.json 분석
선택: 1
필터 A (3줄 입력, 공백 구분)
입력 형식 오류: 각 줄에 3개의 숫자를 공백으로 구분해 입력하세요.
필터 B (3줄 입력, 공백 구분)
패턴 (3줄 입력, 공백 구분)
[[0.0, 1.0, 0.0], [1.0, 1.0, 1.0], [0.0, 1.0, 0.0]]
[[1.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]]
[[1.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]]
True
True
True
A score: 1.0
B score: 5.0
Label: X
```


