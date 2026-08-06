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
