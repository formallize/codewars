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


is_square([1, 4, 9, 16, 25, 36])  # True
is_square([1, 2, 3, 4, 5, 6])  # False
is_square([])  # None


# 2. Homogenous arrays. На входе списки, нужно вернуть только списки, которые непустые и имеют одинакового типа данные
# def filter_homogenous(arrays):
#     new_arr = []
#     new_arr_index = []
#     for i in range(0, len(arrays)):
#         array_list = list(map(type, arrays[i]))
#         if len(set(array_list)) == 1:
#             new_arr.append(array_list)
#             new_arr_index.append(i)
#
#     # print(new_arr)
#     # print(new_arr_index)
#     for i in new_arr_index:
#         print(arrays[i], end=' ')
#
#
# # filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]])  # [1, 5, 4], ['b']]
# filter_homogenous([[123, 234, 432], ['', 'abc'], [''], ['', 1], ['', '1'], []])  # [123, 234, 432], ['', 'abc'], [''],
# ['', '1']

# 3. Initialize my name. Дано полное имя, нужно проинициализировать имя и среднее имя представить в виде инициалов
def initialize_names(name):
    # РЕШЕНИЕ №1
    name_list = name.split(' ')
    if len(name_list) == 1 or len(name_list) == 2:
        return ' '.join(name_list)
    else:
        f'{name_list[0]} {" ".join([w[0] + "." for w in name_list[1:-1]])} {name_list[-1]}'
    # РЕШЕНИЕ №2
    names = name.split()
    names[1:-1] = map(lambda n: n[0] + '.', names[1:-1])
    return ' '.join(names)


initialize_names('Jack Ryan')  # Jack Ryan
initialize_names('Lois Mary Lane')  # Lois M. Lane
initialize_names('Dimitri')  # Dimitri
initialize_names('Alice Betty Catherine Davis')  # Alice B. C. Davis


# Frequency sequence. Принимается строка и разделитель. На выходе вывести строку с количеством каждого символа в строке
def freq_seq(s, sep):
    # РЕШЕНИЕ №1
    return ''.join([str(s.count(w)) + sep for w in s])[:-1]
    # РЕШЕНИЕ №2
    sep.join([str(s.count(w) for w in s)])



freq_seq('hello world', '-')  # '1-1-3-3-2-1-1-2-1-3-1'
freq_seq('19999999', ':')  # '1:7:7:7:7:7:7:7'



