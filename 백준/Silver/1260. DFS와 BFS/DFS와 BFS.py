import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1][v2] = True
    graph[v2][v1] = True

visited = [False for _ in range(N + 1)]

need_visit = deque()
need_visit.append(V)

while need_visit:

    v = need_visit.popleft()
    if visited[v]:
        continue
    visited[v] = True
    print(v, end=' ')

    for i in range(N, 0, -1):
        if graph[v][i] and visited[i] == False:
            need_visit.appendleft(i)
print()


visited = [False for _ in range(N + 1)]

need_visit = deque()
need_visit.append(V)

while need_visit:

    v = need_visit.pop()
    if visited[v]:
        continue
    visited[v] = True
    print(v, end=' ')

    for i in range(1, N + 1):
        if graph[v][i] and visited[i] == False:
            need_visit.appendleft(i)
print()
