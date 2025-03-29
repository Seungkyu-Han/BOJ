import sys, heapq

N, M = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(N + 1)}

for _ in range(M + 1):
    A, B, C = map(int, sys.stdin.readline().split())

    graph[A].append([B, C])
    graph[B].append([A, C])


def min_distance():
    visited = set()
    need_visit = []
    heapq.heappush(need_visit, [-1, 0])

    distance = 0

    # 내리막은 0, 오르막은 1
    while need_visit:

        cur_distance, cur_node = heapq.heappop(need_visit)

        if cur_node in visited:
            continue

        visited.add(cur_node)

        if cur_distance == 1:
            distance += 1

        for next_node, next_distance in graph[cur_node]:
            if next_node not in visited:
                if next_distance == 0:
                    heapq.heappush(need_visit, [1, next_node])
                else:
                    heapq.heappush(need_visit, [0, next_node])
    return distance

def max_distance():
    visited = set()
    need_visit = []
    heapq.heappush(need_visit, [-1, 0])

    distance = 0

    # 내리막은 1, 오르막은 0
    while need_visit:

        cur_distance, cur_node = heapq.heappop(need_visit)

        if cur_node in visited:
            continue

        visited.add(cur_node)

        if cur_distance == 0:
            distance += 1

        for next_node, next_distance in graph[cur_node]:
            if next_node not in visited:
                if next_distance == 1:
                    heapq.heappush(need_visit, [1, next_node])
                else:
                    heapq.heappush(need_visit, [0, next_node])
    return distance

print(max_distance() ** 2 - min_distance() ** 2)
