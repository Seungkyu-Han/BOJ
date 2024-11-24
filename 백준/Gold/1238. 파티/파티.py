import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

graph = [[float('inf') for _ in range(N)] for _ in range(N)]

for _ in range(M):
    v, u, weight = map(int, sys.stdin.readline().split())
    graph[v-1][u-1] = weight

go_to_X = {i:float('inf') for i in range(N)}
go_from_X = {i:float('inf') for i in range(N)}
go_to_X[X - 1], go_from_X[X - 1] = 0, 0

need_visit = []
heapq.heappush(need_visit, [0, X - 1])

while need_visit:
    cur_weight, cur_node = heapq.heappop(need_visit)

    if cur_weight > go_to_X[cur_node]:
        continue

    for i in range(N):
        if go_to_X[i] > cur_weight + graph[i][cur_node]:
            go_to_X[i] = cur_weight + graph[i][cur_node]
            heapq.heappush(need_visit, (cur_weight + graph[i][cur_node], i))


heapq.heappush(need_visit, [0, X - 1])

while need_visit:

    cur_weight, cur_node = heapq.heappop(need_visit)

    if cur_weight > go_from_X[cur_node]:
        continue

    for i in range(N):
        if go_from_X[i] > cur_weight + graph[cur_node][i]:
            go_from_X[i] = cur_weight + graph[cur_node][i]
            heapq.heappush(need_visit, (cur_weight + graph[cur_node][i], i))

result = 0

for i in range(N):
    result = max(result, go_from_X[i] + go_to_X[i])

print(result)