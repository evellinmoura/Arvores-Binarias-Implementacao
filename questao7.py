def ancestors(tree, p):
    result = []
    current = tree.parent(p)

    while current is not None:
        result.append(current.element())
        current = tree.parent(current)

    return result