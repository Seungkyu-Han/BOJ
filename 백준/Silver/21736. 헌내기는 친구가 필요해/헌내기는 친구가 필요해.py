import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

result = 0

graph = []

start_n, start_m = 0, 0

for i in range(N):
    input_graph = list(sys.stdin.readline().strip())
    for j in range(M):
        if input_graph[j] == 'I':
            start_n, start_m = i, j
    graph.append(input_graph)


need_visit = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
visited[start_n][start_m] = True

need_visit.append([start_n, start_m])

while need_visit:

    cur_n, cur_m = need_visit.popleft()

    for next_n, next_m in [[cur_n + 1, cur_m], [cur_n - 1, cur_m], [cur_n, cur_m - 1], [cur_n, cur_m + 1]]:
        if 0 <= next_n < N and 0 <= next_m < M and not visited[next_n][next_m] and graph[next_n][next_m] != 'X':
            if graph[next_n][next_m] == 'P':
                result += 1
            need_visit.append([next_n, next_m])
            visited[next_n][next_m] = True


print(result if result != 0 else "TT")