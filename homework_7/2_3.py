"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from timeit import timeit
import statistics

m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(statistics.median(orig_list[:]))
print(
    timeit(
        "statistics.median(orig_list[:])",
        globals=globals(),
        number=1000))


m = 100
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(statistics.median(orig_list[:]))
print(
    timeit(
        "statistics.median(orig_list[:])",
        globals=globals(),
        number=1000))


m = 1000
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
# print(orig_list)
# print(sorted(orig_list[:]))
print(statistics.median(orig_list[:]))
print(
    timeit(
        "statistics.median(orig_list[:])",
        globals=globals(),
        number=1000))

# 24
# 0.0020941999998740357
# 4
# 0.010335200000099576
# 1
# 0.2736873999999716