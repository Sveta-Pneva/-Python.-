"""
Задание 7. На закрепление навыков работы с деком
В рассмотрении на уроке листинга есть один недостаток
Приведенный код руководителя "работа" только строки без пробелов,
например, 'топот'
Молоко делили ледоколом
Вам нужно доработать программу так, чтобы она могла контролироваться
проверка на палиндроме и в таких строках (включающих пробелы)
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""
class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


if __name__ == '__main__':
    dc_obj = DequeClass()
    print(dc_obj.is_empty())  # -> True

    # добавить элементы в хвост
    dc_obj.add_to_rear(10)
    dc_obj.add_to_rear('my_str')

    # добавить элементы в голову
    dc_obj.add_to_front(None)
    dc_obj.add_to_front(True)

    # размер дека
    print(dc_obj.size())  # -> 4
    print(dc_obj.is_empty())  # -> False

    # добавить элемент в хвост
    dc_obj.add_to_rear(3.3)

    print(dc_obj.remove_from_rear())  # -> 3.3
    print(dc_obj.remove_from_front())  # -> True




def pal_checker(string):
    string.lower()
    string = string.split()
    string = ''.join(string)
    print(string)
    dc_obj = DequeClass()

    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
