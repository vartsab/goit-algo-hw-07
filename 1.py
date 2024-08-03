class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_max(node):
    current = node
    # Рухаємося вправо, доки є праві дочірні вузли
    while current.right is not None:
        current = current.right
    return current.value

# Приклад використання:
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.right = Node(4)

max_value = find_max(root)
print(f"The maximum value in the tree is: {max_value}")
