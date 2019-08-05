from math import inf

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_bst(root):
    ll = -inf
    ul = inf
    if root is None:
        return True
    else:
        return recurs(root, ll, ul)

def recurs(node, ll, ul):
    lok = True
    rok = True
    if not (ll < node.val < ul):
        return False
    if node.left is not None:
        lok = recurs(node.left, ll, node.val)
    if node.right is not None:
        rok = recurs(node.right, node.val, ul)
    if (node.left is None) and (node.right is None):
        if not (ll < node.val < ul):
            return False
    return (lok and rok)

if __name__ == '__main__':
    root = Node(0)
    root.left = Node(-1)
    assert is_bst(root)
    ro
