"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

l = []
o = [i for i in range(10)]
d = deque([])
f1 = {}
f2 = {}
res = {}
# 1
def append_in_list(lst):
    for i in range(10000):
        lst.append(i)

def append_in_deque(dec):
    for i in range(10000):
        dec.append(i)

for i in range(10):
    f1[timeit("append_in_list(l)", globals=globals(), number=1000)] = "append_in_list()"
    f2[timeit("append_in_deque(d)", globals=globals(), number=1000)] = "append_in_deque()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
# {0.9056755999990855: 'append_in_list()', 0.6938873000035528: 'append_in_deque()'}

def pop_from_list(lst):
    for i in range(1000):
        lst.append(i)

def pop_from_deque(dec):
    for i in range(1000):
        dec.append(i)

for i in range(10):
    f1[timeit("pop_from_list(l)", globals=globals(), number=1000)] = "pop_from_list()"
    f2[timeit("pop_from_deque(d)", globals=globals(), number=1000)] = "pop_from_deque()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
# {0.06292579999717418: 'pop_from_list()', 0.06998320000275271: 'pop_from_deque()'}


def extend_from_list(lst, o_l):
    for i in range(1000):
        lst.extend(o_l)

def extend_from_deque(dec, o_l):
    for i in range(1000):
        dec.extend(o_l)

for i in range(10):
    f1[timeit("extend_from_list(l, o)", globals=globals(), number=1000)] = "extend_from_list()"
    f2[timeit("extend_from_deque(d, o)", globals=globals(), number=1000)] = "extend_from_deque()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
#{0.07574960000056308: 'extend_from_list()', 0.06268719999934547: 'extend_from_deque()'}

#2
def appendleft_in_deque(dec):
    for i in range(100):
        dec.appendleft(i)

def appendleft_in_list(lst):
    for i in range(100):
        lst.insert(0, i)

for i in range(10):
    f1[timeit("appendleft_in_list(l)", globals=globals(), number=1000)] = "appendleft_in_list()"
    f2[timeit("appendleft_in_deque(d)", globals=globals(), number=1000)] = "appendleft_in_deque()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
# {2.490661199997703: 'appendleft_in_list()', 0.005553800001507625: 'appendleft_in_deque()'}


def popleft_in_deque(dec):
    dec.popleft()

def popleft_in_list(lst):
    lst.reverse()
    lst.pop()
    lst.reverse()


f1[timeit("popleft_in_list(l)", globals=globals(), number=1000)] = "popleft_in_list()"
f2[timeit("popleft_in_deque(d)", globals=globals(), number=1000)] = "popleft_in_deque()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
# {236.4986622000015: 'popleft_in_list()', 0.00015920000078040175: 'popleft_in_deque()'}

def extendleft_in_deque(dec, o_l):
    dec.extendleft(o_l)

def extendleft_in_list(lst, o_l):
    lst.reverse()
    lst.append(o_l)
    lst.reverse()


f1[timeit("extendleft_in_list(l, o)", globals=globals(), number=1000)] = "extendleft_in_list()"
f2[timeit("extendleft_in_deque(d, o)", globals=globals(), number=1000)] = "extendleft_in_deque()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
# {237.53296770000088: 'extendleft_in_list()', 0.0004348999973444734: 'extendleft_in_deque()'}
#3
"""Операции над deque быстрее чем над list, за исключением операции pop."""