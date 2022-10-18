"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
class QueueClass:
    def __init__(self):
        self.elems_to_do = []
        self.elems_modification = []
        self.elems_decided = []

    def is_empty(self):
        return self.elems_to_do == []

    def to_queue(self, item):
        self.elems_to_do.insert(0, item)

    def from_queue(self, num=0):
        if num == 0:
            return self.elems_to_do.pop()
        elif num == 1:
            return self.elems_modification.pop()
        else:
            return self.elems_decided.pop()

    def size(self):
        return len(self.elems_to_do), len(self.elems_modification), len(self.elems_decided)

    def modification_status(self):
        self.elems_modification.insert(0, self.elems_to_do[len(self.elems_to_do) - 1])
        self.elems_to_do.pop()
        return self.elems_modification

    def decided_status(self, num=0):
        if num == 0 or len(self.elems_modification) == 0:
            self.elems_decided.insert(0, self.elems_to_do[len(self.elems_to_do) - 1])
            self.elems_to_do.pop()
        else:
            self.elems_decided.insert(0, self.elems_modification[len(self.elems_modification) - 1])
            self.elems_to_do.pop()
        return self.elems_decided

    def get_queues(self):
        a = []
        a.append(self.elems_to_do)
        a.append(self.elems_modification)
        a.append(self.elems_decided)
        return a


if __name__ == '__main__':
    qc_obj = QueueClass()

    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue('98')
    qc_obj.to_queue(False)
    qc_obj.to_queue('09')
    qc_obj.to_queue('=-=')
    qc_obj.to_queue('+-+')

    print(qc_obj.decided_status())
    print(qc_obj.modification_status())
    print(qc_obj.modification_status())
    print(qc_obj.modification_status())
    print(qc_obj.decided_status())
    print(qc_obj.decided_status(1))
    print(qc_obj.get_queues())
    print(qc_obj.from_queue(1))
