class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(myl):
    if myl == []:
        return None
    mid = len(myl) // 2
    mval = Node(myl[mid])
    lkids = myl[:mid]
    rkids = myl[(mid + 1):]

    if len(lkids) > 1:
        mval.left = build_tree(lkids)
    elif len(lkids) == 1:
        mval.left = Node(lkids[0])

    if len(rkids) > 1:
        mval.right = build_tree(rkids)
    elif len(rkids) == 1:
        mval.right = Node(rkids[0])

    return mval
if __name__ == '__main__':
    assert build_tree([2, 3]).left.val == 2
