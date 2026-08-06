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
