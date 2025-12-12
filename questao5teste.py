
from questao3 import LinkedBinaryTree
from questao5 import  is_sum_tree


if __name__ == "__main__":
    T = LinkedBinaryTree()

    r = T.add_root(44)
    a = T.add_left(r, 9)
    b = T.add_right(r, 13)

    T.add_left(a, 4)
    T.add_right(a, 5)

    T.add_left(b, 6)
    T.add_right(b, 7)

    print("É árvore soma?", is_sum_tree(T))