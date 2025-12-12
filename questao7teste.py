from questao3 import LinkedBinaryTree
from questao7 import ancestors


if __name__ == "__main__":
    T = LinkedBinaryTree()

    r = T.add_root(1)
    a = T.add_left(r, 2)
    b = T.add_right(r, 3)

    T.add_left(a, 4)
    T.add_right(a, 5)

    c = T.add_left(b, 6)
    d = T.add_right(b, 7)

    T.add_left(c, 8)
    T.add_right(d, 9)

    print("Ancestrais do nó 9:", ancestors(T, T.right(d)))
    print("Ancestrais do nó 6:", ancestors(T, c))
    print("Ancestrais do nó 5:", ancestors(T, T.right(a)))