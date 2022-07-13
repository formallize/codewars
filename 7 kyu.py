# 1. Are they square? Дан список и нужно определить, являются ли элементы списка квадратами целого числа
from math import sqrt


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


# 4. Задача «FizzBuzz». Написать программу, которая будет печатать все числа от 1 до 100. При этом: Если число
# делится на 3, вместо числа напечатать Fizz. Если число делится на 5, вместо числа напечатать Buzz. Если число
# делится и на 3, и на 5 - напечатать FizzBuzz
def fizzbuzz():
    return ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 else 'Buzz' if x % 5 == 0 else x for x in
            range(1, 101)]


fizzbuzz()


# 5. Есть заданный основной отрезок [A, B] и есть N - количество произвольных задаваемых отрезков. Необходимо вычислить
# длину основного отрезка, на которой не происходит наложения дополнительных отрезков
# A = 15, B = 165
# N1 [37, 68] N2 [52, 74] N3 [118,146] N4 [35, 44] N5 [37, 65] N6 [46, 74]
def my_def():
    set1 = ({x for x in range(37, 69)} | {x for x in range(52, 75)} | {x for x in range(118, 147)} |
            {x for x in range(35, 45)} | {x for x in range(37, 66)} | {x for x in range(46, 75)})
    # print(len({x for x in range(15, 166)} - set1))
    # print({x for x in range(15, 166)} - set1)


my_def()


# def f(s1, s2):
#     if set(s1) == set(s2):
#         print('true')
#     else:
#         print('false')

#
# f('dgo', 'dog')
# f('sddd', 'sddf')


# 6. Disemvowel Trolls. На вход подается фраза и нужно вывести строку без гласных символов.
def disemvowel(string_):
    return ''.join([ch for ch in string_ if ch.lower() not in 'aoeui'])


disemvowel("This website is for losers LOL!")  # Ths wbst s fr lsrs LL!


# 7. Descending Order. На вход приходит число. Небходимо составить максимально возможное число из этих цифр.
def descending_order(num):
    # РЕШЕНИЕ №1
    return ''.join(sorted([n for n in str(num)], reverse=True))

    # РЕШЕНИЕ №2
    return int("".join(sorted(str(num), reverse=True)))


descending_order(123456789)  # 987654321
descending_order(145263)  # 654321


# 8. Mumbling.
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(s):
    # return reduce(lambda x, y: x + '-' + (y * (s.find(y)+1)).title(), [c for c in s])
    return '-'.join(ch.upper() + ch.lower() * i for i, ch in enumerate(s))


accum("ZpgglnRxqenU")  # Z-Pp-Ggg-Lull-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu


# 9. Get the Middle Character. Задача — вернуть средний символ слова. Если длина слова нечетная, вернуть средний
# символ. Если длина слова четная - вернуть средние 2 символа

def get_middle(s):
    # РЕШЕНИЕ №1
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]
    else:
        return s[len(s) // 2]
    # РЕШЕНИЕ №2
    return s[(len(s) - 1) / 2:len(s) / 2 + 1]


get_middle("test")  # "es"
get_middle("testing")  # "t"


# 10. Credit Card Mask. Зашифровать по типу маски кредитных карт
def maskify(cc):
    # РЕШЕНИЕ №1
    if len(cc) > 5:
        return "#" * (len(cc) - 4) + cc[-4:]
    else:
        return cc
    # РЕШЕНИЕ №2
    return "#" * (len(cc) - 4) + cc[-4:]


maskify("4556364607935616")  # ############5616
maskify("64607935616")  # #######5616
maskify("1")  # 1


# 11. Shortest Word. На вход подается фраза из слов, вычислить длину самого короткого слова.
def find_short(s):
    return min([len(w) for w in s.split(' ')])


find_short("bitcoin take over the world maybe who knows perhaps")  # 3


# 12. Isograms. Изограмма — это слово, в котором нет повторяющихся букв. Последовательные или непоследовательные.
# Реализуйте функцию, которая определяет, является ли строка, которая содержит только буквы, является изограммой.
# Предположим, что пустая строка является изограммой. Игнорировать регистр букв.
def is_isogram(s):
    # РЕШЕНИЕ №1:
    new_s = ""
    for ch in s:
        if not ch.lower() in new_s:
            new_s = new_s + ch
    return len(s) == len(new_s)

    # РЕШЕНИЕ №2
    return len(string) == len(set(string.lower()))


is_isogram("Dermatoglyphics")  # Dermatoglyphics True


# 13. Exes and Ohs. Проверьте, содержит ли строка одинаковое количество символов «x» и «o». Метод должен возвращать
# логическое значение и не учитывать регистр. Строка может содержать любые символы.


def xo(s):
    # РЕШЕНИЕ №1:
    s_x = 0
    s_o = 0
    for ch in s:
        if ch.lower() == "x":
            s_x += 1
        elif ch.lower() == "o":
            s_o += 1
    return s_x == s_o
    # РЕШЕНИЕ №2
    s = s.lower()
    return s.count('x') == s.count('o')


xo('xo')
xo('xo0')
xo('xxxoo')


# 14. Count the divisors of a number. Подсчитайте количество делителей натурального числа n.
# 4 --> 3 (1, 2, 4)
# 5 --> 2 (1, 5)
# 12 --> 6 (1, 2, 3, 4, 6, 12)
# 30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)


def divisors(number):
    # РЕШЕНИЕ №1
    new_arr = 0
    for n in range(1, number + 1):
        if number % n == 0:
            new_arr += 1
    return new_arr

    # РЕШЕНИЕ №2
    return len([n for n in range(1, number + 1) if n % n == 0])


# 15. Find the next perfect square! Завершите метод findNextSquare, который находит следующий целочисленный идеальный
# квадрат после квадрата, переданного в качестве параметра. Напомним, что интеграл идеальный квадрат — это целое
# число n, такое что sqrt(n) также является целым числом. Если параметр сам по себе не является идеальным квадратом,
# то следует вернуть -1.

# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square

def find_next_square(sq):
    # РЕШЕНИЕ №1
    if not sqrt(sq) % 1 == 0:
        return -1
    return int((sqrt(sq) + 1) ** 2)

    # РЕШЕНИЕ №2
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1

    # РЕШЕНИЕ №3
    x = sq ** 0.5
    return -1 if x % 1 else (x + 1) ** 2


find_next_square(121)
find_next_square(600)


# 16. Sum of two lowest positive integers. Создайте функцию, которая возвращает сумму двух наименьших положительных
# чисел, учитывая массив из минимум 4 положительных целых чисел. будут переданы положительные целые числа. Например,
# когда передается массив вида [19,5,42,2,77], на выходе должно быть 7.

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


sum_two_smallest_numbers([5, 8, 12, 18, 22])  # 13
sum_two_smallest_numbers([7, 15, 12, 18, 22])  # 19


# 17. Ones and Zeros. Учитывая массив единиц и нулей, преобразуйте эквивалентное двоичное значение в целое число.
# Например: [0,0,0,1] обрабатывается как 0001, что является двоичным представлением 1.

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11

def binary_array_to_number(arr):
    # РЕШЕНИЕ №1
    sum = 0
    for i, n in enumerate(arr[::-1]):
        sum += n * 2 ** i
    return sum
    # РЕШЕНИЕ №2
    return int("".join(map(str, arr)), 2)
    # РЕШЕНИЕ №3
    return int(''.join(str(a) for a in arr), 2)


binary_array_to_number([0, 0, 0, 1]) # 1
binary_array_to_number([0, 1, 1, 0]) # 6
binary_array_to_number([1, 1, 1, 1]) # 15
