# Implementation of a binary search tree


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, new_node):
        self.left = new_node

    def set_right(self, new_node):
        self.right = new_node


class BST:

    def __init__(self):
        self.root = None

    def in_order(self):
        if self.root is not None:
            self._in_order(self.root)

    def _in_order(self, root):
        if root:
            self._in_order(root.get_left())
            print(root.get_data())
            self._in_order(root.get_right())

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, root, val):
        if root.get_data() > val:
            if root.get_left() is not None:
                self._insert(root.get_left(), val)
            else:
                root.set_left(Node(val))
        elif root.get_data() < val:
            if root.get_right() is not None:
                self._insert(root.get_right(), val)
            else:
                root.set_right(Node(val))


tree = BST()
tree.insert(20)
tree.insert(70)
tree.insert(1000)
tree.insert(10)
tree.insert(12)
tree.insert(-1)
tree.insert(1)
tree.insert(-20)

tree.in_order()
