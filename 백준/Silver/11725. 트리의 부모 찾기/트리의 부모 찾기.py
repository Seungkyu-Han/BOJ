import sys

N = int(sys.stdin.readline())

graph = {i + 1: [] for i in range(N)}

parent = {i + 1: 0 for i in range(N)}
parent[1] = 1

for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())

    graph[v1].append(v2)
    graph[v2].append(v1)


need_visit = [1]

while need_visit:

    cur_node = need_visit.pop()

    for next_node in graph[cur_node]:
        if parent[next_node] == 0:
            parent[next_node] = cur_node
            need_visit.append(next_node)


for i in range(2, N + 1):
    print(parent[i])