class LinkedBinaryTree:
    
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be a Position type")
        if p._container is not self:
            raise ValueError("Position does not belong to this tree")
        if p._node._parent is p._node:
            raise ValueError("Position is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return self._size == 0

    def add_root(self, element):
        if self._root is not None:
            raise ValueError("Root already exists")
        self._root = self._Node(element)
        self._size = 1
        return self._make_position(self._root)

    def add_left(self, p, element):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child already exists")
        node._left = self._Node(element, parent=node)
        self._size += 1
        return self._make_position(node._left)

    def add_right(self, p, element):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child already exists")
        node._right = self._Node(element, parent=node)
        self._size += 1
        return self._make_position(node._right)

    def replace(self, p, element):
        node = self._validate(p)
        old = node._element
        node._element = element
        return old

    def delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Cannot delete node with two children")
        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if parent._left is node:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  
        return node._element

    # ------------------------ Traversals ----------------------------

    def preorder(self):
        result = []
        if self._root is not None:
            self._preorder_subtree(self._root, result)
        return result

    def _preorder_subtree(self, node, result):
        result.append(node._element)
        if node._left is not None:
            self._preorder_subtree(node._left, result)
        if node._right is not None:
            self._preorder_subtree(node._right, result)

    def inorder(self):
        result = []
        if self._root is not None:
            self._inorder_subtree(self._root, result)
        return result

    def _inorder_subtree(self, node, result):
        
        if node._left is not None:
            self._inorder_subtree(node._left, result)
        result.append(node._element)
        if node._right is not None:
            self._inorder_subtree(node._right, result)

    def postorder(self):
        
        result = []
        if self._root is not None:
            self._postorder_subtree(self._root, result)
        return result

    def _postorder_subtree(self, node, result):
        
        if node._left is not None:
            self._postorder_subtree(node._left, result)
        if node._right is not None:
            self._postorder_subtree(node._right, result)
        result.append(node._element)
