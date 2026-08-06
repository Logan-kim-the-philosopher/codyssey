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
