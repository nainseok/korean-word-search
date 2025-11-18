# index : // 588
first = [['ㄱ'], ['ㄱ', 'ㄱ'], ['ㄴ'], ['ㄷ'], ['ㄷ', 'ㄷ'], ['ㄹ'], ['ㅁ'], ['ㅂ'], ['ㅂ', 'ㅂ'], ['ㅅ'], ['ㅅ', 'ㅅ'], ['ㅇ'], ['ㅈ'], ['ㅈ', 'ㅈ'], ['ㅊ'], ['ㅋ'], ['ㅌ'], ['ㅍ'], ['ㅎ']]

# index : % 588 // 28 
middle = [['ㅏ'], ['ㅏ', 'ㅣ'], ['ㅑ'], ['ㅑ', 'ㅣ'], ['ㅓ'], ['ㅓ', 'ㅣ'], ['ㅕ'], ['ㅕ', 'ㅣ'], ['ㅗ'], ['ㅗ', 'ㅏ'], ['ㅗ', 'ㅏ', 'ㅣ'], ['ㅗ', 'ㅣ'], ['ㅛ'], ['ㅜ'], ['ㅜ', 'ㅓ'], ['ㅜ', 'ㅓ', 'ㅣ'], ['ㅜ', 'ㅣ'], ['ㅠ'], ['ㅡ'], ['ㅡ', 'ㅣ'], ['ㅣ']]

# index : % 28
last = [[], ['ㄱ'], ['ㄱ', 'ㄱ'], ['ㄱ', 'ㅅ'], ['ㄴ'], ['ㄴ', 'ㅈ'], ['ㄴ', 'ㅎ'], ['ㄷ'], ['ㄹ'], ['ㄹ', 'ㄱ'], ['ㄹ', 'ㅁ'], ['ㄹ', 'ㅂ'], ['ㄹ', 'ㅅ'], ['ㄹ', 'ㅌ'], ['ㄹ', 'ㅍ'], ['ㄹ', 'ㅎ'], ['ㅁ'], ['ㅂ'], ['ㅂ', 'ㅅ'], ['ㅅ'], ['ㅅ', 'ㅅ'], ['ㅇ'], ['ㅈ'], ['ㅊ'], ['ㅋ'], ['ㅌ'], ['ㅍ'], ['ㅎ']]

def let_decom(letter):
    n = ord(letter) - 44032
    l = first[n // 588] + middle[(n % 588) // 28] + last[n % 28]
    return(l)

def word_decom(word):
    l = []
    for c in word:
        l += let_decom(c)
    return(sorted(l))

def conso_let_decom(letter):
    n = ord(letter) - 44032
    l = first[n // 588] + last[n % 28]
    return(l)

def conso_word_decom(word):
    l = []
    for c in word:
        l += conso_let_decom(c)
    return(sorted(l))

def is_basic(word):
    for c in word:
        n = ord(c) - 44032
        if len(first[n // 588]) > 1:
            return False
        if len(middle[(n % 588) // 28]) > 1:
            return False
        if len(last[n % 28]) > 1:
            return False
    return True

def let_ceasar(letter, foff, moff, loff):
    n = ord(letter) - 44032 + (foff % 19) * 588 + (moff % 21) * 28 + (loff % 28)
    if n > 19 * 21 * 28:
        n -= 19 * 21 *28
    return chr(n+44032)

def word_ceasar(word, foff, moff, loff):
    s = ""
    for c in word:
        s += let_ceasar(c, foff, moff, loff)
    return s

if __name__ == "__main__":
    print(word_ceasar("보석반지", 4, 4, 4))