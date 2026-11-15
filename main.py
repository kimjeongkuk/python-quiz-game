import json
import os

# 1. 개별 퀴즈를 담당하는 클래스
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = int(answer)

    def display(self, index):
        print(f"\n[문제 {index}]")
        print(self.question)
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return self.answer == user_answer

    # 데이터를 저장하기 위해 딕셔너리 형태로 변환
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

# 2. 게임 전체 로직을 관리하는 클래스
class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.file_path = "state.json"
        self.load_data()

    # 파일에서 데이터 불러오기
    def load_data(self):
        if not os.path.exists(self.file_path):
            self.set_default_quizzes()
            return

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
            print(f"\n📂 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
        except (json.JSONDecodeError, Exception):
            print("\n⚠️ 파일이 손상되어 기본 데이터를 로드합니다.")
            self.set_default_quizzes()

    # 기본 퀴즈 설정 (파일이 없을 때)
    def set_default_quizzes(self):
        default_data = [
            ["파이썬의 창시자는?", ["귀도 반 로섬", "제임스 고슬링", "데니스 리치", "빌 게이츠"], 1],
            ["파이썬에서 리스트에 요소를 추가하는 함수는?", ["add()", "push()", "append()", "insert_at()"], 3],
            ["JSON의 약자는?", ["Java Simple Object Notation", "JavaScript Object Notation", "Just Simple Object Notation", "Jupyter Standard Object Notation"], 2],
            ["Git에서 변경사항을 저장소에 기록하는 명령은?", ["git push", "git commit", "git add", "git pull"], 2],
            ["다음 중 프로그래밍 언어가 아닌 것은?", ["Python", "Java", "HTML", "C++"], 3]
        ]
        self.quizzes = [Quiz(q, c, a) for q, c, a in default_data]
        self.save_data()

    # 파일에 데이터 저장
    def save_data(self):
        data = {
            "best_score": self.best_score,
            "quizzes": [q.to_dict() for q in self.quizzes]
        }
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # 안전한 숫자 입력 받기
    def get_safe_input(self, prompt, min_val, max_val):
        while True:
            try:
                user_input = input(prompt).strip()
                if not user_input:
                    print("⚠️ 입력값이 비어있습니다.")
                    continue
                val = int(user_input)
                if min_val <= val <= max_val:
                    return val
                else:
                    print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("⚠️ 숫자를 입력해주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n\n👋 프로그램을 안전하게 종료합니다.")
                self.save_data()
                exit()

    # 퀴즈 풀기
    def play(self):
        if not self.quizzes:
            print("📋 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)
            user_ans = self.get_safe_input("정답 입력: ", 1, 4)
            if quiz.is_correct(user_ans):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

        final_score = int((score / len(self.quizzes)) * 100)
        print(f"\n🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답! ({final_score}점)")

        if final_score > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = final_score
            self.save_data()

    # 퀴즈 추가
    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()
        choices = []
        for i in range(1, 5):
            choices.append(input(f"선택지 {i}: ").strip())
        answer = self.get_safe_input("정답 번호 (1-4): ", 1, 4)
        
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("✅ 퀴즈가 추가되었습니다!")

    # 목록 보기
    def list_quizzes(self):
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)

    # 메뉴 출력
    def run(self):
        while True:
            print("\n" + "="*40)
            print("        🎯 나만의 퀴즈 게임 🎯")
            print("="*40)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("="*40)
            
            choice = self.get_safe_input("선택: ", 1, 5)
            
            if choice == 1: self.play()
            elif choice == 2: self.add_quiz()
            elif choice == 3: self.list_quizzes()
            elif choice == 4: print(f"\n🏆 최고 점수: {self.best_score}점")
            elif choice == 5:
                print("👋 게임을 종료합니다.")
                break

if __name__ == "__main__":
    game = QuizGame()
    game.run()