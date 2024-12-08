import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def bfs(cur_graph, n, m):
    bfs_cur_graph = [row[:] for row in cur_graph]

    for cur_n in range(n):
        for cur_m in range(m):
            if bfs_cur_graph[cur_n][cur_m] == 2:
                need_visit = deque([[cur_n, cur_m]])
                while need_visit:
                    visited_n, visited_m = need_visit.popleft()

                    for next_n, next_m in [[visited_n - 1, visited_m], [visited_n + 1, visited_m], [visited_n, visited_m - 1], [visited_n, visited_m + 1]]:
                        if 0 <= next_n < n and 0 <= next_m < m and bfs_cur_graph[next_n][next_m] == 0:
                            bfs_cur_graph[next_n][next_m] = 2
                            need_visit.append([next_n, next_m])

    return sum(row.count(0) for row in bfs_cur_graph)


def back_tracking(cur_graph, cur_n, cur_m, cur_wall, n, m):

    if cur_wall == 3:
        return bfs(cur_graph, n, m)

    result = 0

    for next_n in range(cur_n, n):
        for next_m in range(cur_m if next_n == cur_n else 0, m):
            if cur_graph[next_n][next_m] == 0:
                cur_graph[next_n][next_m] = 1
                result = max(result, back_tracking(cur_graph, next_n, next_m, cur_wall + 1, n, m))
                cur_graph[next_n][next_m] = 0
    return result

print(back_tracking(graph, 0, 0, 0, N, M))