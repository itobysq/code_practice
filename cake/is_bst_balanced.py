"""
Module to determine whether or not a binary tree is height balanced. Time
complexity is O(n). Space complexity is O(h)
"""

class Node():
    """
    Binary tree node
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recurs(node, depth):
    """
    Recursive part checks if left subtree is balanced, right subtree is balanced,
    and if the difference in the subree height is <= 1
    """
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

def is_balanced(root):
    """
    Top level function
    """
    if root is None:
        return True
    height, balanced = recurs(root, 0)
    return balanced

if __name__ == '__main__':
    """
    Examples
    """
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(2)
    assert not is_balanced(root)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    assert is_balanced(root)
    assert is_balanced(Node(88))
