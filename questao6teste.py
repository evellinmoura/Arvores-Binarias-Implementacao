from questao3 import LinkedBinaryTree
from questao6 import print_root_to_leaf_paths


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

    print_root_to_leaf_paths(T)