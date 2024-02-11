import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

ripe = deque()

for m in range(M):
    for n in range(N):
        if tomato[m][n] == 1:
            ripe.append([0, m, n])

max_result = 0

while ripe:

    cur_cnt, cur_m, cur_n = ripe.popleft()

    max_result = max(max_result, cur_cnt)

    for next_m, next_n in [[cur_m, cur_n + 1], [cur_m, cur_n - 1], [cur_m + 1, cur_n], [cur_m - 1, cur_n]]:
        if 0 <= next_m < M and 0 <= next_n < N and tomato[next_m][next_n] == 0:
            tomato[next_m][next_n] = 1
            ripe.append([cur_cnt + 1, next_m, next_n])


is_finish = True

for m in range(M):
    for n in range(N):
        if tomato[m][n] == 0:
            is_finish = False
            break
    if not is_finish:
        break

print(max_result if is_finish else -1)