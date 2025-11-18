# 한글 문자열을 입력
# 예시 : "빨주노초파남보" 입력 시 "빨주노초파남보"만을 이용해 만들 수 있는 단어 출력
# 빈 문자열 입력 시 종료

f = open("words/standard_all_immutables.txt", 'r')
txt = f.readlines()
f.close()

def search(query, txt):
    if not query:
        return -1
    search_list = []
    for line in txt:
        word = line.rstrip()

        # 글자 수 필터
        if len(word) < 2:
            continue

        # 중복 글자 필터
        if len(word) != len(set(word)):
            continue
        
        # cut개 제외 모든 글자가 query에 포함되는지
        cut = 0
        dif = 0
        for i in word:
            if i not in query:
                dif += 1
        if dif > cut:
            continue

        search_list.append(word)
    return search_list

if __name__ == "__main__":
    while True:
        query = input("단어를 입력해주세요\n").strip()
        result = search(query, txt)
        if result == -1:
            break
        else:
            print(f"찾은 단어의 수 : {len(result)}")
            print(result)
