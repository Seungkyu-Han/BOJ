import heapq
import sys

N, M = map(int, sys.stdin.readline().split())

miro = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(M)]


need_visit = []
heapq.heappush(need_visit, [0, 0, 0])
visited = [[float('inf') for _ in range(N)] for _ in range(M)]
visited[0][0] = 0

while need_visit:

    cur_cnt, cur_n, cur_m = heapq.heappop(need_visit)

    if cur_n == N - 1 and cur_m == M - 1:
        print(cur_cnt)
        break

    if cur_cnt > visited[cur_m][cur_n]:
        continue

    for next_n, next_m in [[cur_n - 1, cur_m], [cur_n + 1, cur_m], [cur_n, cur_m - 1], [cur_n, cur_m + 1]]:
        if 0 <= next_n < N and 0 <= next_m < M:
            next_cnt = cur_cnt if miro[next_m][next_n] == 0 else cur_cnt + 1
            if visited[next_m][next_n] <= next_cnt:
                continue
            heapq.heappush(need_visit, [next_cnt, next_n, next_m])
            visited[next_m][next_n] = next_cnt
