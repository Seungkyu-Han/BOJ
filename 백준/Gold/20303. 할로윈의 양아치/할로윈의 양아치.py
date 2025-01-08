import sys

# union set
N, M, K = map(int, sys.stdin.readline().split())
candy = list(map(int, sys.stdin.readline().split()))

parent = [i for i in range(N)]
rank = [0 for i in range(N)]


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        if rank[root1] == rank[root2]:
            rank[root2] += 1
        parent[root1] = root2


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    union(u - 1, v - 1)

root_dict = dict()


for i in range(N):
    root = find(i)
    if root not in root_dict:
        root_dict[root] = [i]
    else:
        root_dict[root].append(i)


value_list = []

for key in root_dict.keys():
    if len(root_dict[key]) >= K:
        continue
    cur_value = 0
    for child in root_dict[key]:
        cur_value += candy[child]
    value_list.append([len(root_dict[key]), cur_value])


dp = [0 for _ in range(K)]

for value_candy in value_list:
    cur_value, cur_candy = value_candy
    for i in range(K - 1, cur_value - 1, -1):
        dp[i] = max(dp[i - cur_value] + cur_candy, dp[i])

print(dp[-1])