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
