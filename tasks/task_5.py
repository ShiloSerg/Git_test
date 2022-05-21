def turn_out(word: str) -> str:
    half_len_word = len(word) // 2
    if len(word) % 2 == 0:
        new_word = reversed(f'{word[-half_len_word:]}'
                            f'{word[:half_len_word]}')
        print(''.join(new_word))
        return ''.join(new_word)
    if len(word) % 2 != 0:
        average_letter = len(word) - half_len_word - 1
        new_word = reversed(f'{word[-half_len_word:]}'
                            f'{word[average_letter]}'
                            f'{word[:half_len_word]}')
        print(''.join(new_word))
        return ''.join(new_word)


if __name__ == '__main__':
    turn_out('male')
    turn_out('mouse')
