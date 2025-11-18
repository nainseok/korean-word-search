# ?와 한글로 이루어진 문자열을 입력
# 예시 : 가운데 글자가 "상"인 세 글자 단어를 검색하고 싶다면 "?상?"을 입력
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
        if len(query) != len(word):
            continue
        is_match = True
        for i in range(len(query)):
            if query[i] != '?' and query[i] != word[i]:
                is_match = False
                break
        if is_match:
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
