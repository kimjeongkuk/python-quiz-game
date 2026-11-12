def show_menu():
    print("\n--- 📒 나만의 단어장 ---")
    print("1. 단어 등록")
    print("2. 전체 단어 보기")
    print("3. 단어 검색")
    print("4. 단어 삭제")
    print("5. 종료")
    return input("메뉴 선택: ")

def main():
    words = {} # 단어를 저장할 딕셔너리
    
    while True:
        menu = show_menu()
        
        if menu == "1":
            word = input("새 단어: ")
            mean = input("뜻: ")
            words[word] = mean
            print(f"✅ '{word}' 등록 완료!")
            
        elif menu == "2":
            print("\n--- 단어 목록 ---")
            if not words:
                print("비어 있습니다.")
            else:
                for w, m in words.items():
                    print(f"{w} : {m}")
                
        elif menu == "3":
            search_word = input("검색할 단어를 입력하세요: ")
            
            if search_word in words: # 만약 입력한 단어가 words 안에 있다면
                print(f"🔍 {search_word}의 뜻: {words[search_word]}")
            else: # 없다면
                print(f"❌ '{search_word}'은(는) 단어장에 없습니다.")
            
        elif menu == "4":
            # [미션] 여기에 삭제 기능을 만들어보세요!
            pass
            
        elif menu == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()