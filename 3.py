class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def sum_tree(node):
    if node is None:
        return 0
    # Рекурсивно обчислюємо суму лівого та правого піддерев і додаємо значення поточного вузла
    return node.value + sum_tree(node.left) + sum_tree(node.right)

# Приклад використання:
root = Node(19760)
root.left = Node(9880)
root.right = Node(29640)
root.left.left = Node(4940)
root.left.right = Node(14820)

total_sum = sum_tree(root)
print(f"The sum of all values in the tree is: {total_sum}")
