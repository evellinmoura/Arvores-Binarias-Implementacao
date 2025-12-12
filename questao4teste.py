from questao3 import LinkedBinaryTree
from questao4 import trees_are_identical


if __name__ == "__main__":
    T1 = LinkedBinaryTree()
    T2 = LinkedBinaryTree()

    r1 = T1.add_root(10)
    a1 = T1.add_left(r1, 5)
    T1.add_right(r1, 20)
    T1.add_left(a1, 2)
    T1.add_right(a1, 7)

    r2 = T2.add_root(10)
    a2 = T2.add_left(r2, 5)
    T2.add_right(r2, 20)
    T2.add_left(a2, 2)
    T2.add_right(a2, 7)

    print("Árvores idênticas?", trees_are_identical(T1, T2))