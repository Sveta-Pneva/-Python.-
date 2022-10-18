"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""
class StackClass:
    def __init__(self):
        self.elems = []
        self.index = -1
        self.list_of_elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.list_of_elems) == 10 or len(self.elems) == 0:
            self.list_of_elems = []
            self.elems.append(self.list_of_elems)
            self.index += 1
        self.list_of_elems.append(el)
        self.elems[self.index] = self.list_of_elems


    def pop_out(self):
        a = self.list_of_elems.pop()
        if len(self.list_of_elems) == 0:
            self.elems.pop()
            self.list_of_elems = self.elems[len(self.elems) - 1]
        else:
            self.elems[self.index] = self.list_of_elems
        return a

    def get_val(self):
        return self.list_of_elems[len(self.list_of_elems) - 1]

    def stack_size(self):
        count = 0
        for i in self.elems:
            count += len(i)
        return count

    def return_elems(self):
        return self.elems


if __name__ == '__main__':
    S_O_P = StackClass()
    for i in range(31):
        S_O_P.push_in(i)
        print(S_O_P.stack_size())
    print(S_O_P.pop_out())
    print(S_O_P.return_elems())
    print(S_O_P.get_val())
