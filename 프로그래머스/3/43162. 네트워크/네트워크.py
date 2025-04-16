def solution(n, computers):
    answer = 0
    
    parent_set = set()
    
    rank = [0 for _ in range(n)]
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            
            if computers[i][j] == 0:
                continue
            
            union(i, j, parent, rank)
    
    for i in range(n):
        parent_set.add(find(i, parent))
    
    
    return len(parent_set)

def find(node: int, parent: list):
    if node != parent[node]:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(node1: int, node2: int, parent: list, rank: list):
    root1: int = find(node1, parent)
    root2: int = find(node2, parent)
    
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
    
    