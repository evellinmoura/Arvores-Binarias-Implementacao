def print_root_to_leaf_paths(tree):

    def backtrack(p, path):
        if p is None:
            return

        path.append(p.element())

        if tree.is_leaf(p):
            print(" -> ".join(map(str, path)))
        else:
            backtrack(tree.left(p), path)
            backtrack(tree.right(p), path)

        path.pop()

    backtrack(tree.root(), [])