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
