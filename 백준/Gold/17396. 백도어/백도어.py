import sys, heapq

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

graph = {i: [] for i in range(N)}

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())

    graph[a].append([b, t])
    graph[b].append([a, t])

need_visit = []
heapq.heappush(need_visit, [0, 0])

distances = [float('inf') for _ in range(N)]
distances[0] = 0

while need_visit:

    cur_node, cur_distance = heapq.heappop(need_visit)

    if cur_distance > distances[cur_node]:
        continue

    for next_node, next_distance in graph[cur_node]:
        if next_node == N - 1:
            distances[next_node] = min(distances[next_node], cur_distance + next_distance)
        elif distances[next_node] > distances[cur_node] + next_distance and A[next_node] == 0:
            heapq.heappush(need_visit, [next_node, cur_distance + next_distance])
            distances[next_node] = cur_distance + next_distance


if distances[-1] == float('inf'):
    print(-1)
else:
    print(distances[-1])