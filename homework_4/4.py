"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]
f1 = {}
f2 = {}
f3 = {}
res = {}

def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

for i in range(100):
    f1[timeit("func_1()", globals=globals(), number=1000)] = "func_1()"
    f2[timeit("func_2()", globals=globals(), number=1000)] = "func_2()"
    f3[timeit("func_3()", globals=globals(), number=1000)] = "func_3()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
res[min(f3)] = f3[min(f3)]
print(res[min(res)], min(res))
print(res)

# по результатам 10 запусков программы, func_1() показывала наименьший результат 9 из 10 раз,
# func_3() показывала наименьший результат 1 из 10 раз, следовательно у меня не получилось ускорить задачу, так как это
# низкий показатель