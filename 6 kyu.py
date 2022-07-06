# 1. Find the odd int. На вход подается массив чисел. Найти число, которое встречается нечетное количество раз.
from functools import reduce


def find_it(seq):
    # РЕШЕНИЕ №1
    return [x for x in seq if seq.count(x) % 2 != 0][0]

    # РЕШЕНИЕ №2
    for i in seq:
        if seq.count(i) % 2:
            return i

    # РЕШЕНИЕ №3
    return reduce(operator.xor, xs)


find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])  # 5 (встречается 3 раза)
find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])  # -1 (встречается 1 раз)
find_it([10, 10, 10])  # 10 (встречается 1 раз)


# 2. Counting Duplicates. На вход подается строка, вывести количество символов, которые встречаются более 1 раза вне
# зависимости от регистра.
def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])


duplicate_count("abideaa")  # 1 (a)
duplicate_count("Indivisibilities")  # 2 (s, i)

# 3. Sum of Digits / Digital Root. Получаем на вход число, нужно складывать числа числа пока не дойдем до одной цифры.
# Пример:
# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


# 4. Who likes it?
[]  # "no one likes this"
["Peter"]  # "Peter likes this"
["Jacob", "Alex"]  # "Jacob and Alex like this"
["Max", "John", "Mark"]  # "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  # "Alex, Jacob and 2 others like this"


def likes(names):
    # РЕШЕНИЕ №1
    if names:
        if len(names) == 1:
            return f'{names[0]} likes this'
        elif len(names) == 2:
            return f'{" and ".join(names)} like this'
        elif len(names) == 3:
            return f'{names[0]}, {names[1]} and {names[2]} like this'
        else:
            return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
    else:
        return 'no one likes this'

    # РЕШЕНИЕ №2
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)
