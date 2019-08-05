def rev_str(mys):
    myl = list(mys)
    start = 0
    end = -1
    while start < len(myl) // 2:
        myl[start], myl[end] = myl[end], myl[start]
        start += 1
        end -= 1
    return ''.join(x for x in myl)

assert rev_str('cat') == 'tac'
assert rev_str('') == ''
assert rev_str('toby') == 'ybot'
