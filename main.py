# main.py
import time
from data import question_data
from models import Question

# --- 기능 함수들 ---

def load_high_score():
    """파일에서 최고 점수를 읽어옵니다."""
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(score):
    """파일에 최고 점수를 저장합니다."""
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def start_quiz():
    high_score = load_high_score()
    print(f"🏆 현재 최고 점수: {high_score}점")
    
    # 1. 난이도 선택 및 필터링
    choice = input("난이도를 선택하세요 (easy, normal, hard): ").lower()
    
    # 리스트 컴프리헨션으로 선택한 난이도 문제만 객체로 만듦
    question_bank = [
        Question(q["text"], q["answer"], q["difficulty"]) 
        for q in question_data if q["difficulty"] == choice
    ]

    if not question_bank:
        print("해당 난이도의 문제가 없습니다. 다시 실행해 주세요.")
        return

    score = 0
    time_limit = 5 # 제한 시간 5초

    # 2. 게임 루프
    for i, question in enumerate(question_bank):
        print(f"\nQ{i+1}. {question.text}")
        
        start_time = time.time() # 시간 측정 시작
        user_answer = input(f"정답(O/X) 입력 [제한시간 {time_limit}초]: ").upper()
        end_time = time.time()   # 시간 측정 종료
        
        taken_time = end_time - start_time

        # 3. 타임어택 체크
        if taken_time > time_limit:
            print(f"⏰ 시간 초과! ({taken_time:.2f}초 소요) 오답 처리됩니다.")
            continue

        # 4. 정답 체크
        if user_answer == question.answer:
            print(f"✅ 정답입니다! ({taken_time:.2f}초 소요)")
            score += 1
        else:
            print(f"❌ 틀렸습니다! (소요 시간: {taken_time:.2f}초)")

    # 3. 결과 발표 및 최고 점수 저장
    print(f"\n--- 게임 종료 ---")
    print(f"최종 점수: {score} / {len(question_bank)}")

    if score > high_score:
        print("🎊 축하합니다! 최고 점수를 경신했습니다!")
        save_high_score(score)
    else:
        print(f"최고 점수({high_score}점) 경신에 실패했습니다. 다음 기회에!")

# 게임 실행
if __name__ == "__main__":
    while True:
        start_quiz()
        if input("\n다시 하시겠습니까? (Y/N): ").upper() != "Y":
            print("게임을 종료합니다. 감사합니다!")
            break