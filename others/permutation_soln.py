def permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        #try every possibility for A[i]
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]

            #generate all permutations for A[i + 1:]
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result

import pdb; pdb.set_trace() # BREAKPOINT
permutations([7, 3, 5])
print('win')
