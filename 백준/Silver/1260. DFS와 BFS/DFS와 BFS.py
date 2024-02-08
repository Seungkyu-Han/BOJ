import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = [[False for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    V1, V2 = map(int, sys.stdin.readline().split())
    graph[V1-1][V2-1] = True
    graph[V2-1][V1-1] = True

DFS, BFS = [False for i in range(N)], [False for i in range(N)]
to_visit = [V-1]

while to_visit:
    cur_node = to_visit.pop(0)
    if DFS[cur_node]:
        continue
    save_to_visit = []
    for i in range(N):
        if graph[cur_node][i] and not DFS[i]:
            save_to_visit.append(i)

    to_visit = save_to_visit + to_visit

    print(cur_node + 1, end=' ')
    DFS[cur_node] = True

print()

to_visit = [V-1]

while to_visit:
    cur_node = to_visit.pop(0)
    if BFS[cur_node]:
        continue

    for i in range(N):
        if graph[cur_node][i] and not BFS[i]:
            to_visit.append(i)

    print(cur_node + 1, end=' ')
    BFS[cur_node] = True