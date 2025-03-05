import sys

def find(node: int, parent_dict: dict[int, int]) -> int:
    if node != parent_dict[node]:
        parent_dict[node] = find(parent_dict[node], parent_dict)
    return parent_dict[node]


def union(node_1: int, node_2: int, parent_dict: dict[int, int], rank_dict: dict[int, int]):

    root1 = find(node_1, parent_dict)
    root2 = find(node_2, parent_dict)

    if rank_dict[root1] > rank_dict[root2]:
        parent_dict[root2] = root1
    else:
        parent_dict[root1] = root2
        if rank_dict[root1] == rank_dict[root2]:
            rank_dict[root2] += 1


T = int(sys.stdin.readline())

for t in range(1, T + 1):
    n = int(sys.stdin.readline())

    k = int(sys.stdin.readline())

    rank: dict[int, int] = {i : 0 for i in range(n)}
    parent: dict[int, int] = {i: i for i in range(n)}

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())

        union(a, b, parent, rank)

    m = int(sys.stdin.readline())

    print(f'Scenario {t}:')

    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())

        if find(u, parent) == find(v, parent):
            print(1)
        else:
            print(0)
    print()
