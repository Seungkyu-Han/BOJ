import sys

N, M = map(int, sys.stdin.readline().split())

visited = [False for _ in range(N + 1)]
graph = {i: [] for i in range(1, N + 1)}
result = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for vertex in range(1, N + 1):
    if not visited[vertex]:

        result += 1
        need_visit = [vertex]
        visited[vertex] = True

        while need_visit:
            cur_vertex = need_visit.pop()

            for next_vertex in graph[cur_vertex]:
                if not visited[next_vertex]:
                    visited[next_vertex] = True
                    need_visit.append(next_vertex)

print(result)