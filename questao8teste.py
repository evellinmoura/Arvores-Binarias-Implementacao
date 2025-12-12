from questao3 import LinkedBinaryTree
from questao8 import replace_with_subtree_sum


if __name__ == "__main__":
    T = LinkedBinaryTree()

    r = T.add_root(1)
    a = T.add_left(r, 2)
    b = T.add_right(r, 3)

    T.add_left(a, 4)

    c = T.add_left(b, 5)
    T.add_right(b, 6)

    T.add_left(c, 7)
    T.add_right(c, 8)

    replace_with_subtree_sum(T)

    print("Preorder após substituição:", T.preorder())