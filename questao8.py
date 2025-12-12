def replace_with_subtree_sum(tree):

    def postorder(p):
        if p is None:
            return 0

        left_sum = postorder(tree.left(p))
        right_sum = postorder(tree.right(p))

        old_value = p.element()
        tree.replace(p, left_sum + right_sum)

        return old_value + left_sum + right_sum

    postorder(tree.root())