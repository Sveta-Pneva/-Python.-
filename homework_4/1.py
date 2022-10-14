"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

a = [i for i in range(1000)]
f1 = {}
f2 = {}
f3 = {}
res = {}

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in nums if nums[i] % 2 == 0]
    return new_arr

def func_3(nums):
    new_arr = [i for i in nums if nums[i] % 2 == 0]
    return new_arr

for i in range(100):
    f1[timeit("func_1(a)", globals=globals(), number=1000)] = "func_1()"
    f2[timeit("func_2(a)", globals=globals(), number=1000)] = "func_2()"
    f3[timeit("func_3(a)", globals=globals(), number=1000)] = "func_3()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
res[min(f3)] = f3[min(f3)]
print(res[min(res)], min(res))
print(res)

# по результатам 10 запусков программы func_2() показывала наименьший результат 9 из 10 раз
# мне удалось создать функцию, которая работает быстрее в 1.35 раз первоначальной
# func_2() 0.06800289999955567
# {0.0919992999988608: 'func_1()', 0.06800289999955567: 'func_2()', 0.06803930000023684: 'func_3()'}