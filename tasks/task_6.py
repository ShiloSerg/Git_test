def roman_number(str_: str) -> int:
    romannums = {"M": 1000, "D": 500, "C": 100, "L": 50,
                 "X": 10, "V": 5, "I": 1}

    list_numbers = []

    for index, value in enumerate(str_):
        if value not in romannums.keys():
            raise ValueError('Таких букв нет в римских числах')
        if index < len(str_) - 1:
            if romannums[value] < romannums[str_[index + 1]]:
                new_num = -romannums[value]
                list_numbers.append(new_num)
            else:
                list_numbers.append(romannums[value])
        else:
            list_numbers.append(romannums[value])
    normal_year = sum(list_numbers)
    print(normal_year)
    return normal_year

if __name__ == '__main__':
    roman_number('XXI')
