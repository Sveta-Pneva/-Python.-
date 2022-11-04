"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для второго скрипта
"""
"""Хранение информации о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумываете, например, реализует словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью."""
from pympler import asizeof
#before
annual_profit = {423000 : "adc", 946086 : "qwerty", 65037 : "point", 0 : "tx", 8967 : "cd", 123 : "abq"}
keys = sorted(annual_profit)
keys = keys[::-1][:3]
for i in range(3):
    k = keys[i]
    print(annual_profit[k], k)

print(asizeof.asizeof(annual_profit, keys))


#after
a_p = (423000, 946086, 65037, 0, 8967, 123)
company = "adc qwerty point tx cd abq"
for i in sorted(a_p)[3:]:
    print(company.split(" ")[a_p.index(i)], i)

print(asizeof.asizeof(a_p, company))
