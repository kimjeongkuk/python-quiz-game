import json
import os

class Wordbook:
    def __init__(self, filename="words.json"):
        """생성자: 단어장 객체가 만들어질 때 파일을 자동으로 불러옵니다."""
        self.filename = filename
        self.words = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # 파일이 없거나(FileNotFoundError), 내용이 깨졌을 때(JSONDecodeError)
            # 에러를 내지 않고 빈 딕셔너리를 반환해서 프로그램을 계속 실행하게 합니다.
            return {}

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


# Wordbook 클래스를 상속받는 WrongWordbook 클래스
class WrongWordbook(Wordbook): 
    def __init__(self, filename="wrong_words.json"):
        # 부모 클래스(Wordbook)의 생성자를 호출하여 초기화 기능을 그대로 사용합니다.
        # 파일 이름만 "wrong_words.json"으로 다르게 설정합니다.
        super().__init__(filename)

    def show_message(self):
        """오답 노트만의 특별한 기능 추가"""
        print("📢 이건 오답 노트입니다. 더 열심히 공부합시다! 💪")

    # 부모의 기능을 수정(오버라이딩)할 수도 있습니다.
    def show_all(self):
        print("\n--- 🔥 집중 복습! 오답 목록 ---")
        super().show_all() # 부모 클래스의 show_all 기능을 그대로 가져와서 실행


def main():
    # 이제 일반 단어장이 아니라 '오답 노트' 객체를 생성합니다.
    my_book = WrongWordbook() 

    while True:
        menu = input("\n1.추가 2.목록 3.메시지 4.종료 : ")

        if menu == "1":
            my_book.add_word()
        elif menu == "2":
            my_book.show_all()
        elif menu == "3":
            my_book.show_message() # 자식 클래스에만 있는 기능
        elif menu == "4":
            break

if __name__ == "__main__":
    def main():
        my_book = Wordbook() # 또는 WrongWordbook()

    while True:
        try:
            print("\n--- 메뉴를 선택하세요 ---")
            menu = input("1.추가 2.목록 3.삭제 4.종료 : ")
            
            # 만약 숫자가 아닌 문자를 입력했을 때를 대비해 정수 변환 시도
            menu_num = int(menu) 

            if menu_num == 1:
               my_book.add_word()
            elif menu_num == 2:
                my_book.show_all()
            elif menu_num == 3:
                my_book.delete_word()
            elif menu_num == 4:
                print("프로그램을 종료합니다.")
                break
            else:
                print("1~4 사이의 숫자를 입력해주세요.")

        except ValueError:
            # 사용자가 숫자가 아닌 문자(예: 'a', '가')를 입력했을 때 실행됨
            print("⚠️ 에러: 숫자만 입력할 수 있습니다! 다시 시도하세요.")