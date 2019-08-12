def get_parens(n):
    j = 1
    if n == 0:
        return []
    valid = set(['()'])
    while j < n:
        temp = set()
        for prev_ans in valid:
            temp.add(prev_ans + '()')
            temp.add('()' + prev_ans)
            temp.add('(' + prev_ans + ')')
        valid = temp
        j += 1
    return list(valid)

if __name__ == '__main__':
    assert set(['()()', '(())']) == set(get_parens(2))
    assert set(['()']) == set(get_parens(1))
