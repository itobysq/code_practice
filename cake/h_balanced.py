class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recurs(node, prev_bal):
    if (node.right is None) and (node.left is None):
        return True
    if (node.right is not None):
        right = recurs(node.right, prev_bal + 1)
    if (node.left is not None):
        left = recurs(node.right, prev_bal + 1)
    if abs(left - right) > 1
        return False
    else:
        return True

def is_h_balanced(node):
    imbal = 0
    return recurs(node, imbal)

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.left = Node(0)
    root.left.right = Node(2)
    assert is_h_balanced(root) == False
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    assert is_h_balanced(root)
    assert is_h_balanced(Node(88))
