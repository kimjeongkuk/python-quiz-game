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
            except:
                return []
        return []

    def save_json(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def run_quiz(self):
        if not self.quizzes:
            print("\n[알림] 퀴즈가 없습니다. 2번 메뉴에서 퀴즈를 먼저 추가해주세요!")
            return

        score = 0
        wrong_data = self.load_json(self.wrong_file)
        
        for quiz in self.quizzes:
            print(f"\n질문: {quiz['question']}")
            
            # --- 선택지 출력 부분 (번호가 없어도 강제로 붙여서 출력) ---
            for i, opt in enumerate(quiz['options'], 1):
                # 이미 '1.' 같은 번호가 포함되어 있는지 확인 후 출력
                opt_str = str(opt)
                if opt_str.startswith(f"{i}."):
                    print(opt_str)
                else:
                    print(f"{i}. {opt_str}")
            # ------------------------------------------------------
            
            ans = input("정답 번호 입력: ").strip()
            
            if str(ans) == str(quiz['answer']):
                print(">> 정답입니다! ✨")
                score += 1
                # 맞혔으면 오답노트에서 제거
                wrong_data = [q for q in wrong_data if q['question'] != quiz['question']]
            else:
                print(f">> 오답! 정답은 {quiz['answer']}번입니다. ❌")
                # 틀렸으면 오답노트에 추가
                if not any(q['question'] == quiz['question'] for q in wrong_data):
                    wrong_data.append(quiz)

        self.save_json(self.wrong_file, wrong_data)
        
        # 점수 계산 및 저장
        final_score = (score / len(self.quizzes)) * 100
        self.score_history.append(f"{final_score:.1f}점")
        self.save_json(self.score_file, self.score_history)
        
        print(f"\n[결과] {len(self.quizzes)}문제 중 {score}문제 정답! ({final_score:.1f}점)")

    def add_quiz(self):
        print("\n--- 새 퀴즈 추가 ---")
        question = input("질문 내용: ")
        options = []
        for i in range(1, 5):
            # 입력받을 때 번호는 빼고 내용만 입력받음
            opt_text = input(f"{i}번 선택지 내용: ")
            options.append(opt_text) # 순수한 내용만 저장
            
        answer = input("정답 번호(1, 2, 3, 4 중 하나): ").strip()
        
        self.quizzes.append({
            "question": question,
            "options": options,
            "answer": answer
        })
        self.save_json(self.quiz_file, self.quizzes)
        print("퀴즈가 성공적으로 저장되었습니다!")

    def list_quizzes(self):
        print("\n--- 퀴즈 목록 ---")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
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
            print("오답 노트가 비어 있습니다. 아주 훌륭해요! 🎉")
        else:
            for i, q in enumerate(wrong_data, 1):
                print(f"{i}. {q['question']}")
                # 오답 노트에서도 선택지 번호를 강제로 붙여서 보여줌
                for j, opt in enumerate(q['options'], 1):
                    print(f"   {j}. {opt}")
                print(f"   => 정답: {q['answer']}번")

    def main_menu(self):
        while True:
            print("\n[메뉴] 1.풀기 2.추가 3.목록 4.점수 5.오답 6.종료")
            choice = input("선택: ").strip()
            if choice == '1': self.run_quiz()
            elif choice == '2': self.add_quiz()
            elif choice == '3': self.list_quizzes()
            elif choice == '4': self.show_scores()
            elif choice == '5': self.show_wrong_answers()
            elif choice == '6': 
                print("학습을 종료합니다. 수고하셨어요! 👋")
                break

if __name__ == "__main__":
    QuizSystem().main_menu()