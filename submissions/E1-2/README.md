# E1-2 파이썬 이해하기

- 발표 링크: [발표용 HTML](https://logan-kim-the-philosopher.github.io/codyssey/E1-2/)

## 챕터

- Chapter 1. 메뉴와 공통 입력 예외 처리
- Chapter 2. Quiz 클래스와 객체 기초
- Chapter 3. QuizGame 클래스와 기능별 메서드 분리
- Chapter 4. 파일 입출력과 데이터 영속성
- Chapter 5. 퀴즈 플레이 기능과 브랜치 병합
- Chapter 6. 추가/목록/삭제/점수 히스토리 검증
- Chapter 7. README, Git 로그, clone/pull 제출 증거

## 실습 로그

## Chapter 1. 메뉴와 공통 입력 예외 처리

### 테마

- while 반복 메뉴와 종료 흐름 구현
- 빈 입력/공백/문자/범위 밖 숫자 처리
- 메뉴 기능 완성 후 commit 기록

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

### 메뉴 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
A  .gitignore
A  work/main.py
```

### 메뉴 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 메뉴 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 반복 메뉴와 종료 흐름 구현"
[codex/e1-2-history-rebuild (root-commit) 27884fe] Feat: 반복 메뉴와 종료 흐름 구현
 2 files changed, 31 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 work/main.py
```

### 메뉴 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph
* 27884fe Feat: 반복 메뉴와 종료 흐름 구현
```


## Chapter 2. Quiz 클래스와 객체 기초

### 테마

- Quiz 클래스 뼈대 정의
- Quiz 객체 생성과 속성 확인
- Quiz 메서드로 출력 책임 이동
- 정답 비교 메서드와 불리언 결과 확인
- Quiz 기능 완성 후 commit 기록

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

### Quiz 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
```

### Quiz 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### Quiz 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: Quiz 클래스와 정답 판정 구현"
[codex/e1-2-history-rebuild 7e2694f] Feat: Quiz 클래스와 정답 판정 구현
 1 file changed, 30 insertions(+)
```

### Quiz 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 7e2694f (HEAD -> codex/e1-2-history-rebuild) Feat: Quiz 클래스와 정답 판정 구현
* bfc04cf Feat: 반복 메뉴와 종료 흐름 구현
```


## Chapter 3. QuizGame 클래스와 기능별 메서드 분리

### 테마

- 퀴즈 목록과 최고 점수 속성 묶기
- QuizGame 메서드로 메뉴 출력 책임 옮기기
- QuizGame 메서드로 메뉴 입력 검사 책임 옮기기
- QuizGame 메서드로 종료 판단 책임 옮기기
- 한 함수에 몰리지 않는 구조 점검
- QuizGame 구조 완성 후 commit 기록

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

### QuizGame 구조 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
```

### QuizGame 구조 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### QuizGame 구조 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Refactor: QuizGame으로 메뉴 책임 분리"
[codex/e1-2-history-rebuild 054e3c8] Refactor: QuizGame으로 메뉴 책임 분리
 1 file changed, 58 insertions(+), 23 deletions(-)
```

### QuizGame 구조 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 054e3c8 (HEAD -> codex/e1-2-history-rebuild) Refactor: QuizGame으로 메뉴 책임 분리
* 7e2694f Feat: Quiz 클래스와 정답 판정 구현
* bfc04cf Feat: 반복 메뉴와 종료 흐름 구현
```


## Chapter 4. 파일 입출력과 데이터 영속성

### 테마

- state.json에서 게임 상태 불러오기
- 손상된 state.json에서도 기본값으로 복구하기
- 저장 복구 기능 완성 후 commit 기록

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

### 저장 복구 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
?? work/state.json
```

### 저장 복구 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 저장 복구 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: state.json 저장과 복구 처리 추가"
[codex/e1-2-history-rebuild a5d5759] Feat: state.json 저장과 복구 처리 추가
 2 files changed, 99 insertions(+), 7 deletions(-)
 create mode 100644 work/state.json
```

### 저장 복구 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* a5d5759 (HEAD -> codex/e1-2-history-rebuild) Feat: state.json 저장과 복구 처리 추가
* 054e3c8 Refactor: QuizGame으로 메뉴 책임 분리
* 7e2694f Feat: Quiz 클래스와 정답 판정 구현
```


## Chapter 5. 퀴즈 플레이 기능과 브랜치 병합

### 테마

- 퀴즈 1개를 실제로 출제하고 정답 판정하기
- 모든 퀴즈를 순서대로 출제하고 점수 합산하기
- 퀴즈가 없는 경우 안내 후 메뉴 복귀
- 플레이 기능 완성 후 commit 기록
- 랜덤 출제와 문제 수 선택 적용
- 힌트 사용과 점수 차감 확인
- 보너스 기능 완성 후 commit 기록

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

### 플레이 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
 M work/state.json
```

### 플레이 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 플레이 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 퀴즈 플레이와 점수 계산 구현"
[codex/e1-2-history-rebuild 9a48940] Feat: 퀴즈 플레이와 점수 계산 구현
 2 files changed, 47 insertions(+), 5 deletions(-)
```

### 플레이 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 9a48940 (HEAD -> codex/e1-2-history-rebuild) Feat: 퀴즈 플레이와 점수 계산 구현
* a5d5759 Feat: state.json 저장과 복구 처리 추가
* 054e3c8 Refactor: QuizGame으로 메뉴 책임 분리
```

### 랜덤 출제와 문제 수 선택 적용

`main.py`

```python
import json
import random


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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)


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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
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
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 랜덤 출제와 문제 수 선택 적용

```bash
$ printf '1\n2\n2\n2\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10a96d7f0>, <__main__.Quiz object at 0x106011f90>, <__main__.Quiz object at 0x106013750>, <__main__.Quiz object at 0x10a928770>, <__main__.Quiz object at 0x10a92ab10>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 0}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 0}
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
선택: 몇 문제를 풀까요? (1-5): 2문제를 랜덤으로 출제합니다.
여러 값을 순서대로 저장하는 자료형은 무엇인가?
dict
list
str
int
2
정답 번호: 정답입니다.
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
정답 번호: 정답입니다.
최고 점수가 갱신되었습니다.
이번 점수: 2
현재 최고 점수: 2
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 랜덤 출제와 문제 수 선택 적용

```bash
$ printf '1\n9\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x105f757f0>, <__main__.Quiz object at 0x1015e1f90>, <__main__.Quiz object at 0x1015e3750>, <__main__.Quiz object at 0x105f30770>, <__main__.Quiz object at 0x105f32b10>]
2
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 2}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 2}
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
선택: 몇 문제를 풀까요? (1-5): 풀 수 있는 문제 수만 입력해주세요.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 랜덤 출제와 문제 수 선택 적용

```bash
$ printf '1\nabc\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x1081b57f0>, <__main__.Quiz object at 0x10385df90>, <__main__.Quiz object at 0x10385f750>, <__main__.Quiz object at 0x108170770>, <__main__.Quiz object at 0x108172b10>]
2
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 2}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 2}
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
선택: 몇 문제를 풀까요? (1-5): 문제 수는 숫자로 입력해주세요.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 힌트 사용과 점수 차감 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 힌트 사용과 점수 차감 확인

```bash
$ printf '1\n1\ny\n3\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10406d7f0>, <__main__.Quiz object at 0x103f9df90>, <__main__.Quiz object at 0x103f9f750>, <__main__.Quiz object at 0x104030770>, <__main__.Quiz object at 0x104032b10>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 0}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 0}
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
선택: 몇 문제를 풀까요? (1-5): 1문제를 랜덤으로 출제합니다.
함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?
break
class
return
import
3
힌트를 볼까요? (y/n): 힌트: 함수 바깥으로 값을 다시 보내는 단어입니다.
힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.
정답 번호: 정답이지만 힌트를 사용해 점수는 올라가지 않습니다.
이번 점수: 0
현재 최고 점수: 0
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 보너스 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
 M work/state.json
```

### 보너스 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 보너스 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 랜덤 출제와 힌트 기능 추가"
[codex/e1-2-history-rebuild 599708f] Feat: 랜덤 출제와 힌트 기능 추가
 2 files changed, 129 insertions(+), 44 deletions(-)
```

### 보너스 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 599708f (HEAD -> codex/e1-2-history-rebuild) Feat: 랜덤 출제와 힌트 기능 추가
* baeba2e Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
* 9a48940 Feat: 퀴즈 플레이와 점수 계산 구현
```


## Chapter 6. 추가/목록/삭제/점수 히스토리 검증

### 테마

- 퀴즈 추가 후 state.json 반영 확인
- 점수 확인 메뉴로 최고 점수 출력
- 삭제 후 파일 반영 확인
- 추가/삭제 입력 범위 예외 처리 보강
- 문제 관리 기능 완성 후 commit 기록
- 날짜/시간 포함 게임 기록 저장 확인
- 플레이 기록 기능 완성 후 commit 기록

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


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
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


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
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


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
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 추가/삭제 입력 범위 예외 처리 보강

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


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

### 문제 관리 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
 M work/state.json
```

### 문제 관리 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 문제 관리 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 퀴즈 추가 삭제와 점수 메뉴 구현"
[codex/e1-2-history-rebuild baeba2e] Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
 2 files changed, 138 insertions(+), 4 deletions(-)
```

### 문제 관리 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* baeba2e (HEAD -> codex/e1-2-history-rebuild) Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
* 9a48940 Feat: 퀴즈 플레이와 점수 계산 구현
* a5d5759 Feat: state.json 저장과 복구 처리 추가
```

### 날짜/시간 포함 게임 기록 저장 확인

`main.py`

```python
import json
import random
from datetime import datetime


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


class QuizGame:
    # 게임 전체에서 퀴즈 목록, 최고 점수, 플레이 기록을 관리한다.
    def __init__(self, quizzes, best_score, score_history):
        self.quizzes = quizzes
        self.best_score = best_score
        self.score_history = score_history

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 플레이 기록")
        print("7. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5", "6", "7"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "7"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 이번 플레이 결과를 날짜/시간과 함께 기록 목록에 추가한다.
    def record_score_history(self, total_questions, score):
        self.score_history.append(
            {
                "played_at": datetime.now().isoformat(timespec="seconds"),
                "total_questions": total_questions,
                "score": score,
            }
        )

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
                    print("정답입니다.")
                    score += 1
                continue

            print("오답입니다.")

        self.record_score_history(count, score)
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

    # 저장된 플레이 기록을 최근 순서대로 출력한다.
    def show_score_history(self):
        if len(self.score_history) == 0:
            print("아직 저장된 플레이 기록이 없습니다.")
            return

        print("플레이 기록")
        for number, history in enumerate(self.score_history, start=1):
            print(
                f"{number}. {history['played_at']} | "
                f"{history['total_questions']}문제 | "
                f"{history['score']}점"
            )

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

            if choice == "6":
                self.show_score_history()
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
            "score_history": self.score_history,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0, [])
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0, [])
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0, [])

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"], data.get("score_history", []))


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 날짜/시간 포함 게임 기록 저장 확인

```bash
$ printf '1\n1\nn\n2\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x1086a17f0>, <__main__.Quiz object at 0x103c99f90>, <__main__.Quiz object at 0x103c9b750>, <__main__.Quiz object at 0x108668770>, <__main__.Quiz object at 0x10866ab10>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 0, 'score_history': []}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 0, 'score_history': []}
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
선택: 몇 문제를 풀까요? (1-5): 1문제를 랜덤으로 출제합니다.
같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?
if
for
print
input
2
힌트를 볼까요? (y/n): 정답 번호: 정답입니다.
최고 점수가 갱신되었습니다.
이번 점수: 1
현재 최고 점수: 1
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 날짜/시간 포함 게임 기록 저장 확인

```bash
$ python3 -m json.tool state.json
{
    "quizzes": [
        {
            "question": "Python에서 문자열을 저장하는 자료형은?",
            "choices": [
                "int",
                "str",
                "bool",
                "list"
            ],
            "answer": 2,
            "hint": "문자열은 따옴표로 감싸 자주 표현합니다."
        },
        {
            "question": "Python에서 3 > 1의 결과는 무엇인가?",
            "choices": [
                "0",
                "False",
                "True",
                "None"
            ],
            "answer": 3,
            "hint": "비교 연산의 결과는 참 또는 거짓입니다."
        },
        {
            "question": "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
            "choices": [
                "dict",
                "list",
                "str",
                "int"
            ],
            "answer": 2,
            "hint": "대괄호 [] 로 만드는 자료형을 떠올려보세요."
        },
        {
            "question": "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
            "choices": [
                "if",
                "for",
                "print",
                "input"
            ],
            "answer": 2,
            "hint": "반복문 문법을 고르면 됩니다."
        },
        {
            "question": "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
            "choices": [
                "break",
                "class",
                "return",
                "import"
            ],
            "answer": 3,
            "hint": "함수 바깥으로 값을 다시 보내는 단어입니다."
        }
    ],
    "best_score": 1,
    "score_history": [
        {
            "played_at": "2026-08-06T19:55:55",
            "total_questions": 1,
            "score": 1
        }
    ]
}
```

### 날짜/시간 포함 게임 기록 저장 확인

```bash
$ printf '6\n7\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x1083a17f0>, <__main__.Quiz object at 0x103971f90>, <__main__.Quiz object at 0x103973750>, <__main__.Quiz object at 0x1083688a0>, <__main__.Quiz object at 0x10836ac40>]
1
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 1, 'score_history': [{'played_at': '2026-08-06T19:55:55', 'total_questions': 1, 'score': 1}]}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 1, 'score_history': [{'played_at': '2026-08-06T19:55:55', 'total_questions': 1, 'score': 1}]}
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
6. 플레이 기록
7. 종료
선택: 플레이 기록
1. 2026-08-06T19:55:55 | 1문제 | 1점
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 플레이 기록
7. 종료
선택: 프로그램을 종료합니다.
```

### 플레이 기록 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
 M work/state.json
```

### 플레이 기록 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 플레이 기록 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 플레이 기록 저장 기능 추가"
[codex/e1-2-history-rebuild 9d2cee1] Feat: 플레이 기록 저장 기능 추가
 2 files changed, 47 insertions(+), 10 deletions(-)
```

### 플레이 기록 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 9d2cee1 (HEAD -> codex/e1-2-history-rebuild) Feat: 플레이 기록 저장 기능 추가
* 599708f Feat: 랜덤 출제와 힌트 기능 추가
* baeba2e Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
```


## Chapter 7. README, Git 로그, clone/pull 제출 증거

### 테마

- README 필수 항목 작성
- git log --oneline --graph와 커밋 수 확인
- GitHub 저장소 연결과 업로드 확인
- 별도 디렉터리에 clone
- clone 변경 push 후 원래 작업 폴더에서 pull
- 개발 환경과 실행 화면 증거 정리

### README 필수 항목 작성

```bash
$ cat README.md
# E1-2 파이썬 이해하기

- 발표 링크: 발표용 HTML 링크 준비 중

## 챕터

- Chapter 1. 메뉴와 공통 입력 예외 처리
- Chapter 2. Quiz 클래스와 객체 기초
- Chapter 3. QuizGame 클래스와 기능별 메서드 분리
- Chapter 4. 파일 입출력과 데이터 영속성
- Chapter 5. 퀴즈 플레이 기능과 브랜치 병합
- Chapter 6. 추가/목록/삭제/점수 히스토리 검증
- Chapter 7. README, Git 로그, clone/pull 제출 증거

## 실습 로그

## Chapter 1. 메뉴와 공통 입력 예외 처리

### 테마

- while 반복 메뉴와 종료 흐름 구현
- 빈 입력/공백/문자/범위 밖 숫자 처리
- 메뉴 기능 완성 후 commit 기록

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

### 메뉴 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
A  .gitignore
A  work/main.py
```

### 메뉴 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 메뉴 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 반복 메뉴와 종료 흐름 구현"
[codex/e1-2-history-rebuild (root-commit) 27884fe] Feat: 반복 메뉴와 종료 흐름 구현
 2 files changed, 31 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 work/main.py
```

### 메뉴 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph
* 27884fe Feat: 반복 메뉴와 종료 흐름 구현
```


## Chapter 2. Quiz 클래스와 객체 기초

### 테마

- Quiz 클래스 뼈대 정의
- Quiz 객체 생성과 속성 확인
- Quiz 메서드로 출력 책임 이동
- 정답 비교 메서드와 불리언 결과 확인
- Quiz 기능 완성 후 commit 기록

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

### Quiz 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
```

### Quiz 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### Quiz 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: Quiz 클래스와 정답 판정 구현"
[codex/e1-2-history-rebuild 7e2694f] Feat: Quiz 클래스와 정답 판정 구현
 1 file changed, 30 insertions(+)
```

### Quiz 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 7e2694f (HEAD -> codex/e1-2-history-rebuild) Feat: Quiz 클래스와 정답 판정 구현
* bfc04cf Feat: 반복 메뉴와 종료 흐름 구현
```


## Chapter 3. QuizGame 클래스와 기능별 메서드 분리

### 테마

- 퀴즈 목록과 최고 점수 속성 묶기
- QuizGame 메서드로 메뉴 출력 책임 옮기기
- QuizGame 메서드로 메뉴 입력 검사 책임 옮기기
- QuizGame 메서드로 종료 판단 책임 옮기기
- 한 함수에 몰리지 않는 구조 점검
- QuizGame 구조 완성 후 commit 기록

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

### QuizGame 구조 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
```

### QuizGame 구조 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### QuizGame 구조 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Refactor: QuizGame으로 메뉴 책임 분리"
[codex/e1-2-history-rebuild 054e3c8] Refactor: QuizGame으로 메뉴 책임 분리
 1 file changed, 58 insertions(+), 23 deletions(-)
```

### QuizGame 구조 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 054e3c8 (HEAD -> codex/e1-2-history-rebuild) Refactor: QuizGame으로 메뉴 책임 분리
* 7e2694f Feat: Quiz 클래스와 정답 판정 구현
* bfc04cf Feat: 반복 메뉴와 종료 흐름 구현
```


## Chapter 4. 파일 입출력과 데이터 영속성

### 테마

- state.json에서 게임 상태 불러오기
- 손상된 state.json에서도 기본값으로 복구하기
- 저장 복구 기능 완성 후 commit 기록

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

### 저장 복구 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
?? work/state.json
```

### 저장 복구 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 저장 복구 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: state.json 저장과 복구 처리 추가"
[codex/e1-2-history-rebuild a5d5759] Feat: state.json 저장과 복구 처리 추가
 2 files changed, 99 insertions(+), 7 deletions(-)
 create mode 100644 work/state.json
```

### 저장 복구 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* a5d5759 (HEAD -> codex/e1-2-history-rebuild) Feat: state.json 저장과 복구 처리 추가
* 054e3c8 Refactor: QuizGame으로 메뉴 책임 분리
* 7e2694f Feat: Quiz 클래스와 정답 판정 구현
```


## Chapter 5. 퀴즈 플레이 기능과 브랜치 병합

### 테마

- 퀴즈 1개를 실제로 출제하고 정답 판정하기
- 모든 퀴즈를 순서대로 출제하고 점수 합산하기
- 퀴즈가 없는 경우 안내 후 메뉴 복귀
- 플레이 기능 완성 후 commit 기록
- 랜덤 출제와 문제 수 선택 적용
- 힌트 사용과 점수 차감 확인
- 보너스 기능 완성 후 commit 기록

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

### 플레이 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
 M work/state.json
```

### 플레이 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 플레이 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 퀴즈 플레이와 점수 계산 구현"
[codex/e1-2-history-rebuild 9a48940] Feat: 퀴즈 플레이와 점수 계산 구현
 2 files changed, 47 insertions(+), 5 deletions(-)
```

### 플레이 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 9a48940 (HEAD -> codex/e1-2-history-rebuild) Feat: 퀴즈 플레이와 점수 계산 구현
* a5d5759 Feat: state.json 저장과 복구 처리 추가
* 054e3c8 Refactor: QuizGame으로 메뉴 책임 분리
```

### 랜덤 출제와 문제 수 선택 적용

`main.py`

```python
import json
import random


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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)


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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
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
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 랜덤 출제와 문제 수 선택 적용

```bash
$ printf '1\n2\n2\n2\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10a96d7f0>, <__main__.Quiz object at 0x106011f90>, <__main__.Quiz object at 0x106013750>, <__main__.Quiz object at 0x10a928770>, <__main__.Quiz object at 0x10a92ab10>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 0}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 0}
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
선택: 몇 문제를 풀까요? (1-5): 2문제를 랜덤으로 출제합니다.
여러 값을 순서대로 저장하는 자료형은 무엇인가?
dict
list
str
int
2
정답 번호: 정답입니다.
Python에서 문자열을 저장하는 자료형은?
int
str
bool
list
2
정답 번호: 정답입니다.
최고 점수가 갱신되었습니다.
이번 점수: 2
현재 최고 점수: 2
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 랜덤 출제와 문제 수 선택 적용

```bash
$ printf '1\n9\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x105f757f0>, <__main__.Quiz object at 0x1015e1f90>, <__main__.Quiz object at 0x1015e3750>, <__main__.Quiz object at 0x105f30770>, <__main__.Quiz object at 0x105f32b10>]
2
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 2}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 2}
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
선택: 몇 문제를 풀까요? (1-5): 풀 수 있는 문제 수만 입력해주세요.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 랜덤 출제와 문제 수 선택 적용

```bash
$ printf '1\nabc\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x1081b57f0>, <__main__.Quiz object at 0x10385df90>, <__main__.Quiz object at 0x10385f750>, <__main__.Quiz object at 0x108170770>, <__main__.Quiz object at 0x108172b10>]
2
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 2}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3}], 'best_score': 2}
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
선택: 몇 문제를 풀까요? (1-5): 문제 수는 숫자로 입력해주세요.
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 힌트 사용과 점수 차감 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 힌트 사용과 점수 차감 확인

```bash
$ printf '1\n1\ny\n3\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x10406d7f0>, <__main__.Quiz object at 0x103f9df90>, <__main__.Quiz object at 0x103f9f750>, <__main__.Quiz object at 0x104030770>, <__main__.Quiz object at 0x104032b10>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 0}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 0}
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
선택: 몇 문제를 풀까요? (1-5): 1문제를 랜덤으로 출제합니다.
함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?
break
class
return
import
3
힌트를 볼까요? (y/n): 힌트: 함수 바깥으로 값을 다시 보내는 단어입니다.
힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.
정답 번호: 정답이지만 힌트를 사용해 점수는 올라가지 않습니다.
이번 점수: 0
현재 최고 점수: 0
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 보너스 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
 M work/state.json
```

### 보너스 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 보너스 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 랜덤 출제와 힌트 기능 추가"
[codex/e1-2-history-rebuild 599708f] Feat: 랜덤 출제와 힌트 기능 추가
 2 files changed, 129 insertions(+), 44 deletions(-)
```

### 보너스 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 599708f (HEAD -> codex/e1-2-history-rebuild) Feat: 랜덤 출제와 힌트 기능 추가
* baeba2e Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
* 9a48940 Feat: 퀴즈 플레이와 점수 계산 구현
```


## Chapter 6. 추가/목록/삭제/점수 히스토리 검증

### 테마

- 퀴즈 추가 후 state.json 반영 확인
- 점수 확인 메뉴로 최고 점수 출력
- 삭제 후 파일 반영 확인
- 추가/삭제 입력 범위 예외 처리 보강
- 문제 관리 기능 완성 후 commit 기록
- 날짜/시간 포함 게임 기록 저장 확인
- 플레이 기록 기능 완성 후 commit 기록

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 퀴즈 추가 후 state.json 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


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
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 점수 확인 메뉴로 최고 점수 출력

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


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
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 삭제 후 파일 반영 확인

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


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
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 추가/삭제 입력 범위 예외 처리 보강

`main.py`

```python
import json
import random


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


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
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
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

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

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

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

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
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0)

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"])


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


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

### 문제 관리 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
 M work/state.json
```

### 문제 관리 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 문제 관리 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 퀴즈 추가 삭제와 점수 메뉴 구현"
[codex/e1-2-history-rebuild baeba2e] Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
 2 files changed, 138 insertions(+), 4 deletions(-)
```

### 문제 관리 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* baeba2e (HEAD -> codex/e1-2-history-rebuild) Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
* 9a48940 Feat: 퀴즈 플레이와 점수 계산 구현
* a5d5759 Feat: state.json 저장과 복구 처리 추가
```

### 날짜/시간 포함 게임 기록 저장 확인

`main.py`

```python
import json
import random
from datetime import datetime


class Quiz:
    # 퀴즈 1개의 문제, 선택지, 정답, 힌트를 저장한다.
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 저장된 퀴즈 내용을 한 번에 출력한다.
    def show(self):
        print(self.question)
        for choice in self.choices:
            print(choice)
        print(self.answer)

    # 사용자 답이 정답 번호와 같은지 확인한다.
    def check_answer(self, user_answer):
        return self.answer == user_answer

    # 현재 퀴즈의 힌트를 출력한다.
    def show_hint(self):
        print(f"힌트: {self.hint}")


class QuizGame:
    # 게임 전체에서 퀴즈 목록, 최고 점수, 플레이 기록을 관리한다.
    def __init__(self, quizzes, best_score, score_history):
        self.quizzes = quizzes
        self.best_score = best_score
        self.score_history = score_history

    # 파일이 없을 때 사용할 기본 퀴즈 목록을 만든다.
    @staticmethod
    def make_default_quizzes():
        return [
            # 문자열 자료형을 묻는 기본 퀴즈다.
            Quiz(
                "Python에서 문자열을 저장하는 자료형은?",
                ["int", "str", "bool", "list"],
                2,
                "문자열은 따옴표로 감싸 자주 표현합니다.",
            ),
            # 불리언 결과를 만드는 비교 연산 퀴즈다.
            Quiz(
                "Python에서 3 > 1의 결과는 무엇인가?",
                ["0", "False", "True", "None"],
                3,
                "비교 연산의 결과는 참 또는 거짓입니다.",
            ),
            # 리스트 자료형을 고르는 퀴즈다.
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
                ["dict", "list", "str", "int"],
                2,
                "대괄호 [] 로 만드는 자료형을 떠올려보세요.",
            ),
            # 반복문 역할을 묻는 퀴즈다.
            Quiz(
                "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
                ["if", "for", "print", "input"],
                2,
                "반복문 문법을 고르면 됩니다.",
            ),
            # 함수 반환값 개념을 묻는 퀴즈다.
            Quiz(
                "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
                ["break", "class", "return", "import"],
                3,
                "함수 바깥으로 값을 다시 보내는 단어입니다.",
            ),
        ]

    # 메뉴 문구를 한 곳에서 출력한다.
    def show_menu(self):
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 점수 확인")
        print("6. 플레이 기록")
        print("7. 종료")

    # 메뉴 입력이 비어 있는지 먼저 검사한다.
    def is_blank_choice(self, choice):
        return choice == ""

    # 메뉴 입력이 숫자인지 검사한다.
    def is_digit_choice(self, choice):
        return choice.isdigit()

    # 메뉴 입력이 허용된 번호인지 검사한다.
    def is_valid_menu_choice(self, choice):
        return choice in ["1", "2", "3", "4", "5", "6", "7"]

    # 종료 메뉴를 선택했는지 검사한다.
    def is_exit_choice(self, choice):
        return choice == "7"

    # 출제할 퀴즈가 1개 이상 있는지 확인한다.
    def has_quizzes(self):
        return len(self.quizzes) > 0

    # 이번에 풀 문제 수를 입력받고 가능한 범위인지 확인한다.
    def ask_quiz_count(self):
        count_text = input(f"몇 문제를 풀까요? (1-{len(self.quizzes)}): ").strip()

        if count_text == "":
            print("문제 수를 입력해주세요.")
            return None

        if not count_text.isdigit():
            print("문제 수는 숫자로 입력해주세요.")
            return None

        count = int(count_text)

        if count < 1 or count > len(self.quizzes):
            print("풀 수 있는 문제 수만 입력해주세요.")
            return None

        return count

    # 저장된 퀴즈 중에서 요청한 개수만큼 랜덤하게 뽑는다.
    def pick_random_quizzes(self, count):
        return random.sample(self.quizzes, count)

    # 힌트를 볼지 입력받고, 봤다면 점수 차감 여부를 알려준다.
    def ask_hint_usage(self, quiz):
        choice = input("힌트를 볼까요? (y/n): ").strip().lower()

        if choice == "y":
            quiz.show_hint()
            print("힌트를 사용해 이 문제는 점수를 얻을 수 없습니다.")
            return True

        return False

    # 이번 플레이 점수가 더 높으면 최고 점수를 갱신한다.
    def update_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다.")

    # 이번 플레이 결과를 날짜/시간과 함께 기록 목록에 추가한다.
    def record_score_history(self, total_questions, score):
        self.score_history.append(
            {
                "played_at": datetime.now().isoformat(timespec="seconds"),
                "total_questions": total_questions,
                "score": score,
            }
        )

    # 저장된 모든 퀴즈를 순서대로 출제하고 맞은 개수를 센다.
    def play_all_quizzes(self):
        if not self.has_quizzes():
            print("등록된 퀴즈가 없어 퀴즈를 시작할 수 없습니다.")
            return

        count = self.ask_quiz_count()
        if count is None:
            return

        # 사용자가 고른 개수만큼 문제를 섞어서 이번 라운드를 만든다.
        selected_quizzes = self.pick_random_quizzes(count)
        score = 0

        print(f"{count}문제를 랜덤으로 출제합니다.")

        for quiz in selected_quizzes:
            quiz.show()
            used_hint = self.ask_hint_usage(quiz)
            answer = int(input("정답 번호: ").strip())

            if quiz.check_answer(answer):
                if used_hint:
                    print("정답이지만 힌트를 사용해 점수는 올라가지 않습니다.")
                else:
                    print("정답입니다.")
                    score += 1
                continue

            print("오답입니다.")

        self.record_score_history(count, score)
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

    # 저장된 플레이 기록을 최근 순서대로 출력한다.
    def show_score_history(self):
        if len(self.score_history) == 0:
            print("아직 저장된 플레이 기록이 없습니다.")
            return

        print("플레이 기록")
        for number, history in enumerate(self.score_history, start=1):
            print(
                f"{number}. {history['played_at']} | "
                f"{history['total_questions']}문제 | "
                f"{history['score']}점"
            )

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

            if choice == "6":
                self.show_score_history()
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
                    "hint": quiz.hint,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
            "score_history": self.score_history,
        }

    # 현재 게임 상태를 state.json 파일에 저장한다.
    def save_to_file(self):
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 파일을 쓰는 중 오류가 발생했습니다.")

    # state.json 파일에서 게임 상태를 읽어 객체로 복원한다.
    @classmethod
    def load_from_file(cls):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0, [])
        except json.JSONDecodeError:
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            return cls(cls.make_default_quizzes(), 0, [])
        except OSError:
            print("저장 파일을 읽는 중 오류가 발생해 기본 퀴즈로 시작합니다.")
            return cls(cls.make_default_quizzes(), 0, [])

        quizzes = [
            Quiz(
                item["question"],
                item["choices"],
                item["answer"],
                item.get("hint", "아직 등록된 힌트가 없습니다."),
            )
            for item in data["quizzes"]
        ]
        return cls(quizzes, data["best_score"], data.get("score_history", []))


def main():
    game = None

    try:
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
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
        if game is not None:
            game.save_to_file()


main()
```

### 날짜/시간 포함 게임 기록 저장 확인

```bash
$ printf '1\n1\nn\n2\n6\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x1086a17f0>, <__main__.Quiz object at 0x103c99f90>, <__main__.Quiz object at 0x103c9b750>, <__main__.Quiz object at 0x108668770>, <__main__.Quiz object at 0x10866ab10>]
0
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 0, 'score_history': []}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 0, 'score_history': []}
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
선택: 몇 문제를 풀까요? (1-5): 1문제를 랜덤으로 출제합니다.
같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?
if
for
print
input
2
힌트를 볼까요? (y/n): 정답 번호: 정답입니다.
최고 점수가 갱신되었습니다.
이번 점수: 1
현재 최고 점수: 1
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 종료
선택: 프로그램을 종료합니다.
```

### 날짜/시간 포함 게임 기록 저장 확인

```bash
$ python3 -m json.tool state.json
{
    "quizzes": [
        {
            "question": "Python에서 문자열을 저장하는 자료형은?",
            "choices": [
                "int",
                "str",
                "bool",
                "list"
            ],
            "answer": 2,
            "hint": "문자열은 따옴표로 감싸 자주 표현합니다."
        },
        {
            "question": "Python에서 3 > 1의 결과는 무엇인가?",
            "choices": [
                "0",
                "False",
                "True",
                "None"
            ],
            "answer": 3,
            "hint": "비교 연산의 결과는 참 또는 거짓입니다."
        },
        {
            "question": "여러 값을 순서대로 저장하는 자료형은 무엇인가?",
            "choices": [
                "dict",
                "list",
                "str",
                "int"
            ],
            "answer": 2,
            "hint": "대괄호 [] 로 만드는 자료형을 떠올려보세요."
        },
        {
            "question": "같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?",
            "choices": [
                "if",
                "for",
                "print",
                "input"
            ],
            "answer": 2,
            "hint": "반복문 문법을 고르면 됩니다."
        },
        {
            "question": "함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?",
            "choices": [
                "break",
                "class",
                "return",
                "import"
            ],
            "answer": 3,
            "hint": "함수 바깥으로 값을 다시 보내는 단어입니다."
        }
    ],
    "best_score": 1,
    "score_history": [
        {
            "played_at": "2026-08-06T19:55:55",
            "total_questions": 1,
            "score": 1
        }
    ]
}
```

### 날짜/시간 포함 게임 기록 저장 확인

```bash
$ printf '6\n7\n' | python3 main.py
퀴즈 게임 시작
[<__main__.Quiz object at 0x1083a17f0>, <__main__.Quiz object at 0x103971f90>, <__main__.Quiz object at 0x103973750>, <__main__.Quiz object at 0x1083688a0>, <__main__.Quiz object at 0x10836ac40>]
1
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 1, 'score_history': [{'played_at': '2026-08-06T19:55:55', 'total_questions': 1, 'score': 1}]}
{'quizzes': [{'question': 'Python에서 문자열을 저장하는 자료형은?', 'choices': ['int', 'str', 'bool', 'list'], 'answer': 2, 'hint': '문자열은 따옴표로 감싸 자주 표현합니다.'}, {'question': 'Python에서 3 > 1의 결과는 무엇인가?', 'choices': ['0', 'False', 'True', 'None'], 'answer': 3, 'hint': '비교 연산의 결과는 참 또는 거짓입니다.'}, {'question': '여러 값을 순서대로 저장하는 자료형은 무엇인가?', 'choices': ['dict', 'list', 'str', 'int'], 'answer': 2, 'hint': '대괄호 [] 로 만드는 자료형을 떠올려보세요.'}, {'question': '같은 동작을 여러 번 반복할 때 주로 사용하는 문법은?', 'choices': ['if', 'for', 'print', 'input'], 'answer': 2, 'hint': '반복문 문법을 고르면 됩니다.'}, {'question': '함수 실행 뒤 결과 값을 돌려줄 때 사용하는 키워드는?', 'choices': ['break', 'class', 'return', 'import'], 'answer': 3, 'hint': '함수 바깥으로 값을 다시 보내는 단어입니다.'}], 'best_score': 1, 'score_history': [{'played_at': '2026-08-06T19:55:55', 'total_questions': 1, 'score': 1}]}
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
6. 플레이 기록
7. 종료
선택: 플레이 기록
1. 2026-08-06T19:55:55 | 1문제 | 1점
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 퀴즈 삭제
5. 점수 확인
6. 플레이 기록
7. 종료
선택: 프로그램을 종료합니다.
```

### 플레이 기록 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 status --short
 M work/main.py
 M work/state.json
```

### 플레이 기록 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 add -A
```

### 플레이 기록 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 commit -m "Feat: 플레이 기록 저장 기능 추가"
[codex/e1-2-history-rebuild 9d2cee1] Feat: 플레이 기록 저장 기능 추가
 2 files changed, 47 insertions(+), 10 deletions(-)
```

### 플레이 기록 기능 완성 후 commit 기록

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 log --oneline --graph --decorate -n 3
* 9d2cee1 (HEAD -> codex/e1-2-history-rebuild) Feat: 플레이 기록 저장 기능 추가
* 599708f Feat: 랜덤 출제와 힌트 기능 추가
* baeba2e Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
```


## Chapter 7. README, Git 로그, clone/pull 제출 증거

### 테마

- README 필수 항목 작성
- git log --oneline --graph와 커밋 수 확인
- GitHub 저장소 연결과 업로드 확인
- 별도 디렉터리에 clone
- clone 변경 push 후 원래 작업 폴더에서 pull
- 개발 환경과 실행 화면 증거 정리

### README 필수 항목 작성

```bash
$ sed -n '1,80p' README.md
# E1-2 파이썬 이해하기

## 프로젝트 개요

터미널에서 실행하는 Python 퀴즈 게임입니다.  
메뉴를 통해 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록 확인, 퀴즈 삭제, 최고 점수 확인, 플레이 기록 확인을 수행할 수 있습니다.

## 퀴즈 주제 선정 이유

Python 기초 문법을 배우는 과제이기 때문에, 퀴즈 주제도 Python 기본 개념으로 맞췄습니다.  
문자열, 불리언, 리스트, 반복문, 반환값처럼 과제에서 직접 설명해야 하는 개념을 퀴즈 문제로 다시 확인할 수 있게 구성했습니다.

## 실행 방법

과제 작업 루트에서 아래 명령으로 실행합니다.

```bash
cd /Users/hskim/Projects/codyssey/artifacts/e1-2/work
python3 main.py
```

## 기능 목록

- 메뉴 출력과 종료
- 빈 입력, 문자 입력, 범위 밖 숫자 입력 예외 처리
- `Quiz` 클래스 기반 개별 퀴즈 표현
- `QuizGame` 클래스 기반 전체 게임 관리
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 보기
- 퀴즈 삭제
- 최고 점수 확인
- 플레이 기록 저장과 조회
- `state.json` 저장/복구
- 랜덤 출제
- 문제 수 선택
- 힌트 사용과 점수 차감

## 파일 구조

```text
artifacts/e1-2/
├── README.md
├── state.json
├── logs/
│   └── practice.jsonl
├── render/
│   └── latest/
│       ├── README.md
│       └── presentation.html
└── work/
    ├── main.py
    └── state.json
```

## 데이터 파일 설명

이 과제의 실행 데이터는 기본적으로 `artifacts/e1-2/work/state.json`에 UTF-8로 저장됩니다.

주요 필드는 다음과 같습니다.

- `quizzes`: 문제, 선택지, 정답, 힌트 목록
- `best_score`: 현재 최고 점수
- `score_history`: 날짜/시간, 푼 문제 수, 점수 기록 배열
```

### README 필수 항목 작성

```bash
$ rg -n '^## ' README.md
3:## 프로젝트 개요
8:## 퀴즈 주제 선정 이유
13:## 실행 방법
22:## 기능 목록
39:## 파일 구조
56:## 데이터 파일 설명
```

### git log --oneline --graph와 커밋 수 확인

```bash
$ git rev-list --count --all
12
```

### git log --oneline --graph와 커밋 수 확인

```bash
$ git log --oneline --graph --decorate --all --max-count=20
* a12d1b7 (HEAD -> main, origin/main) Docs: clone 저장소 검증 메모 추가
*   302870a Merge branch 'codex/e1-2-readme-evidence'
|\  
| * 443cb6f (codex/e1-2-readme-evidence) Docs: README와 제출 증거 정리
|/  
* 15a283c Feat: 퀴즈 게임 기본 구조와 저장 흐름 구현
* 9d2cee1 (codex/e1-2-history-rebuild) Feat: 플레이 기록 저장 기능 추가
* 599708f Feat: 랜덤 출제와 힌트 기능 추가
* baeba2e Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
* 9a48940 Feat: 퀴즈 플레이와 점수 계산 구현
* a5d5759 Feat: state.json 저장과 복구 처리 추가
* 054e3c8 Refactor: QuizGame으로 메뉴 책임 분리
* 7e2694f Feat: Quiz 클래스와 정답 판정 구현
* bfc04cf Feat: 반복 메뉴와 종료 흐름 구현
```

### GitHub 저장소 연결과 업로드 확인

```bash
$ git remote -v
origin	/private/tmp/e1-2-remote-cuFnUC.git (fetch)
origin	/private/tmp/e1-2-remote-cuFnUC.git (push)
```

### GitHub 저장소 연결과 업로드 확인

```bash
$ gh auth status
github.com
  X Failed to log in to github.com account Logan-kim-the-philosopher (default)
  - Active account: true
  - The token in default is invalid.
  - To re-authenticate, run: gh auth login -h github.com
  - To forget about this account, run: gh auth logout -h github.com -u Logan-kim-the-philosopher
```

### 별도 디렉터리에 clone

```bash
$ git clone /private/tmp/e1-2-remote-cuFnUC.git /private/tmp/e1-2-clone-BOihMa
Cloning into '/private/tmp/e1-2-clone-BOihMa'...
done.
```

### 별도 디렉터리에 clone

```bash
$ git -C /private/tmp/e1-2-clone-BOihMa remote -v
origin	/private/tmp/e1-2-remote-cuFnUC.git (fetch)
origin	/private/tmp/e1-2-remote-cuFnUC.git (push)
```

### clone 변경 push 후 원래 작업 폴더에서 pull

```bash
$ git -C /private/tmp/e1-2-clone-BOihMa commit -m "Docs: clone 저장소 검증 메모 추가" && git -C /private/tmp/e1-2-clone-BOihMa push origin main
[main a12d1b7] Docs: clone 저장소 검증 메모 추가
 1 file changed, 2 insertions(+)
To /private/tmp/e1-2-remote-cuFnUC.git
   302870a..a12d1b7  main -> main
```

### clone 변경 push 후 원래 작업 폴더에서 pull

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 pull origin main
From /private/tmp/e1-2-remote-cuFnUC
 * branch            main       -> FETCH_HEAD
   302870a..a12d1b7  main       -> origin/main
Updating 302870a..a12d1b7
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

### clone 변경 push 후 원래 작업 폴더에서 pull

```bash
$ rg -n "clone 저장소" README.md
89:- clone 저장소에서 2026-08-06 pull 실습 메모를 추가했습니다.
```

### 개발 환경과 실행 화면 증거 정리

```bash
$ python3 --version
Python 3.14.6
```

### 개발 환경과 실행 화면 증거 정리

```bash
$ git --version
git version 2.55.0
```

### 개발 환경과 실행 화면 증거 정리

```bash
$ cd /Users/hskim/Projects/codyssey/artifacts/e1-2/work && pwd && ls -la
/Users/hskim/Projects/codyssey/artifacts/e1-2/work
total 64
drwxr-xr-x@ 8 hskim  staff    256 Aug  6 20:05 .
drwxr-xr-x@ 9 hskim  staff    288 Aug  6 22:17 ..
drwxr-xr-x@ 3 hskim  staff     96 Aug  6 20:05 __pycache__
-rw-r--r--@ 1 hskim  staff  14378 Aug  6 20:00 main.py
-rw-r--r--@ 1 hskim  staff    234 Aug  6 15:16 state.before-5-quizzes.json
-rw-r--r--@ 1 hskim  staff   1550 Aug  6 20:01 state.json
-rw-r--r--@ 1 hskim  staff   1066 Aug  6 18:54 state.json.bak
-rw-r--r--@ 1 hskim  staff   1356 Aug  6 19:39 state.pre_hint_backup.json
```

### 증빙

- artifacts/e1-2/README.md
### 증빙

- artifacts/e1-2/README.md
```

### README 필수 항목 작성

```bash
$ ls -la README.md
-rw-r--r--@ 1 hskim  staff  397412 Aug  6 22:21 /Users/hskim/Projects/codyssey/artifacts/e1-2/README.md
```

### git log --oneline --graph와 커밋 수 확인

```bash
$ git rev-list --count --all
12
```

### git log --oneline --graph와 커밋 수 확인

```bash
$ git log --oneline --graph --decorate --all --max-count=20
* a12d1b7 (HEAD -> main, origin/main) Docs: clone 저장소 검증 메모 추가
*   302870a Merge branch 'codex/e1-2-readme-evidence'
|\  
| * 443cb6f (codex/e1-2-readme-evidence) Docs: README와 제출 증거 정리
|/  
* 15a283c Feat: 퀴즈 게임 기본 구조와 저장 흐름 구현
* 9d2cee1 (codex/e1-2-history-rebuild) Feat: 플레이 기록 저장 기능 추가
* 599708f Feat: 랜덤 출제와 힌트 기능 추가
* baeba2e Feat: 퀴즈 추가 삭제와 점수 메뉴 구현
* 9a48940 Feat: 퀴즈 플레이와 점수 계산 구현
* a5d5759 Feat: state.json 저장과 복구 처리 추가
* 054e3c8 Refactor: QuizGame으로 메뉴 책임 분리
* 7e2694f Feat: Quiz 클래스와 정답 판정 구현
* bfc04cf Feat: 반복 메뉴와 종료 흐름 구현
```

### GitHub 저장소 연결과 업로드 확인

```bash
$ git remote -v
origin	/private/tmp/e1-2-remote-cuFnUC.git (fetch)
origin	/private/tmp/e1-2-remote-cuFnUC.git (push)
```

### GitHub 저장소 연결과 업로드 확인

```bash
$ gh auth status
github.com
  X Failed to log in to github.com account Logan-kim-the-philosopher (default)
  - Active account: true
  - The token in default is invalid.
  - To re-authenticate, run: gh auth login -h github.com
  - To forget about this account, run: gh auth logout -h github.com -u Logan-kim-the-philosopher
```

### 별도 디렉터리에 clone

```bash
$ git clone /private/tmp/e1-2-remote-cuFnUC.git /private/tmp/e1-2-clone-BOihMa
Cloning into '/private/tmp/e1-2-clone-BOihMa'...
done.
```

### 별도 디렉터리에 clone

```bash
$ git -C /private/tmp/e1-2-clone-BOihMa remote -v
origin	/private/tmp/e1-2-remote-cuFnUC.git (fetch)
origin	/private/tmp/e1-2-remote-cuFnUC.git (push)
```

### clone 변경 push 후 원래 작업 폴더에서 pull

```bash
$ git -C /private/tmp/e1-2-clone-BOihMa commit -m "Docs: clone 저장소 검증 메모 추가" && git -C /private/tmp/e1-2-clone-BOihMa push origin main
[main a12d1b7] Docs: clone 저장소 검증 메모 추가
 1 file changed, 2 insertions(+)
To /private/tmp/e1-2-remote-cuFnUC.git
   302870a..a12d1b7  main -> main
```

### clone 변경 push 후 원래 작업 폴더에서 pull

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 pull origin main
From /private/tmp/e1-2-remote-cuFnUC
 * branch            main       -> FETCH_HEAD
   302870a..a12d1b7  main       -> origin/main
Updating 302870a..a12d1b7
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

### clone 변경 push 후 원래 작업 폴더에서 pull

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 diff HEAD~1 HEAD -- README.md
diff --git a/README.md b/README.md
index 027d04d..beacb8d 100644
--- a/README.md
+++ b/README.md
@@ -85,3 +85,5 @@ artifacts/e1-2/
   ]
 }
 ```
+
+- clone 저장소에서 2026-08-06 pull 실습 메모를 추가했습니다.
```

### 개발 환경과 실행 화면 증거 정리

```bash
$ python3 --version
Python 3.14.6
```

### 개발 환경과 실행 화면 증거 정리

```bash
$ git --version
git version 2.55.0
```

### 개발 환경과 실행 화면 증거 정리

```bash
$ cd /Users/hskim/Projects/codyssey/artifacts/e1-2/work && pwd && ls -la
/Users/hskim/Projects/codyssey/artifacts/e1-2/work
total 64
drwxr-xr-x@ 8 hskim  staff    256 Aug  6 20:05 .
drwxr-xr-x@ 9 hskim  staff    288 Aug  6 22:17 ..
drwxr-xr-x@ 3 hskim  staff     96 Aug  6 20:05 __pycache__
-rw-r--r--@ 1 hskim  staff  14378 Aug  6 20:00 main.py
-rw-r--r--@ 1 hskim  staff    234 Aug  6 15:16 state.before-5-quizzes.json
-rw-r--r--@ 1 hskim  staff   1550 Aug  6 20:01 state.json
-rw-r--r--@ 1 hskim  staff   1066 Aug  6 18:54 state.json.bak
-rw-r--r--@ 1 hskim  staff   1356 Aug  6 19:39 state.pre_hint_backup.json
```

### GitHub 저장소 연결과 업로드 확인

```bash
$ git -C /Users/hskim/Projects/codyssey/artifacts/e1-2 push origin main:e1-2-submission codex/e1-2-history-rebuild:e1-2-history-rebuild codex/e1-2-readme-evidence:e1-2-readme-evidence
Everything up-to-date
```

### GitHub 저장소 연결과 업로드 확인

```bash
$ git -C /Users/hskim/Projects/codyssey push origin main
To github.com:Logan-kim-the-philosopher/codyssey.git
   2a39fe5..c061820  main -> main
```

### GitHub 저장소 연결과 업로드 확인

```bash
$ gh api repos/Logan-kim-the-philosopher/codyssey/pages
{"url":"https://api.github.com/repos/Logan-kim-the-philosopher/codyssey/pages","status":"building","cname":null,"custom_404":false,"html_url":"https://logan-kim-the-philosopher.github.io/codyssey/","build_type":"legacy","source":{"branch":"main","path":"/docs"},"public":true,"protected_domain_state":null,"pending_domain_unverified_at":null,"https_enforced":true}
```

### 증빙

- artifacts/e1-2/README.md
### 증빙

- artifacts/e1-2/README.md
