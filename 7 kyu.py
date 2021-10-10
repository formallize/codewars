# 1. Are they square? Дан список и нужно определить, являются ли элементы списка квадратами целого числа
def is_square(arr):
    # РЕШЕНИЕ №1
    if not arr:
        return None
    for el in arr:
        if (el ** 0.5) % 1 != 0.0:
            return False
    return True
    # РЕШЕНИЕ №2 (функция all() возвращает True, если все элементы коллекции равны True)
    if arr:
        return all((a ** 0.5).is_integer() for a in arr)


is_square([1, 4, 9, 16, 25, 36]) # True
is_square([1, 2, 3, 4, 5, 6]) # False
is_square([]) # None
