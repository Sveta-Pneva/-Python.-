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
from memory_profiler import profile


num_to_translate = input()
@profile
def num_translate_2(n):
    translation_dict = {"zero": "ноль", "one": "один", "two": "два", "tree": "три", "four": "четыре", "five": "пять",
                     "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять",
                        "eleven": "одиннадцать", "twelve": "двенадцать"}
    return translation_dict.get(n)


print(num_translate_2(num_to_translate))
"""=============================================================
    30     19.5 MiB     19.5 MiB           1   @profile
    31                                         def num_translate_2(n):
    32     19.5 MiB      0.0 MiB           2       translation_dict = {"zero": "ноль", "one": "один", "two": "два", "tree": "три", "four": "четыре", "five": "пять",
    33     19.5 MiB      0.0 MiB           1                        "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять",
    34     19.5 MiB      0.0 MiB           1                           "eleven": "одиннадцать", "twelve": "двенадцать"}
    35     19.5 MiB      0.0 MiB           1       return translation_dict.get(n)


двенадцать"""


#до
@profile
def num_translate(n):
    translation_list = ["zero", "ноль", "one", "один", "two", "два", "tree", "три", "four", "четыре", "five", "пять",
                         "six", "шесть", "seven", "семь", "eight", "восемь", "nine", "девять", "ten", "десять",
                        "eleven", "одиннадцать", "twelve", "двенадцать"]
    if n in translation_list:
        for i in range(len(translation_list)):
            if translation_list[i-1] == n:
                return translation_list[i]
    else:
        return None

print(num_translate(num_to_translate))
"""=============================================================
    32     19.7 MiB     19.7 MiB           1   @profile
    33                                         def num_translate(n):
    34     19.7 MiB      0.0 MiB           1       translation_list = ["zero", "ноль", "one", "один", "two", "два", "tree", "три", "four", "четыре", "five", "пять",
    35                                                                  "six", "шесть", "seven", "семь", "eight", "восемь", "nine", "девять", "ten", "десять",
    36                                                                 "eleven", "одиннадцать", "twelve", "двенадцать"]
    37     19.7 MiB      0.0 MiB           1       if n in translation_list:
    38     19.7 MiB      0.0 MiB          26           for i in range(len(translation_list)):
    39     19.7 MiB      0.0 MiB          26               if translation_list[i-1] == n:
    40     19.7 MiB      0.0 MiB           1                   return translation_list[i]
    41                                             else:
    42                                                 return None
"""




