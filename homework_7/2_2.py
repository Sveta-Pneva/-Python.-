"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

def mean_sercher(lst_obj):
    while len(lst_obj) > 2:
        lst_obj.pop(lst_obj.index(max(lst_obj)))
        lst_obj.pop(lst_obj.index(min(lst_obj)))
    return lst_obj[0]

m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(mean_sercher(orig_list[:]))
print(
    timeit(
        "mean_sercher(orig_list[:])",
        globals=globals(),
        number=1000))

m = 100
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(mean_sercher(orig_list[:]))
print(
    timeit(
        "mean_sercher(orig_list[:])",
        globals=globals(),
        number=1000))

m = 1000
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(mean_sercher(orig_list[:]))
print(
    timeit(
        "mean_sercher(orig_list[:])",
        globals=globals(),
        number=1000))

# -29
# 0.01075459999992745
# 17
# 0.5211340000000746
# -1
# 50.1017502000002