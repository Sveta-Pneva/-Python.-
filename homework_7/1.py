"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit

def bubble_sort(lst_obj):
    n = len(lst_obj)
    x = 1
    while n > x:
        for i in range(n-1, -1+x, -1):
            if lst_obj[i] < lst_obj[i-1]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        x += 1
    return lst_obj

def bubble_sort_1(lst_obj):
    n = len(lst_obj)
    x = 1
    a = 1
    while n > x:
        if a == 0:
            return lst_obj
        a = 0
        for i in range(n-1, -1+x, -1):
            if lst_obj[i] < lst_obj[i-1]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
                a = 1
        x += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort(orig_list[:]))
sorted(orig_list)
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

"""[43, -47, 42, -43, 62, -39, 93, 9, -35, -36]
[-47, -43, -39, -36, -35, 9, 42, 43, 62, 93]
0.009756299999935436
0.009523900000203867
[-42, -55, -12, -10, -60, -54, -18, 32, -82, -43, 83, -40, -72, 64, 92, -36, 74, -98, 29, -94, 76, -19, -73, 41, -39, 2, -27, -90, 29, 86, -96, -41, -100, -61, -13, -3, 27, 2, -70, -85, -17, 31, -4, 94, 60, 16, -96, 82, 10, -25, 13, -33, 56, 17, 38, 42, 71, 42, 30, 16, 21, -96, 85, -87, 12, -29, -42, -17, 54, -11, -20, 90, 30, 87, -7, 34, -47, 79, 74, -25, 19, 48, 59, -88, -12, -57, -34, -88, -64, 28, 48, 72, 15, -84, -8, -81, 16, 90, -12, -81]
[-100, -98, -96, -96, -96, -94, -90, -88, -88, -87, -85, -84, -82, -81, -81, -73, -72, -70, -64, -61, -60, -57, -55, -54, -47, -43, -42, -42, -41, -40, -39, -36, -34, -33, -29, -27, -25, -25, -20, -19, -18, -17, -17, -13, -12, -12, -12, -11, -10, -8, -7, -4, -3, 2, 2, 10, 12, 13, 15, 16, 16, 16, 17, 19, 21, 27, 28, 29, 29, 30, 30, 31, 32, 34, 38, 41, 42, 42, 48, 48, 54, 56, 59, 60, 64, 71, 72, 74, 74, 76, 79, 82, 83, 85, 86, 87, 90, 90, 92, 94]
0.693474900000183
0.6580622000001313
[58, -35, -98, -7, 89, -74, 9, 55, -2, 49, 47, 92, 33, 54, 69, -66, 53, -93, -64, 80, -84, -96, 31, 82, -39, -39, 73, -79, -77, -52, 56, -69, 6, 82, -76, -92, 42, 53, 6, -50, 8, 79, -80, -97, 63, 8, 5, -77, 93, -21, 1, 35, 30, -6, 43, 37, -99, -89, -52, 9, -17, -33, -4, 33, -55, 16, -61, -83, -17, 48, 9, -39, -13, -44, 18, -80, 60, 60, 30, 55, -80, 72, -51, -36, 20, 83, -38, 32, -11, -89, -68, 19, 59, -48, -34, 32, 82, 92, -70, 51, 13, 3, 61, -70, -16, 1, -56, -97, -15, -2, 47, 68, 64, -32, 49, -73, -93, 94, 34, 17, -37, -15, -87, -57, 89, 64, -7, 51, -98, 99, -68, -35, 5, 84, 0, -54, 5, 43, -19, 42, 94, 4, 4, -87, 33, 57, 83, -35, 74, 74, 39, 27, 71, 43, 46, 82, -3, -72, -84, 20, 92, -38, -60, -39, -1, -13, 82, -52, 55, -64, 31, 47, 93, 91, -44, 49, -28, -38, 13, -65, -6, -34, -52, 9, 56, -74, 25, -12, -60, -32, -20, -78, -60, 55, -1, 12, 18, -86, -93, -90, -31, 74, 76, 96, 57, 7, -9, -97, 78, -85, -36, 30, -84, 93, 89, -20, -47, -88, 74, -33, -51, -75, 84, 98, 94, -13, -66, -19, -86, -59, 53, -93, -79, -62, 8, 6, -2, -14, 95, 49, -22, 92, -43, -63, 94, 88, 15, 11, 58, -49, 10, 39, 89, -69, -16, -55, -4, 77, -16, -88, -50, 13, 51, 72, -68, -32, 36, 98, 50, -92, -17, 84, 38, 65, -37, -37, -55, 8, 58, 34, -91, 8, 53, -99, 46, -33, 14, 78, -67, 16, -1, -71, 38, 54, 1, -36, 79, -17, -88, 64, -79, -98, 100, -69, 4, 20, 19, -99, -68, 98, 43, -60, 79, 14, -94, -12, 62, 48, -49, -57, 41, 58, -92, -6, -57, 4, 23, -59, 39, -73, -59, -69, -74, 32, 59, -4, 74, -16, 49, -24, -42, -35, -40, 13, 15, -46, -13, 76, 27, -73, 4, 69, -73, 58, -8, -82, 78, 59, 10, 89, 88, 14, 94, -14, -68, 31, 25, 37, -57, -81, 38, -51, -81, -81, 64, 24, -83, -30, 80, -80, 43, -71, -16, 6, -95, -55, -29, -68, 88, -95, -68, -2, 24, -86, 74, 7, 47, -46, 100, 71, 52, 65, -68, 48, -5, -63, 63, 46, 93, -39, -69, 16, 83, -91, -47, 36, 99, -10, 5, 29, -83, 75, 51, 48, -40, -95, -53, -45, 74, 33, 62, 70, 42, 76, -98, -45, -70, 21, 92, -26, -94, -67, -70, 45, -18, 49, -77, -79, 86, 87, 48, 6, 44, -46, 50, 89, 53, -21, -2, 43, 78, 91, -42, -51, 11, 36, 26, 68, -81, 68, -44, 59, 96, -63, 32, 12, 72, 69, -40, 20, 73, -24, 63, -25, -22, -83, 45, 26, 60, 66, -31, -10, -36, 96, -12, 34, -7, -30, -19, 78, -5, -35, 54, -90, 19, -47, 11, 0, -84, -78, 49, -41, 72, 13, -62, 75, 15, 88, -99, -16, -15, 77, -8, 65, -65, -15, 71, -11, -51, -81, -38, 85, 73, -61, -35, 38, 22, -3, -94, 87, 20, -72, -76, 64, 98, 79, -69, 80, 16, 66, -50, 66, 66, -43, 42, -2, -71, -49, 73, -51, -40, 83, -85, 24, -55, 53, -32, 32, -64, -68, -45, 78, 93, -53, 36, 16, 30, 39, 64, -60, 60, 31, 73, -90, -70, -30, -62, -54, 35, 34, 30, 1, -74, 74, -65, -46, -49, -38, 90, -91, 58, 6, 90, 88, 40, -66, -95, -31, -58, -87, -57, 45, -28, -25, 50, -84, -2, -18, -72, -32, 50, 19, -56, -49, -26, -20, -23, -1, 64, 21, -51, -42, -43, -84, -76, -44, -69, 71, 53, -42, 87, 91, 36, -1, -63, 92, -31, -62, -45, -87, 56, -62, 61, 71, -64, 47, 58, 25, -55, 94, 38, 21, 62, -4, -87, -33, -60, 30, 74, 5, 53, -43, -85, 66, 75, 82, -38, -24, 88, -33, 96, -6, 20, -19, -80, -84, 57, 27, 52, 47, -91, -58, 5, -78, -8, 90, -30, -14, 97, -78, 16, -27, 13, -12, 31, 87, 10, -37, 85, -93, 2, 16, 92, 6, -3, -16, 56, -72, 27, -30, -39, -50, 21, -85, 93, 39, 96, -96, -51, -30, -26, 94, -50, 28, 89, 10, 32, 95, -10, -47, 18, 28, 82, -7, -14, 3, 77, -32, -28, 44, -41, -61, 74, 56, -47, -27, 5, -87, 97, -57, -42, -88, 9, 74, -4, -72, -62, -54, 52, -85, 17, -21, 27, 23, -99, 6, -36, -83, 34, -60, -2, -29, -20, -37, 51, -63, -69, -42, 3, 32, -37, 7, 97, 24, 89, 48, -96, -31, -26, 44, 46, -40, 96, 85, 36, 38, -10, -52, 37, -19, -62, -4, 42, 24, -60, -69, -81, -45, 15, -61, -59, 54, 90, -76, 98, -8, 56, 17, 25, 44, 2, -84, -97, 8, -72, 13, 47, -13, -8, -59, -38, 36, -35, 66, 50, -50, -31, -42, 85, 23, -9, -62, 28, -57, 89, 8, -45, -94, 96, 43, 30, 10, 92, 11, 44, -19, 34, 8, 81, -89, -45, -77, 56, -99, 75, 89, -98, 20, 93, -28, -61, -73, 34, 50, 30, 23, 44, -70, -30, -78, -9, -79, -2, 32, 88, 82, -10, 94, -95, -85, -66, 9, 70, 87, -4, 25, 10, -34, -79, 9, 34, 48, -42, 60, 13, -61, 16, -46, -95, 56, 25, 87, 67, 13, -91, 86, 0, -21, 77, 61, -19, -63, -52, 38, -86, 8, -22, -77, -29, 25, 3, -30, 31, 79, -46, 75, 64, 42, -58, -30, -70, -19, -68, -79, -32, -98, 94, 100, 48, -51, 55, 48, 15, 50, 88, -50, -82, 6, -68, -3, 79, -56, -47, 58, 10, 73, 46, 18, 37, -99, 54, -3, 82, 74, -82, -62, 1, -8, -65, 46, -73, 36, -31, -24, -18, -57, 91, 1, -26, -24]
[-99, -99, -99, -99, -99, -99, -99, -98, -98, -98, -98, -98, -98, -97, -97, -97, -97, -96, -96, -96, -95, -95, -95, -95, -95, -95, -94, -94, -94, -94, -93, -93, -93, -93, -93, -92, -92, -92, -91, -91, -91, -91, -91, -90, -90, -90, -89, -89, -89, -88, -88, -88, -88, -87, -87, -87, -87, -87, -87, -86, -86, -86, -86, -85, -85, -85, -85, -85, -85, -84, -84, -84, -84, -84, -84, -84, -84, -83, -83, -83, -83, -83, -82, -82, -82, -81, -81, -81, -81, -81, -81, -80, -80, -80, -80, -80, -79, -79, -79, -79, -79, -79, -79, -78, -78, -78, -78, -78, -77, -77, -77, -77, -77, -76, -76, -76, -76, -75, -74, -74, -74, -74, -73, -73, -73, -73, -73, -73, -72, -72, -72, -72, -72, -72, -71, -71, -71, -70, -70, -70, -70, -70, -70, -70, -69, -69, -69, -69, -69, -69, -69, -69, -69, -68, -68, -68, -68, -68, -68, -68, -68, -68, -68, -68, -67, -67, -66, -66, -66, -66, -65, -65, -65, -65, -64, -64, -64, -64, -63, -63, -63, -63, -63, -63, -62, -62, -62, -62, -62, -62, -62, -62, -62, -61, -61, -61, -61, -61, -61, -60, -60, -60, -60, -60, -60, -60, -60, -59, -59, -59, -59, -59, -58, -58, -58, -57, -57, -57, -57, -57, -57, -57, -57, -56, -56, -56, -55, -55, -55, -55, -55, -55, -54, -54, -54, -53, -53, -52, -52, -52, -52, -52, -52, -51, -51, -51, -51, -51, -51, -51, -51, -51, -50, -50, -50, -50, -50, -50, -50, -49, -49, -49, -49, -49, -48, -47, -47, -47, -47, -47, -47, -46, -46, -46, -46, -46, -46, -45, -45, -45, -45, -45, -45, -45, -44, -44, -44, -44, -43, -43, -43, -43, -42, -42, -42, -42, -42, -42, -42, -42, -41, -41, -40, -40, -40, -40, -40, -39, -39, -39, -39, -39, -39, -38, -38, -38, -38, -38, -38, -38, -37, -37, -37, -37, -37, -37, -36, -36, -36, -36, -36, -35, -35, -35, -35, -35, -35, -35, -34, -34, -34, -33, -33, -33, -33, -33, -32, -32, -32, -32, -32, -32, -32, -31, -31, -31, -31, -31, -31, -31, -30, -30, -30, -30, -30, -30, -30, -30, -30, -29, -29, -29, -28, -28, -28, -28, -27, -27, -26, -26, -26, -26, -26, -25, -25, -24, -24, -24, -24, -24, -23, -22, -22, -22, -21, -21, -21, -21, -20, -20, -20, -20, -19, -19, -19, -19, -19, -19, -19, -19, -18, -18, -18, -17, -17, -17, -17, -16, -16, -16, -16, -16, -16, -16, -15, -15, -15, -15, -14, -14, -14, -14, -13, -13, -13, -13, -13, -12, -12, -12, -12, -11, -11, -10, -10, -10, -10, -10, -9, -9, -9, -8, -8, -8, -8, -8, -8, -7, -7, -7, -7, -6, -6, -6, -6, -5, -5, -4, -4, -4, -4, -4, -4, -4, -3, -3, -3, -3, -3, -2, -2, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 23, 23, 23, 23, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 26, 26, 27, 27, 27, 27, 27, 28, 28, 28, 29, 30, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 40, 41, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 45, 45, 45, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 60, 60, 60, 60, 60, 61, 61, 61, 62, 62, 62, 63, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 65, 65, 65, 66, 66, 66, 66, 66, 66, 67, 68, 68, 68, 69, 69, 69, 70, 70, 71, 71, 71, 71, 71, 72, 72, 72, 72, 73, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 76, 76, 76, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 80, 80, 80, 81, 82, 82, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 84, 84, 84, 85, 85, 85, 85, 86, 86, 87, 87, 87, 87, 87, 87, 88, 88, 88, 88, 88, 88, 88, 88, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 94, 94, 95, 95, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 98, 98, 98, 98, 98, 99, 99, 100, 100, 100]
82.03682720000006
85.50593990000016"""
# при сортировке не больших списков оптимизированная функция работает быстрее не оптимизированной, но для сортировки больших списков лучше использовать не оптимизированную функцию.