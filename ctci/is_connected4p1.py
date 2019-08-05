
def recurs(src, dest, adj, visited):
    for node in adj[src]:
        if node not in visited:
            visited.add(node)
            if node == dest:
                return True
            res = recurs(node, dest, adj, visited)
            if res == True:
                return True
    return False

def is_conn(src, dest, adj):
    if src == dest:
        return True
    visited = set()
    for node in adj[src]:
        visited.add(src)
        res = recurs(node, dest, adj, visited)
        if res == True:
            return True
    return False

if __name__ == '__main__':
    adj = {'A':['B'],
            'B':['C','D'],
            'C':['B'],
            'D':['B'],
            'E':['F'],
            'F':['E','G'],
            'G':['F']}
    assert is_conn('A', 'D', adj)
    assert not is_conn('A', 'G', adj)
