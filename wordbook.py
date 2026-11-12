import json
import random
import os

# 파일 경로 설정
FILE_PATH = "wordbook.json"

# 단어장 불러오기
def load_wordbook():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# 단어장 저장하기
def save_wordbook(wordbook):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(wordbook, f, ensure_ascii=False, indent=4)

# 1. 단어 추가
def add_word(wordbook):
    word = input("추가할 영단어를 입력하세요: ").strip()
    mean = input(f"'{word}'의 뜻을 입력하세요: ").strip()
    wordbook[word] = mean
    save_wordbook(wordbook)
    print(f"'{word}' 단어가 추가되었습니다.")

# 2. 단어 목록 보기
def show_list(wordbook):
    if not wordbook:
        print("\n단어장이 비어 있습니다.")
        return
    print("\n--- 단어 목록 ---")
    for word, mean in wordbook.items():
        print(f"{word} : {mean}")

# 3. 단어 검색
def search_word(wordbook):
    word = input("검색할 단어를 입력하세요: ").strip()
    if word in wordbook:
        print(f"결과: {word} - {wordbook[word]}")
    else:
        print("찾는 단어가 없습니다.")

# 4. 단어 삭제
def delete_word(wordbook):
    word = input("삭제할 단어를 입력하세요: ").strip()
    if word in wordbook:
        del wordbook[word]
        save_wordbook(wordbook)
        print(f"'{word}' 단어가 삭제되었습니다.")
    else:
        print("삭제할 단어가 없습니다.")

# 5. [업데이트된 기능] 퀴즈 실행 (3문제 연속 풀기)
def run_quiz(wordbook):
    if len(wordbook) < 3:
        print("\n[알림] 퀴즈를 진행하려면 단어가 최소 3개 이상 필요합니다.")
        return

    print(f"\n--- 챌린지 퀴즈 시작! (총 3문제) ---")
    score = 0
    
    # 무작위로 3개 추출
    quiz_samples = random.sample(list(wordbook.items()), 3)

    for i, (word, mean) in enumerate(quiz_samples, 1):
        print(f"\n[{i}번 문제] '{word}'의 뜻은 무엇일까요?")
        answer = input("답변: ").strip()

        if answer == mean:
            print("정답입니다! ✨")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 '{mean}'입니다. 😅")

    print(f"\n--- 퀴즈 종료 ---")
    print(f"결과: 3문제 중 {score}문제를 맞혔습니다!")
    
    if score == 3:
        print("와우! 완벽해요! 💯")
    elif score >= 1:
        print("잘하셨어요! 조금만 더 힘내세요! 💪")
    else:
        print("다시 한번 복습해볼까요? 열공! 🔥")

# 메인 메뉴
def main():
    wordbook = load_wordbook()
    
    while True:
        print("\n--- 영단어장 프로그램 ---")
        print("1. 단어 추가")
        print("2. 단어 목록")
        print("3. 단어 검색")
        print("4. 단어 삭제")
        print("5. 퀴즈 풀기")
        print("6. 종료")
        
        choice = input("원하는 메뉴 번호를 선택하세요: ")
        
        if choice == '1':
            add_word(wordbook)
        elif choice == '2':
            show_list(wordbook)
        elif choice == '3':
            search_word(wordbook)
        elif choice == '4':
            delete_word(wordbook)
        elif choice == '5':
            run_quiz(wordbook)
        elif choice == '6':
            print("프로그램을 종료합니다. 열공하세요!")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()