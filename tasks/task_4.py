def get_strong_word(str_: str) -> int:
    data = str_.split()
    list_strong_words = []
    for word in data:
        word_strong = 0
        for ch in word:
            if ch.isalpha():
                word_strong += ord(ch)
        list_strong_words.append(word_strong)
    print(max(list_strong_words))
    return max(list_strong_words)


if __name__ == '__main__':
    get_strong_word('Какое то слово сильнее')
