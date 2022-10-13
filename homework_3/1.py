"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
from time import time as t
a = 9876543
l = []
d = {}
def funk_speed(funk):
    def speed(*args, **kwargs):
        start = t()
        result = funk(*args, **kwargs)
        finish = t()
        time = finish - start
        print(funk)
        print(time)
        return result
    return speed

# a. функция add_in_list выполняется быстрее
@funk_speed
def add_in_list(lst, n):
    for i in range(n): #n
        lst.append(i) #1

add_in_list(l, a)

@funk_speed
def add_in_dict(dct, n):
    for i in range(n): #n
        dct[i] = i #1

add_in_dict(d, a)


# b. функция get_from_list выполняется быстрее
@funk_speed
def get_from_list(lst, n, k=0, m=1):
    new_list= [] #1
    for i in range(k, n, m): #n
        new_list.append(lst[i]) #1
    return new_list #1

get_from_list(l, a)


@funk_speed
def get_from_dict(dct, n, k=0, m=1):
    new_dict = {} #1
    for i in range(k, n, m): #n
        new_dict[dct[i]] = i #1
    return new_dict #1

get_from_dict(d, a)


# c. функция drop_from_dict выполняется быстрее
# <function drop_from_list at 0x000001BF222A5CF0>
# 92.31419396400452
# 9866543
# <function drop_from_dict at 0x000001BF222A5E10>
# 0.00099945068359375
# 9866543
@funk_speed
def drop_from_list(lst, n):
    for i in range(n): #n
        lst.pop(i) #1

drop_from_list(l, 10000)
print(len(l))

@funk_speed
def drop_from_dict(dct, n):
    for i in range(n): #n
        dct.pop(i) #1

drop_from_dict(d, 10000)
print(len(d))