# -*- coding: utf-8 -*-
import random
import json
import os

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.score = 0
        self.total = 0
        self.played = False
        self.save_file = "quizzes.json"
        self.load_quizzes()

    def validate_input(self, value, field_name):
        if not value.strip():
            print(f"오류: {field_name}을(를) 입력해주세요.")
            return False
        return True

    def save_quizzes(self):
        try:
            with open(self.save_file, "w", encoding="utf-8") as f:
                json.dump(self.quizzes, f, ensure_ascii=False, indent=2)
            print("퀴즈가 저장되었습니다.")
        except Exception as e:
            print(f"저장 실패: {e}")

    def load_quizzes(self):
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, "r", encoding="utf-8") as f:
                    self.quizzes = json.load(f)
                print(f"퀴즈 {len(self.quizzes)}개를 불러왔습니다.")
            except Exception as e:
                print(f"불러오기 실패: {e}")
                self.quizzes = []

    def add_quiz(self):
        print("\n=== 퀴즈 추가 ===")

        question = input("문제를 입력하세요: ")
        if not self.validate_input(question, "문제"):
            return

        options = []
        for i in range(1, 5):
            option = input(f"{i}번 보기를 입력하세요: ")
            if not self.validate_input(option, f"{i}번 보기"):
                return
            options.append(option)

        while True:
            answer = input("정답 번호를 입력하세요(1~4): ")
            if answer in ["1", "2", "3", "4"]:
                break
            print("오류: 1~4 사이의 숫자를 입력해주세요.")

        self.quizzes.append({
            "question": question,
            "options": options,
            "answer": int(answer)
        })
        self.save_quizzes()
        print("퀴즈가 추가되었습니다!")

    def get_hint(self, quiz):
        answer_idx = quiz["answer"] - 1
        wrong_options = [i for i in range(4) if i != answer_idx]
        remove_idx = random.choice(wrong_options)
        print(f"힌트: {remove_idx + 1}번 보기는 오답입니다!")

    def play_quiz(self):
        if not self.quizzes:
            print("\n오류: 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        print("\n=== 퀴즈 시작 ===")
        quiz_list = random.sample(self.quizzes, len(self.quizzes))
        score = 0
        wrong_list = []

        for i, quiz in enumerate(quiz_list, 1):
            print(f"\nQ{i}. {quiz['question']}")
            for j, option in enumerate(quiz['options'], 1):
                print(f"  {j}. {option}")

            while True:
                user_input = input("정답 번호(1~4) 또는 H(힌트): ").strip().upper()
                if user_input == "H":
                    self.get_hint(quiz)
                    continue
                if user_input in ["1", "2", "3", "4"]:
                    break
                print("오류: 1~4 사이의 숫자 또는 H를 입력해주세요.")

            if int(user_input) == quiz["answer"]:
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다! 정답은 {quiz['answer']}번입니다.")
                wrong_list.append(quiz)

        self.total = len(quiz_list)
        self.score = score
        self.played = True

        print(f"\n최종 점수: {self.score}/{self.total}")
        print(f"정답률: {self.score / self.total * 100:.1f}%")

        if wrong_list:
            self.save_wrong_notes(wrong_list)

    def save_wrong_notes(self, wrong_list):
        try:
            with open("wrong_notes.json", "w", encoding="utf-8") as f:
                json.dump(wrong_list, f, ensure_ascii=False, indent=2)
            print(f"오답 {len(wrong_list)}개가 wrong_notes.json에 저장되었습니다.")
        except Exception as e:
            print(f"오답 저장 실패: {e}")

    def show_wrong_notes(self):
        print("\n=== 오답 노트 ===")
        if not os.path.exists("wrong_notes.json"):
            print("저장된 오답이 없습니다.")
            return
        try:
            with open("wrong_notes.json", "r", encoding="utf-8") as f:
                wrong_list = json.load(f)
            for i, quiz in enumerate(wrong_list, 1):
                print(f"\nQ{i}. {quiz['question']}")
                for j, option in enumerate(quiz['options'], 1):
                    print(f"  {j}. {option}")
                print(f"  정답: {quiz['answer']}번")
        except Exception as e:
            print(f"오답 불러오기 실패: {e}")

    def show_score(self):
        print("\n=== 점수 확인 ===")
        if not self.played:
            print("아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어주세요.")
            return
        print(f"최종 점수: {self.score}/{self.total}")
        print(f"정답률: {self.score / self.total * 100:.1f}%")

    def show_quizzes(self):
        print("\n=== 퀴즈 목록 ===")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\nQ{i}. {quiz['question']}")
            for j, option in enumerate(quiz['options'], 1):
                print(f"  {j}. {option}")
            print(f"  정답: {quiz['answer']}번")

    def run(self):
        print("퀴즈 게임에 오신 것을 환영합니다!")

        while True:
            print("\n=== 메뉴 ===")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 점수 확인")
            print("5. 오답 노트 보기")
            print("6. 종료")

            choice = input("\n메뉴를 선택하세요(1~6): ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quizzes()
            elif choice == "4":
                self.show_score()
            elif choice == "5":
                self.show_wrong_notes()
            elif choice == "6":
                print("게임을 종료합니다. 수고하셨습니다!")
                break
            else:
                print("오류: 1~6 사이의 숫자를 입력해주세요.")

            input("\n계속하려면 Enter를 눌러주세요...")

if __name__ == "__main__":
    game = QuizGame()
    game.run()