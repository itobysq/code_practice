def merge_ranges(tups):
    if tups == []:
        return []
    if len(tups) == 1:
        return tups
    pt = 0
    tups = sorted(tups, key=lambda x: x[0])

    final = []
    while pt < len(tups) - 1:
        if tups[pt][1] < tups[pt+1][0]:
            final.append(tups[pt])
        else:
            tups[pt+1] = (tups[pt][0], max(tups[pt][1], tups[pt+1][1]))
        pt += 1
    final.append(tups[pt])
    return final

if __name__ == '__main__':
    assert merge_ranges([(0,1),(3,5),(4,8)]) == [(0,1),(3,8)]
    assert merge_ranges([(0,1)]) == [(0,1)]
    assert merge_ranges([(0,5),(0,3),(0,9)]) == [(0,9)]
