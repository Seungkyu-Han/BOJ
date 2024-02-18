import sys
from collections import deque

n = int(sys.stdin.readline().strip())

node = {i: [] for i in range(n)}

for i in range(n - 1):
    start, end, weight = map(int, sys.stdin.readline().split())

    node[start - 1].append([end - 1, weight])
    node[end - 1].append([start - 1, weight])

result = 0

for i in range(n):
    cur_result = 0
    visited = [False for _ in range(n)]
    need_visit = deque()
    need_visit.append([0, i])
    visited[i] = True

    while need_visit:

        cur_weight, cur_node = need_visit.popleft()

        cur_result = max(cur_result, cur_weight)

        for next_node, next_weight in node[cur_node]:
            if visited[next_node] is False:
                visited[next_node] = True
                need_visit.append([cur_weight + next_weight, next_node])

    result = max(result, cur_result)

print(result)