import json
import os

class QuizSystem:
    def __init__(self):
        self.quiz_file = 'quizzes.json'
        self.wrong_file = 'wrong_answers.json'
        self.score_file = 'scores.json'
        
        self.quizzes = self.load_json(self.quiz_file)
        self.score_history = self.load_json(self.score_file)

    def load_json(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_json(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def run_quiz(self):
        if not self.quizzes:
            print("\n[알림] 등록된 퀴즈가 없습니다. 2번 메뉴에서 추가해주세요.")
            return

        score = 0
        wrong_data = self.load_json(self.wrong_file)
        
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\nQ{i}. {quiz['question']}")
            
            # Print options with numbers
            for number, opt in enumerate(quiz['options']):
                print(f"{number + 1}. {opt}")
            
            ans = input("정답 번호 입력 (1~4): ").strip()
            
            if str(ans) == str(quiz['answer']):
                print(">> 정답입니다!")
                score += 1
                # Remove from wrong answers if answered correctly
                wrong_data = [q for q in wrong_data if q['question'] != quiz['question']]
            else:
                print(f">> 오답! 정답은 {quiz['answer']}번입니다.")
                # Add to wrong answers avoiding duplicates
                if not any(q['question'] == quiz['question'] for q in wrong_data):
                    wrong_data.append(quiz)

        self.save_json(self.wrong_file, wrong_data)
        final_score = (score / len(self.quizzes)) * 100
        self.score_history.append(f"{final_score:.1f}점")
        self.save_json(self.score_file, self.score_history)
        
        print(f"\n[결과] {len(self.quizzes)}문제 중 {score}문제 정답! ({final_score:.1f}점)")

    def add_quiz(self):
        print("\n--- 새 퀴즈 추가 ---")
        question = input("질문 내용: ").strip()
        if not question:
            print("오류: 질문 내용을 입력해주세요.")
            return

        options = []
        for i in range(1, 5):
            opt_text = input(f"{i}번 선택지 내용: ").strip()
            options.append(f"{i}. {opt_text}")
            
        answer = input("정답 번호 (1~4): ").strip()
        if answer not in ["1", "2", "3", "4"]:
            print("오류: 정답은 1~4 사이의 숫자여야 합니다.")
            return
        
        self.quizzes.append({
            "question": question,
            "options": options,
            "answer": answer
        })
        self.save_json(self.quiz_file, self.quizzes)
        print("퀴즈가 성공적으로 저장되었습니다.")

    def list_quizzes(self):
        print("\n--- 퀴즈 목록 ---")
        self.quizzes = self.load_json(self.quiz_file)
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q['question']}")

    def show_scores(self):
        print("\n--- 역대 점수 기록 ---")
        self.score_history = self.load_json(self.score_file)
        if not self.score_history:
            print("기록이 없습니다. 퀴즈를 먼저 풀어보세요.")
        else:
            for i, s in enumerate(self.score_history, 1):
                print(f"{i}회차: {s}")

    def show_wrong_answers(self):
        print("\n--- 오답 노트 ---")
        wrong_data = self.load_json(self.wrong_file)
        if not wrong_data:
            print("오답 노트가 비어 있습니다. 모두 맞히셨네요! 🎉")
            return
            
        for i, q in enumerate(wrong_data, 1):
            print(f"\nQ{i}. {q['question']}")
            for opt in q['options']:
                print(opt)
            print(f">> 정답: {q['answer']}번")

    def main_menu(self):
        while True:
            print("\n=== 퀴즈 시스템 메뉴 ===")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 기록")
            print("5. 오답 노트")
            print("6. 종료")
            
            choice = input("선택: ").strip()
            if choice == '1':
                self.run_quiz()
            elif choice == '2':
                self.add_quiz()
            elif choice == '3':
                self.list_quizzes()
            elif choice == '4':
                self.show_scores()
            elif choice == '5':
                self.show_wrong_answers()
            elif choice == '6':
                print("프로그램을 종료합니다.")
                break
            else:
                print("오류: 1~6 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    QuizSystem().main_menu()