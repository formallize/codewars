# 1. Fake Binary. Дана строка и нужно заменить числа до 5 на 0, а 5 и выше - на 1
def fake_bin(x):
    # Решение №1
    lst = []
    for i in map(int, x):
        if i < 5:
            lst.append(0)
        else:
            lst.append(1)
    return ''.join(map(str, lst))

    # Решение №2
    return ''.join(('0' if char < '5' else '1' for char in x))


# fake_bin('113495')  # 000011
# fake_bin('8472234') # 1010000


# 2. Beginner - Lost Without a Map. Функция принимает список чисел и необходимо вернуть список с x2 значениями
# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    # Решение №1
    return list(map(lambda x: x * 2, a))

    # Решение №2
    return [x * 2 for x in a]


# maps([1, 2, 3])  # [2, 4, 6]
# maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# maps([1, 4, 8])  # [2, 8, 16]


# 3. Abbreviate a Two Word Name. Функция принимает имя и фамилию и возвращает инициалы человека
def abbrev_name(name):
    # Решенеие 1
    name_dict = name.split(' ')
    return f'{name_dict[0][:1].title()}.{name_dict[1][:1].title()}'

    # Решение 2
    return '.'.join(w[0] for w in name.split()).upper()


# abbrev_name('vasya pupkin')# V.P
# abbrev_name("Anatoly safrygin") # A.S


# 4. Get the mean of an array. Дан список чисел и нужно вернуть среднее арифметическое, округленное до ближ. целого
# числа Решение №1
import math


def get_average(marks):
    # Решение 1
    return math.floor(sum(marks) / len(marks))

    # Решение 2
    return sum(marks) // len(marks)


# get_average([1, 5, 87, 45, 8, 8]) #25
# get_average([1, 5, 87, 45, 8, 8]) #25


# 5. Basic Mathematical Operations. Функция принимает 3 аргумента (оператор, значение 1, значение 2). В зависимости от
# оператора произвести действия со значениями.
def basic_op(operator, value1, value2):
    # Решение 1.
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    else:
        return value1 / value2

    # Решение №2
    return eval("{}{}{}".format(value1, operator, value2))


# basic_op("+", 3, 5) # 8
# basic_op("-", 4, 1) # 3
# basic_op("*", 2, 6) # 12
# basic_op("/", 16, 4) # 4.0


# 6. Remove String Spaces. Функция принимает строку и удаляет в ней первый и последний символ, возвращая оставшуюся
# часть.
def remove_char(s):
    return s[1:-1]


# remove_char("string") #trin


# 7. Return Negative. Функция возвращает отрицательное значение аргумента, НО если оно уже отрицательное - знак не
# меняется
def make_negative(number):
    # Решение №1
    return number if number < 0 else -number

    # Решение №2
    return -abs(num)


# make_negative(2)  # -2
# make_negative(-5)  # -5


# 8. Convert boolean values to strings 'Yes' or 'No'. Принимается аргумент Boolean и нужно вернуть 'Yes' или 'No'
# Решение №1
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


# bool_to_word(True) # Yes


# 9. Reverse words. Функция принимает строку и возвращает каждое слово наоборот
# Решение №1
def reverse_words(text):
    word_list = text.split(' ')
    return ' '.join([word[::-1] for word in word_list])


# reverse_words("This is an example!")


# 10. List Filtering. Функция принимает список из положительных чисел и строк, возвращает список из чисел следуюзим
# образом  filter_list([1,2,'a','b']) == [1,2]
def filter_list(l):
    # Решение №1
    lst = []
    for i in l:
        if isinstance(i, int):
            lst.append(i)
    return lst

    # Решение №2
    return [x for x in l if isinstance(x, int)]


# filter_list([1, 'a', 'b', 0, 15])
# filter_list([1, 2, 'aasf', '1', '123', 123])  # [1,2,123]


# 11. Sum of positive. Дан список чисел. Нужно вернуть сумму положительных чисел. [1,-4,7,12] => 1 + 7 + 12 = 20
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# positive_sum([1,-4,7,12]) # 20


# 12. Character Frequency. Функция принимает строку и нужно рассчитать частоту встречающихся символов
from collections import Counter


def char_freq(message):
    print((Counter(message)))


# char_freq("I like cats") # Counter({' ': 2, 'I': 1, 'l': 1, 'i': 1, 'k': 1, 'e': 1, 'c': 1, 'a': 1, 't': 1, 's': 1})


# 13. Remove the time. Дана строка "Monday February 2, 8pm" и нужно удалить время -> "Monday February 2"
def shorten_to_date(long_date):
    # Решение №1
    return ''.join(long_date.split(',')[:-1])

    # Решение №2
    return long_date.split(', ')[0]


# shorten_to_date("Monday February 2, 8pm") # Monday February 2


# 14. Generate range of integers. В аргументах функции 3 числа (начало, конец и шаг). fun(2, 10, 2) -> [2,4,6,8,10]
# Решение №1
def generate_range(min, max, step):
    print(list(range(min, max + 1, step)))


# generate_range(2, 10, 2)  # [2,4,6,8,10]


# 15. Difference of Volumes of Cuboids. Функция принимает 2 списка, вычислить произведение первого и второго,
# а затем вычесть из наибольшего произведения наименьшее
# Решение №1
from functools import reduce


def find_difference(a, b):
    # Решение №1
    # mul_a = reduce(lambda x, y: x * y, a)
    # mul_b = reduce(lambda x, y: x * y, b)
    # return (mul_b - mul_a if a_list < mul_b else mul_a - mul_b)

    # Решение №2
    return abs((reduce(lambda x, y: x * y, a)) - reduce(lambda x, y: x * y, b))


find_difference([3, 2, 5], [1, 4, 4])  # 14
find_difference([9, 7, 2], [5, 2, 2])  # 106


# 16. Correct the mistakes of the character recognition software. Заменить 5 -> S, 0 -> 0, 1 -> I
def correct(s):
    return s.replace("5", "S").replace("0", "0").replace("1", "I")


# correct("L0ND0N") # LONDON
# correct("51NGAP0RE") # SINGAPORE


# 17. Removing Elements. Дан список элементов и нужно удалить каждый второй элемент списка.
def remove_every_other(my_list):
    # Решение №1
    new_lst = []
    for index, val in enumerate(my_list):
        if index % 2 == 0:
            new_lst.append(val)

    return new_lst
    # Решение №2
    return my_list[::2]


# remove_every_other(['Hello', 'Goodbye', 'Hello Again'])  # ['Hello', 'Hello Again']
# remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # [1, 3, 5, 7, 9]


# 18. Find the smallest integer in the array. Дан список целых чисел, нужно вернуть самое малое из них
def find_smallest_int(arr):
    print(min(arr))


# find_smallest_int([34, 15, 88, 2])  # 2
# find_smallest_int([34, -345, -1, 100])  # -345


# 19. Short Long Short. Даны строки a и b. Вернуть строку short+long+short
def solution(a, b):
    print(a + b + a if len(a) < len(b) else b + a + b)


# solution('45', '1') # 1451
# solution('Soon', 'Me') # MeSoonMe


# 20. Hello, Name or World! Функция принимает имя возвращает строку типа "Hello, {name}!". Если аргумента нет - то
# "Hello, World!"
def hello(name):
    # Решение №1
    return 'Hello, World!' if name is None or name == "" else f'Hello, {name.lower().title()}!'

    # Решение №2
    return f"Hello, {name.title() or 'World'}!"


hello("john")  # Hello, John!
hello("aliCE")  # Hello, Alice!
hello("")  # Hello, World!

# 21. Return Two Highest Values in List. Дан список из чисел. Нужно вернуть 2 максимальных значения в списке,
# если меньше 2 уникальных значений - вернуть его
# def two_highest(arg1):
#     print(sorted(set(arg1))[:0:-1] if len(set(arg1)) > 2 else list(set(arg1)))
#
#
# two_highest([15, 20, 20, 17])  # [20, 17]
# two_highest([1, 1, 1])  # [1]
# two_highest([])  #

# 22. Beginner Series #4 Cockroach. Тараканы - самые быстрые насекомые. Перевести скорость км/ч в см/сек
import math


def cockroach_speed(s):
    # Решение №1
    return math.floor(s * 1000 / 36)
    # Решение №2
    return s // 0.36


cockroach_speed(30)  # 833


def ensure_question(s):
    print(s + '?' if s[0:-1] != '?' else 'hello')


# ensure_question("Well")
# ensure_question("Yes")
# ensure_question("")


# 23. Check the exam. Функция принимает 2 списка, в первом правильные значения, а во втором ответы ученика. Если ответ
# ученика правильный, то +4 очка, если неверный, то -1 очко, а если пустой ответ - то никак не меняется количество
# РЕШЕНИЕ №1
def check_exam(arr1, arr2):
    result = 0
    for i in range(0, 4):
        if arr1[i] == arr2[i]:
            result += 4
        elif arr2[i] == '':
            result += 0
        else:
            result -= 1
    return result == 0 if result < 0 else result

    # РЕШЕНИЕ 2
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))


check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"])  # 6
check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"])  # 0


# 24. Quarter of the year. Входящий аргумент функции - месяц, нужно определить к какому кварталу он относится и вывести
def quarter_of(month):
    # РЕШЕНИЕ №1
    return f'Квартал №{math.ceil(month / 3)}'


quarter_of(3)  # 1
quarter_of(8)  # 2


# 25. Multiple of index. Дан массив целых чисел. Вывести новый массив с числами, которые кратны собственному индексу
def multiple_of_index(arr):
    # РЕШЕНИЕ №1
    new_arr = []
    for index, val in enumerate(arr):
        if index != 0 and val % index == 0:
            new_arr.append(val)

    return new_arr
    # РЕШЕНИЕ №2
    return [lst[i] for i in range(1, len(lst)) if lst[i] % i == 0]


multiple_of_index([22, -6, 32, 82, 9, 25])  # [-6, 32, 25]
multiple_of_index([68, -1, 1, -7, 10, 10])  # [-1, 10]


# 26. На вход дается число n чисел. Вывести все эти числа (кроме числа n) в одну строку через пробел
def find_n():
    n = int(input('Введите число: '))
    print(' '.join(map(str, [n for n in range(1, n)])))


# ind_n()


# 27. Дан список слов. Составить из последних букв каждого слова - новое
def create_word(lst):
    return ''.join([w[-1] for w in lst])


create_word(['кот', 'кити', 'ток'])  # тик


# 28. Name Shuffler. Функция получает в виде строки имя и фамилию. Нужно поменять их местами и вернуть.
def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


name_shuffler('john McClane')  # McClane john


# 29. Прогрессия
def find_sum_prog():
    first = int(input('Введите первый член прогрессии: '))
    diff = int(input('Введите разность прогрессии: '))
    n = int(input('Введите число членов прогрессии: '))
    last_el = first
    for i in range(first, n):
        last_el += diff
    final_sum = ((first + last_el) / 2) * n
    print(f'Сумма первых {n} чисел арифметической прогрессии - {int(final_sum)}')


#find_sum_prog()  # 145


# 30. Do you speak "English"?. На входе строка, проверить содержит ли оно слово 'english' в разных раскладках
def sp_eng(sentence):
    # РЕШЕНИЕ №1
    return True if sentence.lower().find('english') != -1 else False

    # РЕШЕНИЕ №2
    return 'english' in sentence.lower()


sp_eng('English')  # True
sp_eng('1234english ;k')  # True
sp_eng('egnlish')  # False


objects = [1, 2, 1, 2, 3]
print(len(set(objects)))