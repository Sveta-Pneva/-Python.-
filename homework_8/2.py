"""
Задание 2.
Доработайте пример структуры "дерево", рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения
Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    def update_right_child(self, new_obj=None):
        self.right_child = new_obj

    def update_left_child(self, new_obj=None):
        self.left_child = new_obj

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def get_children(self):
        return {self.root: (self.left_child.root, self.right_child.root)}

    def runner(self):
        print(self.root, end=' ')
        if self.left_child:
            self.left_child.runner()
        if self.right_child:
            self.right_child.runner()




r = BinaryTree(15)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(0.1)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(10)
r.insert_left(11)
r.insert_left(12)
print(r.get_right_child().get_root_val())
print(r.get_children())
# r.find_val(3)
# r.find_val(12)
# r.find_val(0.1)
# r.find_val(11)
print(r.runner())


