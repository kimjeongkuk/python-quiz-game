import json
import os

class Wordbook:
    def __init__(self, filename="words.json"):
        """생성자: 단어장 객체가 만들어질 때 파일을 자동으로 불러옵니다."""
        self.filename = filename
        self.words = self.load_data()

    def load_data(self):
        """파일에서 단어 데이터를 불러오는 메서드"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}  # 파일이 없으면 빈 딕셔너리 반환

    def save_data(self):
        """현재 단어 상태를 파일에 저장하는 메서드"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.words, f, ensure_ascii=False, indent=4)

    def add_word(self):
        """단어 추가 메서드"""
        eng = input("추가할 영어 단어: ").strip()
        kor = input("뜻: ").strip()
        self.words[eng] = kor
        self.save_data()
        print(f"✅ '{eng}' 단어가 추가되었습니다.")

    def show_all(self):
        """전체 목록 출력 메서드"""
        if not self.words:
            print("📭 단어장이 비어 있습니다.")
            return
        
        print("\n--- 단어 목록 ---")
        for eng, kor in self.words.items():
            print(f"{eng} : {kor}")
        print("----------------")

# --- 프로그램 실행부 ---
def main():
    # 1. Wordbook 객체 생성 (이때 자동으로 데이터를 불러옴)
    my_book = Wordbook()

    while True:
        menu = input("\n1.추가 2.목록 3.종료 : ")

        if menu == "1":
            my_book.add_word()
        elif menu == "2":
            my_book.show_all()
        elif menu == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()