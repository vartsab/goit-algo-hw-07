class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_min(node):
    current = node
    # Рухаємося вліво, доки є ліві дочірні вузли
    while current.left is not None:
        current = current.left
    return current.value

# Приклад використання:
root = Node(62.8)
root.left = Node(31.4)
root.right = Node(94.20)
root.left.left = Node(15.7)

min_value = find_min(root)
print(f"The minimum value in the tree is: {min_value}")
