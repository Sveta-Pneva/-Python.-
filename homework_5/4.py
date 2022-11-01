"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

a = {}
b = OrderedDict()
n = [i for i in range(17, 94063*2, 3)]
f1 = {}
f2 = {}
res = {}
def add_in_dict():
    for i in range(10000):
        a[i] = n[i]

def add_in_ordereddict():
    for i in range(10000):
        b[i] = n[i]

for i in range(10):
    f1[timeit("add_in_dict()", globals=globals(), number=1000)] = "add_in_dict()"
    f2[timeit("add_in_ordereddict()", globals=globals(), number=1000)] = "add_in_ordereddict()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
# {0.9007631999993464: 'add_in_dict()', 1.1915893999976106: 'add_in_ordereddict()'}

def get_keys_from_dict():
    for i in range(10000):
        a.keys()

def get_keys_from_ordereddict():
    for i in range(10000):
        b.keys()

for i in range(10):
    f1[timeit("get_keys_from_dict()", globals=globals(), number=1000)] = "get_keys_from_dict()"
    f2[timeit("get_keys_from_ordereddict()", globals=globals(), number=1000)] = "get_keys_from_ordereddict()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
# {0.783790700006648: 'get_keys_from_dict()', 0.7898820000045816: 'get_keys_from_ordereddict()'}

def update_dict():
    for i in range(10000):
        a[i] = "a"

def update_ordereddict():
    for i in range(10000):
        b[i] = "b"

for i in range(10):
    f1[timeit("update_dict()", globals=globals(), number=1000)] = "update_dict()"
    f2[timeit("update_ordereddict()", globals=globals(), number=1000)] = "update_ordereddict()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
print(res[min(res)], min(res))
print(res)
f1 = {}
f2 = {}
res = {}
# {0.6915900000021793: 'pop_from_dict()', 1.0230775000018184: 'pop_from_ordereddict()'}

"""Ответ: если OrderedDict как обычный словарьв Python 3.6 и более поздних версиях, то смысла нет. 
Но если использовать функции присудствущие только у OrderedDict то использование оправдано."""