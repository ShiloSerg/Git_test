def get_strong_word(str_: str) -> str:
    data = str_.split()
    for word in data:
        word_strong = 0
        for ch in word:
            if ch.isalpha():
                word_strong += ord(ch)
        print(word_strong)


get_strong_word('Какое то слово сильнее')




