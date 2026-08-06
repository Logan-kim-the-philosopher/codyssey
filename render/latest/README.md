# E1-2 파이썬 이해하기

- 발표 링크: 발표용 HTML 링크 준비 중

## 챕터

- Chapter 1. 메뉴와 공통 입력 예외 처리
- Chapter 2. Quiz 클래스와 객체 기초
- Chapter 3. QuizGame 클래스와 기능별 메서드 분리
- Chapter 4. 파일 입출력과 데이터 영속성
- Chapter 5. 퀴즈 플레이 기능과 브랜치 병합
- Chapter 6. 추가/목록/삭제/점수 히스토리 검증

## 실습 로그

## Chapter 1. 메뉴와 공통 입력 예외 처리

### 테마

- while 반복 메뉴와 종료 흐름 구현
- 빈 입력/공백/문자/범위 밖 숫자 처리

### while 반복 메뉴와 종료 흐름 구현

`main.py`

```python
def main():
    print("퀴즈 게임 시작")

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        choice = input("선택: ")

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### while 반복 메뉴와 종료 흐름 구현

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### 빈 입력/공백/문자/범위 밖 숫자 처리

`main.py`

```python
def main():
    print("퀴즈 게임 시작")

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### 빈 입력/공백/문자/범위 밖 숫자 처리

```bash
$ printf '\n2\n' | python3 main.py
퀴즈 게임 시작
1. 퀴즈 풀기
2. 종료
선택: 입력이 비어 있습니다. 다시 선택하세요.
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### 빈 입력/공백/문자/범위 밖 숫자 처리

```bash
$ printf 'abc\n2\n' | python3 main.py
퀴즈 게임 시작
1. 퀴즈 풀기
2. 종료
선택: 숫자로 입력해주세요.
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### 빈 입력/공백/문자/범위 밖 숫자 처리

```bash
$ printf '9\n2\n' | python3 main.py
퀴즈 게임 시작
1. 퀴즈 풀기
2. 종료
선택: 1 또는 2만 입력할 수 있습니다.
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### 빈 입력/공백/문자/범위 밖 숫자 처리

```bash
$ printf ' 2 \n' | python3 main.py
퀴즈 게임 시작
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```


## Chapter 2. Quiz 클래스와 객체 기초

### 테마

- Quiz 클래스 뼈대 정의
- Quiz 객체 생성과 속성 확인
- Quiz 메서드로 출력 책임 이동
- 정답 비교 메서드와 불리언 결과 확인

### Quiz 클래스 뼈대 정의

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


def main():
    print("퀴즈 게임 시작")

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### Quiz 객체 생성과 속성 확인

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


def main():
    # 실습용 예시 퀴즈를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )

    # 객체에 저장된 값을 직접 출력해 확인한다.
    print("퀴즈 게임 시작")
    print(quiz1.question)
    print(quiz1.choices)
    print(quiz1.answer)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### Quiz 객체 생성과 속성 확인

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
['int', 'str', 'bool', 'list']
2
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### Quiz 메서드로 출력 책임 이동

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)


def main():
    # 실습용 예시 퀴즈를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )

    # 객체에 저장된 값을 직접 출력해 확인한다.
    print("퀴즈 게임 시작")
    print(quiz1.question)
    print(quiz1.choices)
    print(quiz1.answer)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### Quiz 메서드로 출력 책임 이동

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)


def main():
    # 실습용 예시 퀴즈를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )

    # 객체에 저장된 값을 메서드로 출력해 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### Quiz 메서드로 출력 책임 이동

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### 정답 비교 메서드와 불리언 결과 확인

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


def main():
    # 실습용 예시 퀴즈를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )

    # 객체에 저장된 값을 메서드로 출력해 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### 정답 비교 메서드와 불리언 결과 확인

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


def main():
    # 실습용 예시 퀴즈를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### 정답 비교 메서드와 불리언 결과 확인

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```


## Chapter 3. QuizGame 클래스와 기능별 메서드 분리

### 테마

- 퀴즈 목록과 최고 점수 속성 묶기
- QuizGame 메서드로 메뉴 출력 책임 옮기기
- QuizGame 메서드로 메뉴 입력 검사 책임 옮기기
- QuizGame 메서드로 종료 판단 책임 옮기기
- 한 함수에 몰리지 않는 구조 점검

### 퀴즈 목록과 최고 점수 속성 묶기

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score


def main():
    # 실습용 예시 퀴즈를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### 퀴즈 목록과 최고 점수 속성 묶기

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### 퀴즈 목록과 최고 점수 속성 묶기

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x1033bc590>]
0
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### QuizGame 메서드로 메뉴 출력 책임 옮기기

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        print("1. 퀴즈 풀기")
        print("2. 종료")
        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### QuizGame 메서드로 메뉴 출력 책임 옮기기

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        game.show_menu()

        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### QuizGame 메서드로 메뉴 출력 책임 옮기기

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x109e88590>]
0
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### QuizGame 메서드로 메뉴 입력 검사 책임 옮기기

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        game.show_menu()

        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if choice == "":
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### QuizGame 메서드로 메뉴 입력 검사 책임 옮기기

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        game.show_menu()

        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if game.is_blank_choice(choice):
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### QuizGame 메서드로 메뉴 입력 검사 책임 옮기기

```bash
$ printf '\n2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x105b44590>]
0
1. 퀴즈 풀기
2. 종료
선택: 입력이 비어 있습니다. 다시 선택하세요.
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### QuizGame 메서드로 종료 판단 책임 옮기기

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        game.show_menu()

        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if game.is_blank_choice(choice):
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not choice.isdigit():
            print("숫자로 입력해주세요.")
            continue

        if choice not in ["1", "2"]:
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if choice == "2":
            print("프로그램을 종료합니다.")
            break


main()
```

### QuizGame 메서드로 종료 판단 책임 옮기기

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        game.show_menu()

        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if game.is_blank_choice(choice):
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not game.is_digit_choice(choice):
            print("숫자로 입력해주세요.")
            continue

        if not game.is_valid_menu_choice(choice):
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if game.is_exit_choice(choice):
            print("프로그램을 종료합니다.")
            break


main()
```

### QuizGame 메서드로 종료 판단 책임 옮기기

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x10386c590>]
0
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### 한 함수에 몰리지 않는 구조 점검

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴를 반복해서 보여주고 종료 입력을 기다린다.
    while True:
        game.show_menu()

        # 공백을 제거한 뒤 메뉴 입력을 검사한다.
        choice = input("선택: ").strip()

        if game.is_blank_choice(choice):
            print("입력이 비어 있습니다. 다시 선택하세요.")
            continue

        if not game.is_digit_choice(choice):
            print("숫자로 입력해주세요.")
            continue

        if not game.is_valid_menu_choice(choice):
            print("1 또는 2만 입력할 수 있습니다.")
            continue

        if game.is_exit_choice(choice):
            print("프로그램을 종료합니다.")
            break


main()
```

### 한 함수에 몰리지 않는 구조 점검

`main.py`

```python
class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 한 함수에 몰리지 않는 구조 점검

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x104308590>]
0
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```


## Chapter 4. 파일 입출력과 데이터 영속성

### 테마

- state.json에서 게임 상태 불러오기
- 손상된 state.json에서도 기본값으로 복구하기

### state.json에서 게임 상태 불러오기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### state.json에서 게임 상태 불러오기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        with open("state.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### state.json에서 게임 상태 불러오기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        with open("state.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### state.json에서 게임 상태 불러오기

```bash
$ printf '2\n' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x104145fd0>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}], 'best_score': 0}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}], 'best_score': 0}
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### 손상된 state.json에서도 기본값으로 복구하기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        with open("state.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 손상된 state.json에서도 기본값으로 복구하기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 실습용 예시 퀴즈와 게임 상태를 만든다.
    quiz1 = Quiz(
        "Python에서 문자열을 저장하는 자료형은?",
        ["int", "str", "bool", "list"],
        2,
    )
    game = QuizGame([quiz1], 0)

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 손상된 state.json에서도 기본값으로 복구하기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()
    quiz1 = game.quizzes[0]

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 손상된 state.json에서도 기본값으로 복구하기

```bash
$ tmpdir=$(mktemp -d /private/tmp/e1-2-corrupt-XXXXXX) && cp /Users/hskim/Projects/codyssey/artifacts/e1-2/work/main.py "$tmpdir/main.py" && printf '{ broken json\n' > "$tmpdir/state.json" && cd "$tmpdir" && printf '2\n' | python3 main.py
저장 파일이 손상되어 기본 퀴즈로 복구합니다.
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x10178a120>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}], 'best_score': 0}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}], 'best_score': 0}
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```


## Chapter 5. 퀴즈 플레이 기능과 브랜치 병합

### 테마

- 퀴즈 1개를 실제로 출제하고 정답 판정하기
- 모든 퀴즈를 순서대로 출제하고 점수 합산하기
- 퀴즈가 없는 경우 안내 후 메뉴 복귀

### 퀴즈 1개를 실제로 출제하고 정답 판정하기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 첫 번째 퀴즈를 출제하고 정답 여부를 확인한다.
    def play_first_quiz(self):
        quiz = self.quizzes[0]
        quiz.show()
        answer = int(input("정답 번호: ").strip())

        if quiz.check_answer(answer):
            print("정답입니다.")
            self.update_best_score(1)
            self.save_to_file()
            print(f"현재 최고 점수: {self.best_score}")
            return

        print("오답입니다.")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()
    quiz1 = game.quizzes[0]

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈 1개를 실제로 출제하고 정답 판정하기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 첫 번째 퀴즈를 출제하고 정답 여부를 확인한다.
    def play_first_quiz(self):
        quiz = self.quizzes[0]
        quiz.show()
        answer = int(input("정답 번호: ").strip())

        if quiz.check_answer(answer):
            print("정답입니다.")
            self.update_best_score(1)
            self.save_to_file()
            print(f"현재 최고 점수: {self.best_score}")
            return

        print("오답입니다.")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_first_quiz()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()
    quiz1 = game.quizzes[0]

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈 1개를 실제로 출제하고 정답 판정하기

```bash
$ python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x103bb6120>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}], 'best_score': 0}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}], 'best_score': 0}
1. 퀴즈 풀기
2. 종료
선택: 1
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
정답 번호: 2
정답입니다.
1. 퀴즈 풀기
2. 종료
선택: 2
프로그램을 종료합니다.
```

### 모든 퀴즈를 순서대로 출제하고 점수 합산하기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_first_quiz()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()
    quiz1 = game.quizzes[0]

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 모든 퀴즈를 순서대로 출제하고 점수 합산하기

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()
    quiz1 = game.quizzes[0]

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 모든 퀴즈를 순서대로 출제하고 점수 합산하기

```bash
$ printf '1
2
3
2
2
3
2
' | python3 main.py
퀴즈 게임 시작
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
[<__main__.Quiz object at 0x1084f1fd0>, <__main__.Quiz object at 0x1084d0910>, <__main__.Quiz object at 0x1084d2850>, <__main__.Quiz object at 0x108554770>, <__main__.Quiz object at 0x1085555b0>]
1
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 1}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 1}
1. 퀴즈 풀기
2. 종료
선택: Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
정답 번호: 정답입니다.
Python에서 3 > 1의 결과는 무엇인가?
0
False
True
None
3
정답 번호: 정답입니다.
여러 값을 순서대로 저장하는 자료형은 무엇인가?
dict
list
str
int
2
정답 번호: 정답입니다.
같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?
if
for
print
input
2
정답 번호: 정답입니다.
함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?
break
class
return
import
3
정답 번호: 정답입니다.
최고 점수가 갱신되었습니다.
이번 점수: 5
현재 최고 점수: 5
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```

### 퀴즈가 없는 경우 안내 후 메뉴 복귀

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()
    quiz1 = game.quizzes[0]

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈가 없는 경우 안내 후 메뉴 복귀

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()
    quiz1 = game.quizzes[0]

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    quiz1.show()
    print(quiz1.check_answer(2))
    print(quiz1.check_answer(1))
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈가 없는 경우 안내 후 메뉴 복귀

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈가 없는 경우 안내 후 메뉴 복귀

```bash
$ printf '1
2
' | python3 main.py
퀴즈 게임 시작
[]
0
{'quizzes': [], 'best_score': 0}
{'quizzes': [], 'best_score': 0}
확인할 기본 퀴즈가 없습니다.
1. 퀴즈 풀기
2. 종료
선택: 등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.
1. 퀴즈 풀기
2. 종료
선택: 프로그램을 종료합니다.
```


## Chapter 6. 추가/목록/삭제/점수 히스토리 검증

### 테마

- 퀴즈 추가 후 state.json 반영 확인
- 점수 확인 메뉴로 최고 점수 출력
- 삭제 후 파일 반영 확인
- 추가/삭제 입력 범위 예외 처리 보강

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "2"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "3"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "3"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "3"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

```bash
$ printf '2\n파이썬 창시자는 누구인가?\nGuido van Rossum\nLinus Torvalds\nJames Gosling\nBjarne Stroustrup\n1\n3\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10819dfd0>, <__main__.Quiz object at 0x10817c910>, <__main__.Quiz object at 0x10817e850>, <__main__.Quiz object at 0x1082008a0>, <__main__.Quiz object at 0x1082016e0>]
5
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 5}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 5}
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
1. 퀴즈 풀기
2. 퀴즈 추가
3. 종료
선택: 문제를 입력하세요: 선택지 1: 선택지 2: 선택지 3: 선택지 4: 정답 번호(1-4): 퀴즈가 추가되었습니다.
현재 퀴즈 수: 6
1. 퀴즈 풀기
2. 퀴즈 추가
3. 종료
선택: 프로그램을 종료합니다.
```

### 퀴즈 추가 후 state.json 반영 확인

```bash
$ python3 - <<'PY'
import json
from pathlib import Path
path = Path('state.json')
data = json.loads(path.read_text(encoding='utf-8'))
print(len(data['quizzes']))
print(data['quizzes'][-1]['question'])
print(data['quizzes'][-1]['answer'])
PY
6
파이썬 창시자는 누구인가?
1
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "3"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "5"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "5"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 저장된 퀴즈 목록을 번호와 함께 출력한다.
    def show_quiz_list(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            # 번호와 문제 제목만 먼저 보여준다.
            print(f"{number}. {quiz.question}")

    # 현재 최고 점수를 출력한다.
    def show_best_score(self):
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "5"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 저장된 퀴즈 목록을 번호와 함께 출력한다.
    def show_quiz_list(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            # 번호와 문제 제목만 먼저 보여준다.
            print(f"{number}. {quiz.question}")

    # 현재 최고 점수를 출력한다.
    def show_best_score(self):
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if choice == "3":
                self.show_quiz_list()
                continue

            if choice == "4":
                self.show_best_score()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

```bash
$ printf '4\n5\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10a76e120>, <__main__.Quiz object at 0x10a74c910>, <__main__.Quiz object at 0x10a74e850>, <__main__.Quiz object at 0x10a7d48a0>, <__main__.Quiz object at 0x10a7d56e0>, <__main__.Quiz object at 0x105d62f90>]
5
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}, {'question': '파이썬 창시자는 누구인가?', 'choices': ['Guido van Rossum', 'Linus Torvalds', 'James Gosling', 'Bjarne Stroustrup'], 'answer': 1}], 'best_score': 5}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}, {'question': '파이썬 창시자는 누구인가?', 'choices': ['Guido van Rossum', 'Linus Torvalds', 'James Gosling', 'Bjarne Stroustrup'], 'answer': 1}], 'best_score': 5}
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
선택: 현재 최고 점수: 5
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
선택: 프로그램을 종료합니다.
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "5"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 저장된 퀴즈 목록을 번호와 함께 출력한다.
    def show_quiz_list(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            # 번호와 문제 제목만 먼저 보여준다.
            print(f"{number}. {quiz.question}")

    # 현재 최고 점수를 출력한다.
    def show_best_score(self):
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if choice == "3":
                self.show_quiz_list()
                continue

            if choice == "4":
                self.show_best_score()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5", "6"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "6"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 저장된 퀴즈 목록을 번호와 함께 출력한다.
    def show_quiz_list(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            # 번호와 문제 제목만 먼저 보여준다.
            print(f"{number}. {quiz.question}")

    # 현재 최고 점수를 출력한다.
    def show_best_score(self):
        print(f"현재 최고 점수: {self.best_score}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if choice == "3":
                self.show_quiz_list()
                continue

            if choice == "4":
                self.show_best_score()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5", "6"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "6"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 저장된 퀴즈 목록을 번호와 함께 출력한다.
    def show_quiz_list(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            # 번호와 문제 제목만 먼저 보여준다.
            print(f"{number}. {quiz.question}")

    # 현재 최고 점수를 출력한다.
    def show_best_score(self):
        print(f"현재 최고 점수: {self.best_score}")

    # 번호로 퀴즈 1개를 삭제하고 파일에 저장한다.
    def delete_quiz(self):
        if not self.has_quizzes():
            print("삭제할 퀴즈가 없습니다.")
            return

        self.show_quiz_list()
        number = int(input("삭제할 퀴즈 번호: ").strip())
        deleted_quiz = self.quizzes.pop(number - 1)
        self.save_to_file()
        print(f"삭제된 퀴즈: {deleted_quiz.question}")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if choice == "3":
                self.show_quiz_list()
                continue

            if choice == "4":
                self.show_best_score()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5", "6"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "6"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer = int(input("정답 번호(1-4): ").strip())
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 저장된 퀴즈 목록을 번호와 함께 출력한다.
    def show_quiz_list(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            # 번호와 문제 제목만 먼저 보여준다.
            print(f"{number}. {quiz.question}")

    # 현재 최고 점수를 출력한다.
    def show_best_score(self):
        print(f"현재 최고 점수: {self.best_score}")

    # 번호로 퀴즈 1개를 삭제하고 파일에 저장한다.
    def delete_quiz(self):
        if not self.has_quizzes():
            print("삭제할 퀴즈가 없습니다.")
            return

        self.show_quiz_list()
        number = int(input("삭제할 퀴즈 번호: ").strip())
        deleted_quiz = self.quizzes.pop(number - 1)
        self.save_to_file()
        print(f"삭제된 퀴즈: {deleted_quiz.question}")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if choice == "3":
                self.show_quiz_list()
                continue

            if choice == "4":
                self.delete_quiz()
                continue

            if choice == "5":
                self.show_best_score()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 삭제 후 파일 반영 확인

```bash
$ printf '4\n6\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10a861fd0>, <__main__.Quiz object at 0x10a840910>, <__main__.Quiz object at 0x10a842850>, <__main__.Quiz object at 0x10a8c88a0>, <__main__.Quiz object at 0x10a8c96e0>, <__main__.Quiz object at 0x10a732f90>]
5
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}, {'question': '파이썬 창시자는 누구인가?', 'choices': ['Guido van Rossum', 'Linus Torvalds', 'James Gosling', 'Bjarne Stroustrup'], 'answer': 1}], 'best_score': 5}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}, {'question': '파이썬 창시자는 누구인가?', 'choices': ['Guido van Rossum', 'Linus Torvalds', 'James Gosling', 'Bjarne Stroustrup'], 'answer': 1}], 'best_score': 5}
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 등록된 퀴즈 목록 (총 6개)
1. Python에서 문자열을 저장하는 자료형은?
2. Python에서 3 > 1의 결과는 무엇인가?
3. 여러 값을 순서대로 저장하는 자료형은 무엇인가?
4. 같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?
5. 함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?
6. 파이썬 창시자는 누구인가?
삭제할 퀴즈 번호: 삭제된 퀴즈: 파이썬 창시자는 누구인가?
현재 퀴즈 수: 5
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 삭제 후 파일 반영 확인

```bash
$ python3 - <<'PY'
import json
from pathlib import Path
path = Path('state.json')
data = json.loads(path.read_text(encoding='utf-8'))
print(len(data['quizzes']))
print(data['quizzes'][-1]['question'])
PY
5
함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?
```

### 추가/삭제 입력 범위 예외 처리 보강

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5", "6"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "6"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer_text = input("정답 번호(1-4): ").strip()

        if answer_text == "":
            print("정답 번호를 입력해주세요.")
            return

        if not answer_text.isdigit():
            print("정답 번호는 숫자로 입력해주세요.")
            return

        answer = int(answer_text)

        if answer < 1 or answer > 4:
            print("정답 번호는 1부터 4까지만 입력할 수 있습니다.")
            return

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 저장된 퀴즈 목록을 번호와 함께 출력한다.
    def show_quiz_list(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            # 번호와 문제 제목만 먼저 보여준다.
            print(f"{number}. {quiz.question}")

    # 현재 최고 점수를 출력한다.
    def show_best_score(self):
        print(f"현재 최고 점수: {self.best_score}")

    # 번호로 퀴즈 1개를 삭제하고 파일에 저장한다.
    def delete_quiz(self):
        if not self.has_quizzes():
            print("삭제할 퀴즈가 없습니다.")
            return

        self.show_quiz_list()
        number = int(input("삭제할 퀴즈 번호: ").strip())
        deleted_quiz = self.quizzes.pop(number - 1)
        self.save_to_file()
        print(f"삭제된 퀴즈: {deleted_quiz.question}")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if choice == "3":
                self.show_quiz_list()
                continue

            if choice == "4":
                self.delete_quiz()
                continue

            if choice == "5":
                self.show_best_score()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 추가/삭제 입력 범위 예외 처리 보강

`main.py`

```python
import json


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답을 저장한다.
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    # 게임 전체에서 퀴즈 목록과 최고 점수를 관리한다.
    def __init__(self, quizzes, best_score):
        self.quizzes = quizzes
        self.best_score = best_score

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5", "6"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "6"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.show()
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                print("정답입니다.")
                score += 1
                continue

            print("오답입니다.")

        self.update_best_score(score)
        self.save_to_file()
        print(f"이번 점수: {score}")
        print(f"현재 최고 점수: {self.best_score}")

    # 새 퀴즈 입력을 받아 목록에 추가하고 파일에 저장한다.
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()
        choices = []

        for number in range(1, 5):
            # 선택지 4개를 순서대로 입력받는다.
            choice = input(f"선택지 {number}: ").strip()
            choices.append(choice)

        answer_text = input("정답 번호(1-4): ").strip()

        if answer_text == "":
            print("정답 번호를 입력해주세요.")
            return

        if not answer_text.isdigit():
            print("정답 번호는 숫자로 입력해주세요.")
            return

        answer = int(answer_text)

        if answer < 1 or answer > 4:
            print("정답 번호는 1부터 4까지만 입력할 수 있습니다.")
            return

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_to_file()
        print("퀴즈가 추가되었습니다.")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 저장된 퀴즈 목록을 번호와 함께 출력한다.
    def show_quiz_list(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            # 번호와 문제 제목만 먼저 보여준다.
            print(f"{number}. {quiz.question}")

    # 현재 최고 점수를 출력한다.
    def show_best_score(self):
        print(f"현재 최고 점수: {self.best_score}")

    # 번호로 퀴즈 1개를 삭제하고 파일에 저장한다.
    def delete_quiz(self):
        if not self.has_quizzes():
            print("삭제할 퀴즈가 없습니다.")
            return

        self.show_quiz_list()
        number_text = input("삭제할 퀴즈 번호: ").strip()

        if number_text == "":
            print("삭제 번호를 입력해주세요.")
            return

        if not number_text.isdigit():
            print("삭제 번호는 숫자로 입력해주세요.")
            return

        number = int(number_text)

        if number < 1 or number > len(self.quizzes):
            print("삭제할 수 있는 퀴즈 번호만 입력해주세요.")
            return

        deleted_quiz = self.quizzes.pop(number - 1)
        self.save_to_file()
        print(f"삭제된 퀴즈: {deleted_quiz.question}")
        print(f"현재 퀴즈 수: {len(self.quizzes)}")

    # 메뉴 반복 흐름을 게임 객체 안에서 실행한다.
    def run_menu(self):
        while True:
            self.show_menu()

            # 공백을 제거한 뒤 메뉴 입력을 검사한다.
            choice = input("선택: ").strip()

            if self.is_blank_choice(choice):
                print("입력이 비어 있습니다. 다시 선택하세요.")
                continue

            if not self.is_digit_choice(choice):
                print("숫자로 입력해주세요.")
                continue

            if not self.is_valid_menu_choice(choice):
                print("1 또는 2만 입력할 수 있습니다.")
                continue

            if choice == "1":
                self.play_all_quizzes()
                continue

            if choice == "2":
                self.add_quiz()
                continue

            if choice == "3":
                self.show_quiz_list()
                continue

            if choice == "4":
                self.delete_quiz()
                continue

            if choice == "5":
                self.show_best_score()
                continue

            if self.is_exit_choice(choice):
                print("프로그램을 종료합니다.")
                break

    # 현재 게임 상태를 저장용 딕셔너리로 만든다.
    def to_dict(self):
        return {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(item["question"], item["choices"], item["answer"])
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    # 저장 파일을 우선 읽고, 없으면 기본 퀴즈로 게임을 시작한다.
    game = QuizGame.load_from_file()

    # 객체에 저장된 값과 메서드 동작을 확인한다.
    print("퀴즈 게임 시작")
    print(game.quizzes)
    print(game.best_score)
    print(game.to_dict())
    game.save_to_file()
    loaded_game = QuizGame.load_from_file()
    print(loaded_game.to_dict())

    if game.has_quizzes():
        quiz1 = game.quizzes[0]
        quiz1.show()
        print(quiz1.check_answer(2))
        print(quiz1.check_answer(1))
    else:
        print("확인할 기본 퀴즈가 없습니다.")

    # 메뉴 반복 흐름도 게임 객체에 맡긴다.
    game.run_menu()


main()
```

### 추가/삭제 입력 범위 예외 처리 보강

```bash
$ printf '2\n테스트 문제\nA\nB\nC\nD\n9\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10a985fd0>, <__main__.Quiz object at 0x10a964910>, <__main__.Quiz object at 0x10a966850>, <__main__.Quiz object at 0x10a9ec8a0>, <__main__.Quiz object at 0x10a9ed6e0>]
5
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 5}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 5}
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 문제를 입력하세요: 선택지 1: 선택지 2: 선택지 3: 선택지 4: 정답 번호(1-4): 정답 번호는 1부터 4까지만 입력할 수 있습니다.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 추가/삭제 입력 범위 예외 처리 보강

```bash
$ printf '4\n9\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10a101fd0>, <__main__.Quiz object at 0x10a0e0910>, <__main__.Quiz object at 0x10a0e2850>, <__main__.Quiz object at 0x10a1688a0>, <__main__.Quiz object at 0x10a1696e0>]
5
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 5}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 5}
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
True
False
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 등록된 퀴즈 목록 (총 5개)
1. Python에서 문자열을 저장하는 자료형은?
2. Python에서 3 > 1의 결과는 무엇인가?
3. 여러 값을 순서대로 저장하는 자료형은 무엇인가?
4. 같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?
5. 함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?
삭제할 퀴즈 번호: 삭제할 수 있는 퀴즈 번호만 입력해주세요.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```


