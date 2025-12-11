class ArrayBinaryTree:
    
    class Position:
        def __init__(self, container, index):
            self._container = container
            self._index = index

        def element(self):
            return self._container._data[self._index]

        def __eq__(self, other):
            return type(other) is type(self) and other._index == self._index

    def __init__(self):
        self._data = []
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be a Position type")
        if p._container is not self:
            raise ValueError("Position does not belong to this tree")
        if p._index >= len(self._data) or self._data[p._index] is None:
            raise ValueError("Position is no longer valid")
        return p._index

    def _make_position(self, index):
        return self.Position(self, index) if 0 <= index < len(self._data) and self._data[index] is not None else None

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(0) if self._data else None

    def parent(self, p):
        index = self._validate(p)
        if index == 0:
            return None
        return self._make_position((index - 1) // 2)

    def left(self, p):
        index = self._validate(p)
        left_index = 2 * index + 1
        return self._make_position(left_index)

    def right(self, p):
        index = self._validate(p)
        right_index = 2 * index + 2
        return self._make_position(right_index)

    def num_children(self, p):
        index = self._validate(p)
        count = 0
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        
        if left_index < len(self._data) and self._data[left_index] is not None:
            count += 1
        
        if right_index < len(self._data) and self._data[right_index] is not None:
            count += 1

        return count

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return self._size == 0

    def _ensure_capacity(self, index):
        if index >= len(self._data):
            new_size = index + 1
            self._data.extend([None] * (new_size - len(self._data)))

    def add_root(self, element):
        if self._data:
            raise ValueError("Root already exists")
        self._data.append(element)
        self._size = 1
        return self._make_position(0)

    def add_left(self, p, element):
        index = self._validate(p)
        left_index = 2 * index + 1
        self._ensure_capacity(left_index)
        if self._data[left_index] is not None:
            raise ValueError("Left child already exists")
        self._data[left_index] = element
        self._size += 1
        return self._make_position(left_index)

    def add_right(self, p, element):
        index = self._validate(p)
        right_index = 2 * index + 2
        self._ensure_capacity(right_index)
        if self._data[right_index] is not None:
            raise ValueError("Right child already exists")
        self._data[right_index] = element
        self._size += 1
        return self._make_position(right_index)

    def replace(self, p, element):
        index = self._validate(p)
        old = self._data[index]
        self._data[index] = element
        return old

    def delete(self, p):
        index = self._validate(p)
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        has_left = left_index < len(self._data) and self._data[left_index] is not None
        has_right = right_index < len(self._data) and self._data[right_index] is not None

        if has_left and has_right:
            raise ValueError("Cannot delete node with two children")

        child_index = left_index if has_left else (right_index if has_right else None)

        if index == 0:
            if child_index is None:
                self._data = []
                self._size = 0
                return None
            self._data[0] = self._data[child_index]
            self._data[child_index] = None
            self._size -= 1
            return self._data[0]

        if child_index is not None:
            parent_index = (index - 1) // 2
            if index == 2 * parent_index + 1:
                self._data[index] = self._data[child_index]
            else:
                self._data[index] = self._data[child_index]
            self._data[child_index] = None
        else:
            self._data[index] = None

        self._size -= 1
        return None


tree = ArrayBinaryTree()
root = tree.add_root(10)
left = tree.add_left(root, 5)
right = tree.add_right(root, 20)
tree.add_left(left, 2)
tree.add_right(left, 7)

print("Tamanho da árvore:", len(tree))
print("Raiz:", root.element())
print("Filho esquerdo da raiz:", tree.left(root).element())
print("O nó 2 é folha?", tree.is_leaf(tree.left(left)))
print("O nó 5 é folha?", tree.is_leaf(left))