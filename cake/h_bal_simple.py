"""
Module to determine whether or not a binary tree is height balanced. 
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recurs(node, depth):
    left_height = depth
    right_height = depth
    tree_balanced = True
    if node.left is not None:
        left_height, balanced = recurs(node.left, depth + 1)
        if not balanced:
            tree_balanced = balanced
    if node.right is not None:
        right_height, balanced = recurs(node.right, depth + 1)
        if not balanced:
            tree_balanced = balanced
    if tree_balanced:
        tree_balanced = abs(left_height - right_height) <= 1
    return max(right_height, left_height), tree_balanced

def isBalanced(root):
    if root is None:
        return True
    tree_balanced = True
    left_height = 0
    right_height = 0
    if root.left is not None:
        left_height, balanced = recurs(root.left, 1)
        if not balanced:
            tree_balanced = balanced
    if root.right is not None:
        right_height, balanced = recurs(root.right, 1)
        if not balanced:
            tree_balanced = balanced
    if tree_balanced:
        tree_balanced = abs(left_height - right_height) <= 1
    return tree_balanced

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
