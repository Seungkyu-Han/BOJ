def solution(n, computers):
    
    parents = [i for i in range(n)]
    ranks = [0 for i in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                if find(i, parents) != find(j, parents):
                    union(i, j, parents, ranks)
    
    parent_set = set()
    
    for i in range(n):
        parent_set.add(find(i, parents))
    
    return len(parent_set)

def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(node1, node2, parent, rank):
    root1 = find(node1, parent)
    root2 = find(node2, parent)
    
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        if rank[root1] == rank[root2]:
            rank[root2] += 1
        parent[root1] = root2