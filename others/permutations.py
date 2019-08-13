def permutations(to_visit):
    """
    Args:
        to_visit (list): 1d array of lists
    Returns:
        perms (list): list of all permutations
    """
    if to_visit == []:
        return [[]]

    combos = []
    for dest in to_visit:
        next_dest = to_visit.pop()
        child = permutations(to_visit)
        child.append(next_dest)
        combos.append(child)
    return child

ans = permutations([1, 2])
import pdb; pdb.set_trace() # BREAKPOINT
print('win')
