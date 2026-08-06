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
