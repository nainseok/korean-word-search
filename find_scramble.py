from decompose import word_decom
f = open("words/standard_all_immutables.txt", 'r')
txt = f.readlines()
f.close()

sc_dic = {}
for line in txt:
    word = line.rstrip()
    dec = tuple(word_decom(word))
    if dec in sc_dic:
        sc_dic[dec].append(word)
    else:
        sc_dic[dec] = [word]

while True:
    query = input("단어를 입력해주세요\n").strip()
    if not query:
        break
    dec = tuple(word_decom(query))
    if dec in sc_dic:
        print(f"찾은 단어의 수 : {len(sc_dic[dec])}")
        print(sc_dic[dec])
    else:
        print("단어를 찾을 수 없습니다.")
