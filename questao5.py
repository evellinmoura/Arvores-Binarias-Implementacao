def is_sum_tree(tree):
    def check(p):
        if p is None:
            return True, 0

        if tree.is_leaf(p):
            return True, p.element()

        left_ok, left_sum = check(tree.left(p))
        right_ok, right_sum = check(tree.right(p))

        current_ok = p.element() == left_sum + right_sum
        total_sum = p.element() + left_sum + right_sum

        return left_ok and right_ok and current_ok, total_sum

    ok, _ = check(tree.root())
    return ok