import sys

n, m = map(int, sys.stdin.readline().split())

parent = {i: i for i in range(n)}
rank = {i : 0 for i in range(n)}

result = 0


def find(target_node):
    if target_node != parent[target_node]:
        parent[target_node] = find(parent[target_node])
    return parent[target_node]


def union(v1, v2):
    #v1 으로 연결

    root1 = find(v1)
    root2 = find(v2)

    # root1으로 연결
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    # root2로 연결
    else:
        if rank[root1] == rank[root2]:
            rank[root2] += 1
        parent[root1] = root2


for i in range(m):

    u, v = map(int, sys.stdin.readline().split())

    root_u, root_v = find(u), find(v)


    if root_u == root_v and result == 0:
        result = i + 1

    union(u, v)


print(result)