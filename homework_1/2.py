"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

nums = [2, 8, 0, -9, 13]

# f = 1 + n(n + 1) + 1 = 2 + n + n**2 - квадратичная
def min_num_1(lst):
    min_num = lst[0] #1
    for i in lst: #n
        if i < min_num: #n
            min_num = i #1
    return min_num #1

print(min_num_1(nums))

# f = len(lst) + len(lst) + 1 + n + 1 + n * 1 + 1 = 2 len(lst) + 2n + 3 - линейная
def min_num_2(lst):
    lst = set(lst) #len(lst)
    lst = list(lst) #len(lst)
    min_num = lst[0] #1
    last_num = lst[::-1] #n
    last_num = last_num[0] #1
    if last_num < min_num: #n
        min_num = last_num #1
    return min_num #1

print(min_num_2(nums))