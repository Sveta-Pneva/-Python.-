"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit

n = 123456789
f1 = {}
f2 = {}
f3 = {}
f4 = {}
res = {}
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    revers_num = " ".join(str(enter_num)).split()
    revers_num.reverse()
    revers_num = int(''.join(map(str, revers_num)))
    return revers_num


for i in range(100):
    f1[timeit("revers(n)", globals=globals(), number=1000)] = "revers()"
    f2[timeit("revers_2(n)", globals=globals(), number=1000)] = "revers_2()"
    f3[timeit("revers_3(n)", globals=globals(), number=1000)] = "revers_3()"
    f4[timeit("revers_4(n)", globals=globals(), number=1000)] = "revers_4()"
res[min(f1)] = f1[min(f1)]
res[min(f2)] = f2[min(f2)]
res[min(f3)] = f3[min(f3)]
res[min(f4)] = f4[min(f4)]
print(res[min(res)], min(res))
print(res)

# по результатам 10 запусков программы, revers_3() показывала наименьший результат 10 из 10 раз
# revers_3() 0.00037739999970654026
# {0.002548900003603194: 'revers()', 0.0016161000021384098: 'revers_2()', 0.00037739999970654026: 'revers_3()', 0.001943200004461687: 'revers_4()'}