class Node:
    def __init__(self, element, parent=None, left=None, right=None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right


class LinkedBinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def root(self):
        return self._root
    
    def parent(self, node):
        return node.parent
    
    def left(self, node):
        return node.left
    
    def right(self, node):
        return node.right
    
    def num_children(self, node):
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count
    
    def is_root(self, node):
        return node == self._root
    
    def is_leaf(self, node):
        return self.num_children(node) == 0
    
    def add_root(self, element):
        if self._root is not None:
            raise ValueError("Root already exists")
        self._root = Node(element)
        self._size = 1
        return self._root
    
    def add_left(self, node, element):
        if node.left is not None:
            raise ValueError("Left child already exists")
        node.left = Node(element, parent=node)
        self._size += 1
        return node.left
    
    def add_right(self, node, element):
        if node.right is not None:
            raise ValueError("Right child already exists")
        node.right = Node(element, parent=node)
        self._size += 1
        return node.right
    
    def replace(self, node, element):
        old = node.element
        node.element = element
        return old
    
    def delete(self, node):
        if self.num_children(node) == 2:
            raise ValueError("Node has two children")
        
        child = node.left if node.left else node.right
        
        if child is not None:
            child.parent = node.parent
        
        if node == self._root:
            self._root = child
        else:
            parent = node.parent
            if node == parent.left:
                parent.left = child
            else:
                parent.right = child
        
        self._size -= 1
        node.parent = node.left = node.right = None
        return node.element
    
    def attach(self, node, tree1, tree2):
        if not self.is_leaf(node):
            raise ValueError("Node must be a leaf")
        
        if not type(self) is type(tree1) is type(tree2):
            raise TypeError("Tree types must match")
        
        self._size += len(tree1) + len(tree2)
        
        if not tree1.is_empty():
            node.left = tree1._root
            tree1._root.parent = node
            tree1._root = None
            tree1._size = 0
        
        if not tree2.is_empty():
            node.right = tree2._root
            tree2._root.parent = node
            tree2._root = None
            tree2._size = 0
    
    def preorder(self, node=None):
        if node is None:
            node = self._root
        if node is not None:
            yield node
            if node.left is not None:
                for child in self.preorder(node.left):
                    yield child
            if node.right is not None:
                for child in self.preorder(node.right):
                    yield child
    
    def inorder(self, node=None):
        if node is None:
            node = self._root
        if node is not None:
            if node.left is not None:
                for child in self.inorder(node.left):
                    yield child
            yield node
            if node.right is not None:
                for child in self.inorder(node.right):
                    yield child
    
    def postorder(self, node=None):
        if node is None:
            node = self._root
        if node is not None:
            if node.left is not None:
                for child in self.postorder(node.left):
                    yield child
            if node.right is not None:
                for child in self.postorder(node.right):
                    yield child
            yield node
    
    def height(self, node=None):
        if node is None:
            node = self._root
        if self.is_leaf(node):
            return 0
        return 1 + max(self.height(c) for c in [node.left, node.right] if c is not None)
    
    def __str__(self):
        if self.is_empty():
            return "Empty Tree"
        return self._str_helper(self._root, "", True)
    
    def _str_helper(self, node, prefix, is_tail):
        if node is None:
            return ""
        
        result = prefix + ("└── " if is_tail else "├── ") + str(node.element) + "\n"
        
        children = []
        if node.left is not None:
            children.append(node.left)
        if node.right is not None:
            children.append(node.right)
        
        for i, child in enumerate(children):
            extension = "    " if is_tail else "│   "
            result += self._str_helper(child, prefix + extension, i == len(children) - 1)
        
        return result


print("=" * 60)
print("ÁRVORE BINÁRIA ENCADEADA - LinkedBinaryTree")
print("=" * 60)

tree = LinkedBinaryTree()

print("\nCriando árvore de exemplo:")
root = tree.add_root("Baltimore")
print(f"Raiz: {root.element}")

ny = tree.add_left(root, "New York")
print(f"Filho esquerdo da raiz: {ny.element}")

providence = tree.add_right(root, "Providence")
print(f"Filho direito da raiz: {providence.element}")

seattle = tree.add_left(ny, "Seattle")
print(f"Filho esquerdo de New York: {seattle.element}")

miami = tree.add_right(ny, "Miami")
print(f"Filho direito de New York: {miami.element}")

print(f"\nTamanho da árvore: {len(tree)}")

print("\nVisualizando a árvore:")
print(tree)

print("Percurso em pré-ordem:")
print(" -> ".join([node.element for node in tree.preorder()]))

print("\nPercurso em ordem simétrica:")
print(" -> ".join([node.element for node in tree.inorder()]))

print("\nPercurso em pós-ordem:")
print(" -> ".join([node.element for node in tree.postorder()]))

print(f"\nAltura da árvore: {tree.height()}")

print("\n" + "=" * 60)
print("TESTE INTERATIVO")
print("=" * 60)

while True:
    print("\nDigite 'sair' para encerrar")
    print("Digite valores separados por espaço para criar nova árvore:")
    entrada = input("→ ")
    
    if entrada.lower() == 'sair':
        print("Encerrando...")
        break
    
    if not entrada.strip():
        continue
    
    valores = entrada.split()
    tree2 = LinkedBinaryTree()
    
    if valores:
        root = tree2.add_root(valores[0])
        nodes = [root]
        i = 1
        
        while i < len(valores) and nodes:
            current = nodes.pop(0)
            
            if i < len(valores):
                left = tree2.add_left(current, valores[i])
                nodes.append(left)
                i += 1
            
            if i < len(valores):
                right = tree2.add_right(current, valores[i])
                nodes.append(right)
                i += 1
    
    print("\nÁrvore criada:")
    print(tree2)
    print(f"Tamanho: {len(tree2)}")
    print(f"Altura: {tree2.height()}")
    print("Pré-ordem:", " -> ".join([node.element for node in tree2.preorder()]))