from collections import deque
import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

village = [0] + list(map(int, sys.stdin.readline().split()))

graph = {i: [] for i in range(1, N + 1)}
depth = {i: -1 for i in range(1, N + 1)}
depth[1] = 0

for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)


# first: marked_prev_node
# second: not marked_prev_node
def dp(prev_node, cur_node) -> list[int]:

    if len(graph[cur_node]) == 1 and prev_node in graph[cur_node]:
        return [village[cur_node], 0]

    marked_prev_node, not_marked_prev_node = 0, 0

    for next_node in graph[cur_node]:
        if next_node != prev_node:
            marked_prev_node_result, not_marked_prev_node_result = dp(cur_node, next_node)
            marked_prev_node += max(marked_prev_node_result, not_marked_prev_node_result)
            not_marked_prev_node += not_marked_prev_node_result

    return [village[cur_node] + not_marked_prev_node, max(marked_prev_node, not_marked_prev_node)]

print(max(dp(0, 1)))