class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recurs(node, depth):
    lh = depth
    rh = depth
    tbal = True
    if node.left is not None:
        lh, bal = recurs(node.left, depth + 1)
        if not bal:
            tbal = bal
    if node.right is not None:
        rh, bal = recurs(node.right, depth + 1)
        if not bal:
            tbal = bal
    if tbal:
        tbal = abs(lh - rh) <= 1
    return max(rh, lh), tbal

def isBalanced(root):
    if root is None:
        return True
    tbal = True
    lh = 0
    rh = 0
    if root.left is not None:
        lh, bal = recurs(root.left, 1)
        if not bal:
            tbal = bal
    if root.right is not None:
        rh, bal = recurs(root.right, 1)
        if not bal:
            tbal = bal
    if tbal:
        tbal = abs(lh - rh) <= 1
    return tbal

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(2)
    assert isBalanced(root) == False
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    assert isBalanced(root)
    assert isBalanced(Node(88))
