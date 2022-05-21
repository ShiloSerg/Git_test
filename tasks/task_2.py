def wave(word: str) -> None:
    for i in range(len(word)):
        print(f'{word[:i]}{word[i].upper()}'
              f'{word[i + 1:]}')


if __name__ == '__main__':
    wave('hello')
