import random
from data import questions

def get_grade(score, total):
    """점수에 따른 등급 메시지를 반환합니다."""
    percentage = (score / total) * 100
    
    if percentage == 100:
        return "천재! 만점입니다! 🏆"
    elif percentage >= 70:
        return "정말 잘하시네요! 👍"
    elif percentage >= 40:
        return "나쁘지 않아요! 😊"
    else:
        return "조금 더 공부하면 좋을 것 같아요! 📚"

def run_quiz(questions_list):
    score = 0
    # 매 게임마다 문제 순서를 섞어줍니다.
    random.shuffle(questions_list)
    
    print("\n" + "="*30)
    print("   🌟 퀴즈 게임을 시작합니다! 🌟")
    print("="*30)
    
    for i, q in enumerate(questions_list):
        print(f"\n{i+1}번 문제:")
        answer = input(q.prompt)
        
        if answer.lower() == q.answer:
            print("정답입니다! ✨")
            score += 1
        else:
            print(f"아쉽네요. 틀렸습니다. (정답: {q.answer})")
        
    # 결과 출력
    total = len(questions_list)
    print("\n" + "="*30)
    print(f"게임 종료! 당신의 점수는 {score}/{total}점입니다.")
    print(f"평가: {get_grade(score, total)}")
    print("="*30 + "\n")

if __name__ == "__main__":
    while True:
        run_quiz(questions)
        
        # 다시 시작 여부 묻기
        play_again = input("게임을 다시 하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            print("\n게임을 이용해 주셔서 감사합니다. 안녕히 가세요! 👋")
            break