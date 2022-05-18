def bytes_to_dec(bytes: list) -> int:
    return int(''.join(str(x) for x in bytes), base=2)


if __name__ == '__main__':
    print(bytes_to_dec([0, 1, 1, 0]))
    print(bytes_to_dec([1, 1, 1, 1]))