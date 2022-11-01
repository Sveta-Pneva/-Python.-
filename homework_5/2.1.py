"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
class Mull_Add:
    def __init__(self, a, b):
        self.a = "".join(a)
        self.b = "".join(b)

    def __add__(self, other):
        return list(hex(int(self.a, 16) + int(self.b, 16)))[2:]

    def __mull__(self, other):
        return list(hex(int(self.a, 16) * int(self.b, 16)))[2:]

n1 = list(input())
n2 = list(input())

s = Mull_Add(n1, n2) + Mull_Add(n1, n2)
p = Mull_Add(n1, n2) * Mull_Add(n1, n2)
print(s, p)