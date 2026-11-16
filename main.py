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
        self.categories = ["Python", "수학", "영어", "상식", "기타"]
        # ✅ 난이도 목록 추가
        self.difficulties = ["쉬움", "보통", "어려움"]
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

    def select_category(self):
        print("\n카테고리를 선택하세요:")
        for i, cat in enumerate(self.categories, 1):
            print(f"  {i}. {cat}")
        while True:
            choice = input("번호 입력: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(self.categories):
                return self.categories[int(choice) - 1]
            print(f"오류: 1~{len(self.categories)} 사이의 숫자를 입력해주세요.")

    def select_difficulty(self):
        # ✅ 난이도 선택 메서드 추가
        print("\n난이도를 선택하세요:")
        for i, diff in enumerate(self.difficulties, 1):
            print(f"  {i}. {diff}")
        while True:
            choice = input("번호 입력: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(self.difficulties):
                return self.difficulties[int(choice) - 1]
            print(f"오류: 1~{len(self.difficulties)} 사이의 숫자를 입력해주세요.")

    def add_quiz(self):
        print("\n=== 퀴즈 추가 ===")

        question = input("문제를 입력하세요: ")
        if not self.validate_input(question, "문제"):
            return

        category = self.select_category()
        # ✅ 난이도 선택 추가
        difficulty = self.select_difficulty()

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
            "category": category,
            "difficulty": difficulty,  # ✅ 난이도 저장
            "options": options,
            "answer": int(answer)
        })
        self.save_quizzes()
        print(f"[{category} / {difficulty}] 퀴즈가 추가되었습니다!")

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

        # ✅ 난이도 필터링 추가
        print("난이도를 선택하시겠습니까?")
        print("  1. 전체")
        print("  2. 난이도 선택")
        diff_mode = input("번호 입력: ").strip()

        if diff_mode == "2":
            difficulty = self.select_difficulty()
            quiz_list = [q for q in self.quizzes
                         if q.get("difficulty") == difficulty]
            if not quiz_list:
                print(f"[{difficulty}] 난이도에 퀴즈가 없습니다.")
                return
            print(f"[{difficulty}] 난이도 퀴즈 {len(quiz_list)}개를 풀겠습니다!")
        else:
            quiz_list = self.quizzes[:]

        print("\n카테고리를 선택하시겠습니까?")
        print("  1. 전체")
        print("  2. 카테고리 선택")
        cat_mode = input("번호 입력: ").strip()

        if cat_mode == "2":
            category = self.select_category()
            quiz_list = [q for q in quiz_list
                         if q.get("category") == category]
            if not quiz_list:
                print(f"[{category}] 카테고리에 퀴즈가 없습니다.")
                return
            print(f"[{category}] 카테고리 퀴즈 {len(quiz_list)}개를 풀겠습니다!")

        quiz_list = random.sample(quiz_list, len(quiz_list))
        score = 0
        wrong_list = []

        for i, quiz in enumerate(quiz_list, 1):
            cat_label = quiz.get("category", "기타")
            diff_label = quiz.get("difficulty", "보통")
            # ✅ 카테고리 + 난이도 함께 표시
            print(f"\nQ{i}. [{cat_label} / {diff_label}] {quiz['question']}")
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
                cat_label = quiz.get("category", "기타")
                diff_label = quiz.get("difficulty", "보통")
                print(f"\nQ{i}. [{cat_label} / {diff_label}] {quiz['question']}")
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
            cat_label = quiz.get("category", "기타")
            diff_label = quiz.get("difficulty", "보통")
            # ✅ 카테고리 + 난이도 함께 표시
            print(f"\nQ{i}. [{cat_label} / {diff_label}] {quiz['question']}")


def main():
    game = QuizGame()
    while True:
        print("\n=== 퀴즈 게임 메뉴 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 오답 노트")
        print("6. 종료")
        choice = input("메뉴를 선택하세요: ").strip()
        if choice == "1":
            game.play_quiz()
        elif choice == "2":
            game.add_quiz()
        elif choice == "3":
            game.show_quizzes()
        elif choice == "4":
            game.show_score()
        elif choice == "5":
            game.show_wrong_notes()
        elif choice == "6":
            print("게임을 종료합니다.")
            break
        else:
            print("오류: 1~6 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()