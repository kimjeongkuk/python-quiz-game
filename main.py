print("hello,world")
# 1. 질문 설계도 만들기
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt  # 질문 내용
        self.answer = answer  # 정답

# 2. 문제 리스트 만들기
question_prompts = [
    "파이썬의 확장자는 무엇인가요?\n(a) .py\n(b) .js\n\n",
    "파이썬을 만든 사람은?\n(a) 귀도 반 로섬\n(b) 빌 게이츠\n\n"
]

# 3. 실제 문제 객체 생성
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a")
]

print(f"총 {len(questions)}개의 문제가 준비되었습니다.")
def run_quiz(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt) # 사용자에게 질문 던지기
        if answer == q.answer:   # 정답 비교
            print("정답입니다! 🎉")
            score += 1
        else:
            print("아쉽네요, 틀렸습니다. 😢")
    
    print(f"\n당신의 점수는 {len(questions)}점 만점에 {score}점입니다!")

# 함수 실행하기
run_quiz(questions)
# 기존의 run_quiz(questions) 코드를 지우고 아래 내용을 넣으세요.

def main_menu():
    while True:
        print("\n--- 파이썬 퀴즈 게임 ---")
        print("1. 게임 시작")
        print("2. 종료")
        
        choice = input("번호를 선택하세요: ")
        
        if choice == "1":
            run_quiz(questions)
        elif choice == "2":
            print("게임을 종료합니다. 다음에 또 봐요! 👋")
            break
        else:
            print("잘못된 입력입니다. 1번이나 2번을 눌러주세요.")

# 프로그램 시작점
if __name__ == "__main__":
    main_menu()
    class Question:
        def __init__(self, prompt, answer):
            self.prompt = prompt
            self.answer = answer

# 1. 문제 추가 (3개 더 추가해서 총 5문제)
question_prompts = [
    "1. 사과는 무슨 색인가요?\n(a) 빨강\n(b) 보라\n\n",
    "2. 바나나는 무슨 색인가요?\n(a) 초록\n(b) 노랑\n\n",
    "3. 파이썬에서 화면에 글자를 출력하는 함수는?\n(a) input\n(b) print\n\n",
    "4. 파이썬 파일의 확장자는?\n(a) .py\n(b) .txt\n\n",
    "5. 리스트의 길이를 잴 때 사용하는 함수는?\n(a) len\n(b) size\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print("정답입니다! ✨")
            score += 1
        else:
            # 2. 오답 확인 기능 추가
            print(f"아쉽네요. 틀렸습니다. (정답: {question.answer}) ❌")
    
    # 3. 점수 등급 나누기 기능 추가
    print(f"\n--- 결과 ---")
    print(f"당신의 점수는 {len(questions)}점 만점에 {score}점입니다!")
    
    if score == len(questions):
        print("등급: 파이썬 천재 🏆")
    elif score >= 3:
        print("등급: 고수 👍")
    else:
        print("등급: 공부가 필요해요 📖")

def main_menu():
    while True:
        print("\n=== 파이썬 퀴즈 게임 v2.0 ===")
        print("1. 게임 시작")
        print("2. 종료")
        
        choice = input("번호를 선택하세요: ")
        
        if choice == "1":
            run_quiz(questions)
        elif choice == "2":
            print("게임을 종료합니다. 즐거웠어요! 👋")
            break
        else:
            print("잘못된 입력입니다. 1번이나 2번을 눌러주세요.")

if __name__ == "__main__":
    main_menu()

    import random  # 문제를 섞기 위해 필요해요

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# 문제 목록
question_prompts = [
    "1. 사과는 무슨 색인가요?\n(a) 빨강\n(b) 보라\n\n",
    "2. 바나나는 무슨 색인가요?\n(a) 초록\n(b) 노랑\n\n",
    "3. 파이썬에서 화면에 글자를 출력하는 함수는?\n(a) input\n(b) print\n\n",
    "4. 파이썬 파일의 확장자는?\n(a) .py\n(b) .txt\n\n",
    "5. 리스트의 길이를 잴 때 사용하는 함수는?\n(a) len\n(b) size\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
]

def run_quiz(questions):
    # [추가] 문제 순서 섞기
    random.shuffle(questions)
    
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print("정답입니다! ✨")
            score += 1
        else:
            print(f"아쉽네요. 틀렸습니다. (정답: {question.answer}) ❌")
    
    print(f"\n당신의 점수는 {len(questions)}점 만점에 {score}점입니다!")
    
    # [추가] 최고 점수 확인 및 저장
    save_high_score(score)

def save_high_score(current_score):
    try:
        # 기존 최고 점수 읽어오기
        with open("highscore.txt", "r") as f:
            high_score = int(f.read())
    except FileNotFoundError:
        # 파일이 없으면 0점으로 시작
        high_score = 0

    if current_score > high_score:
        print(f"🎊 축하합니다! 새로운 최고 기록입니다: {current_score}점")
        with open("highscore.txt", "w") as f:
            f.write(str(current_score))
    else:
        print(f"현재 최고 기록은 {high_score}점입니다. 더 힘내세요!")

def main_menu():
    while True:
        print("\n=== 파이썬 퀴즈 게임 v3.0 ===")
        print("1. 게임 시작")
        print("2. 종료")
        
        choice = input("번호를 선택하세요: ")
        
        if choice == "1":
            run_quiz(questions)
        elif choice == "2":
            print("게임을 종료합니다. 즐거웠어요! 👋")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main_menu()
