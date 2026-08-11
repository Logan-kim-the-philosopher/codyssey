import json
import time


def validate_square_matrix(matrix, expected_size):
    if len(matrix) != expected_size:
        return False

    for row in matrix:
        if len(row) != expected_size:
            return False

    return True


def mac(matrix_a, matrix_b):
    size = len(matrix_a)
    score = 0.0

    for row_index in range(size):
        for col_index in range(size):
            score += matrix_a[row_index][col_index] * matrix_b[row_index][col_index]

    return score


def decide_label(cross_score, x_score, epsilon=1e-9):
    if abs(cross_score - x_score) < epsilon:
        return "UNDECIDED"

    if cross_score > x_score:
        return "Cross"

    return "X"


def normalize_label(label):
    normalized = str(label).strip().lower()

    if normalized in {"+", "cross"}:
        return "Cross"

    if normalized == "x":
        return "X"

    return label


def load_data(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def measure_average_mac_ms(pattern_matrix, filter_matrix, repeat=10):
    durations = []

    for _ in range(repeat):
        start_time = time.perf_counter()
        mac(pattern_matrix, filter_matrix)
        end_time = time.perf_counter()
        durations.append((end_time - start_time) * 1000)

    return sum(durations) / len(durations)


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


def run_json_mode(data):
    total_count = 0
    pass_count = 0
    fail_count = 0
    failed_cases = []

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
        if predicted == expected:
            pass_count += 1
        else:
            fail_count += 1
            failed_cases.append(f"{pattern_key}: predicted={predicted}, expected={expected}")
        print(pattern_key, predicted, expected, "PASS" if predicted == expected else "FAIL")

    print(f"Total: {total_count}")
    print(f"Pass: {pass_count}")
    print(f"Fail: {fail_count}")
    print("Failed cases:")
    for failed_case in failed_cases:
        print(failed_case)

    sample_input = data["patterns"]["size_5_1"]["input"]
    sample_cross_filter = data["filters"]["size_5"]["cross"]
    print(f"Average MAC ms (10 runs): {measure_average_mac_ms(sample_input, sample_cross_filter)}")

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


def main():
    data = load_data("data.json")

    print("=== Mini NPU Simulator ===")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")
    mode = input("선택: ")
    print(f"선택한 모드: {mode}")

    if mode == "1":
        run_manual_mode()
        return

    if mode == "2":
        run_json_mode(data)
        return

    print("아직 구현되지 않은 모드입니다.")


if __name__ == "__main__":
    main()
