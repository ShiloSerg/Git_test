def endless_wave(word: str) -> str:
    new_word = list(word)
    for value in range(len(word)):
        new_word[value] = new_word[value].upper()
        yield ''.join(new_word)
        new_word[value] = new_word[value].lower()
    for value in range(len(word) - 2, -1, -1):
        new_word[value] = new_word[value].upper()
        yield ''.join(new_word)
        new_word[value] = new_word[value].lower()


if __name__ == '__main__':
    for elem in endless_wave('hello'):
        print(elem)
