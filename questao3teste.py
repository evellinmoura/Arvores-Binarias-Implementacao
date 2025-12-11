from questao3 import LinkedBinaryTree
tree = LinkedBinaryTree()
root = tree.add_root(10)
left = tree.add_left(root, 5)
right = tree.add_right(root, 20)

tree.add_left(left, 2)
tree.add_right(left, 7)

print("Preorder Traversal:", tree.preorder())  # [10, 5, 2, 7, 20]
print("Inorder Traversal:", tree.inorder())    # [2, 5, 7, 10, 20]
print("Postorder Traversal:", tree.postorder()) # [2, 7, 5, 20, 10]
