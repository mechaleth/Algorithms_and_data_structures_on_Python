# Закодируйте любую строку по алгоритму Хаффмана.
import collections
from functools import reduce

Leaf_Data = collections.namedtuple("Leaf_Data", "symbol,weight")


class Empty_Node_Tree:
    _head_weight: int
    _left_leaf = None
    _right_leaf = None

    def __init__(self, left_leaf=None, right_leaf=None):
        self._left_leaf = left_leaf
        self._right_leaf = right_leaf
        self._head_weight = \
            Empty_Node_Tree._get_leaf_weight(self._left_leaf) + \
            Empty_Node_Tree._get_leaf_weight(self._right_leaf)

    @property
    def weight(self):
        return self._head_weight

    @staticmethod
    def _get_leaf_weight(leaf):
        Empty_Node_Tree._leaf_check(leaf)
        if leaf is None:
            return 0
        if isinstance(leaf, Leaf_Data):
            return leaf.weight
        if isinstance(leaf, Empty_Node_Tree):
            return leaf.weight

    @staticmethod
    def _calculate_weight(left_leaf, right_leaf):
        return Empty_Node_Tree._get_leaf_weight(left_leaf) + \
               Empty_Node_Tree._get_leaf_weight(right_leaf)

    @staticmethod
    def _leaf_check(leaf):
        if leaf is None:
            return False
        if isinstance(leaf, Empty_Node_Tree) or isinstance(leaf, Leaf_Data):
            return True
        raise TypeError("Leaf must be an Empty_Node_Tree class or Leaf_Data or None")

    @property
    def left_leaf(self):
        return self._left_leaf

    @left_leaf.setter
    def left_leaf(self, leaf):
        Empty_Node_Tree._leaf_check(leaf)
        self._left_leaf = leaf

    @property
    def right_leaf(self):
        return self._right_leaf

    @right_leaf.setter
    def right_leaf(self, leaf):
        Empty_Node_Tree._leaf_check(leaf)
        self._right_leaf = leaf


def Haffman_drive(string: str) -> Empty_Node_Tree:
    """
    Функция кодирования строки в дерево Хаффмана
    :param string: строка
    :return: элемент - дерево Хаффмана Empty_Node_Tree.
    """
    if not string:
        return Empty_Node_Tree()
    string_counter = collections.Counter(string)
    ordered_counter = [Leaf_Data(k, v) for k, v in sorted(string_counter.items(), key=lambda k: k[1], reverse=True)]
    del string_counter
    node_object = None
    if len(ordered_counter) == 1:
        return Empty_Node_Tree(ordered_counter[0])
    while len(ordered_counter) > 1:
        first_item = ordered_counter.pop()
        second_item = ordered_counter.pop()
        node_object = Empty_Node_Tree(first_item, second_item)
        for indx in range(len(ordered_counter)):
            if node_object.weight > ordered_counter[indx].weight:
                ordered_counter.insert(indx, node_object)
                break
        else:
            ordered_counter.append(node_object)
    return ordered_counter[0]


def Haffman_walk(tree: Empty_Node_Tree) -> dict:
    """
    Формирования словаря закодированных элемнетов
    при проходе по дереву Хаффмана
    :param tree: дерево Хаффмана
    :return: словарь закодированных элементов str : bytes
    """
    # Так было бы правильно. Но нули перед 1 не сохранить
    # right_step = lambda num: (num << 1) ^ 1
    # left_step = lambda num: num << 1
    def right_step(num: bytes):
        return num + b'1'

    def left_step(num: bytes):
        return num + b'0'

    def tree_step(step_func: 'function', leaf_element, init: bytes):
        if isinstance(leaf_element, Leaf_Data):
            sym_dict[leaf_element.symbol] = step_func(init)
        elif isinstance(leaf_element, Empty_Node_Tree):
            Haffman_step(leaf_element, step_func(init))

    sym_dict = {}

    # def Haffman_step(tree: Empty_Node_Tree, init: int):
    def Haffman_step(tree: Empty_Node_Tree, init: bytes):
        """
        Рекурсивное заполнение словаря с кодами символов -
        проходка по дереву Хаффмана
        :param tree: дерево Хаффмана Empty_Node_Tree
        :param init: текущее число для текущего положения узла
        :return: None. Рекурсивное заполнение внешнего словаря sym_dict
        """
        tree_step(right_step, tree.right_leaf, init)
        tree_step(left_step, tree.left_leaf, init)

    Haffman_step(tree, b'')
    return sym_dict


#root_string = "beep boop beer!"
root_string = input("введите строку для кодировки ")

# Дерево Хаффмана
tree = Haffman_drive(root_string)
# Haffman_walk(word, 0)

# Закодируем элементы дерева
Haffman_code_dict = Haffman_walk(tree)
# Выведем кодировку
for key, value in Haffman_code_dict.items():
    # print(f'{key} : {bin(value)}')
    print(f'{key} : {value}')

# Выведем закодированную строку
if not root_string:
    print("Исходная строка пустая, кодировать нечего")
    exit()
print(f'исходная строка {root_string}')
print(f'закодированная строка {reduce(lambda a, b: a + b, [Haffman_code_dict[char] for char in root_string])}')

# Строка, конечно же, будет отличаться от той, что в примере
# из-за сортировки Counter
