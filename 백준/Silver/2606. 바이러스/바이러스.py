import sys

N = int(sys.stdin.readline().strip())

graph = {}

for i in range(N):
    graph[i+1] = []

for _ in range(int(sys.stdin.readline().strip())):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False for i in range(N + 1)]
visited[1] = True
need_visit = [1]

while need_visit:
    v = need_visit.pop(0)

    for w in graph[v]:
        if not visited[w]:
            visited[w] = True
            need_visit.append(w)

print(visited.count(True) - 1)