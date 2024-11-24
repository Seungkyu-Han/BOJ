import sys
import heapq

N, E = map(int, sys.stdin.readline().split())

graph = {n + 1: [] for n in range(N)}

for _ in range(E):
    v, u, weight = map(int, sys.stdin.readline().split())

    graph[v].append((u, weight))
    graph[u].append((v, weight))

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(cur_graph, start):
    distances = {n + 1: float('inf') for n in range(N)}
    need_visit = []

    heapq.heappush(need_visit, [0, start])

    while need_visit:

        cur_distance, cur_node = heapq.heappop(need_visit)

        if distances[cur_node] < cur_distance:
            continue


        for next_node, next_distance in cur_graph[cur_node]:
            if next_distance + cur_distance < distances[next_node]:
                distances[next_node] = next_distance + cur_distance
                heapq.heappush(need_visit, [next_distance + cur_distance, next_node])

    distances[start] = 0
    return distances

path_v1 = dijkstra(graph, v1)
path_v2 = dijkstra(graph, v2)

result = min(path_v1[1] + path_v2[N], path_v1[N] + path_v2[1]) + path_v1[v2]

print(result if result != float('inf') else -1)