"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit

def gnome_sort(lst_obj):
    i = 1
    size = len(lst_obj)
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1
    return lst_obj

m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(gnome_sort(orig_list[:])[(len(orig_list) - 1) // 2])

m = 100
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(gnome_sort(orig_list[:])[(len(orig_list) - 1) // 2])

m = 1000
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(gnome_sort(orig_list[:])[(len(orig_list) - 1) // 2])
# 0.03418420000525657
# -28
# 3.6993058000007295
# 4
# 423.2976653000005
# -2