def identical(t1, p1, t2, p2):
    if p1 is None and p2 is None:
        return True

    if p1 is None or p2 is None:
        return False

    if p1.element() != p2.element():
        return False

    return (identical(t1, t1.left(p1), t2, t2.left(p2)) and
            identical(t1, t1.right(p1), t2, t2.right(p2)))


def trees_are_identical(t1, t2):
    return identical(t1, t1.root(), t2, t2.root())