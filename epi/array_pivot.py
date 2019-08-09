def pivot(A, i):
    tar = A[i]
    lhp = 0
    for idx, val in enumerate(A):
        if val < tar:
            A[idx], A[lhp] = A[lhp], A[idx]
            lhp += 1
    rhp = len(A) - 1
    for idx, val in enumerate(reversed(A)):
        if val > tar:
            A[len(A) - 1 - idx], A[rhp] = A[rhp], A[len(A) - 1 - idx]
            rhp -= 1

    return A

if __name__ == '__main__':
    test = [0, 1, 2, 0, 2, 1, 1]
    assert pivot(test, 1) == [0, 0, 1, 1, 1, 2, 2]
