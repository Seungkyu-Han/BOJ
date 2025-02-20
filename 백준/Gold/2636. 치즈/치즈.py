import sys

N, M = map(int, sys.stdin.readline().split())

cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cheese_cnt = 0

cur_time = 0

while True:

    cur_cheese_cnt = 0

    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                cur_cheese_cnt += 1

    if cur_cheese_cnt == 0:
        break

    cheese_cnt = cur_cheese_cnt
    cur_time += 1

    touched_cheese = set()

    need_visit = [[0, 0]]
    visited = [[False for _ in range(M)] for _ in range(N)]

    while need_visit:

        cur_n, cur_m = need_visit.pop()

        for next_n, next_m in [[cur_n + 1, cur_m], [cur_n - 1, cur_m], [cur_n, cur_m + 1], [cur_n, cur_m - 1]]:
            if 0 <= next_n < N and 0 <= next_m < M and not visited[next_n][next_m]:
                if cheese[next_n][next_m] == 0:
                    need_visit.append([next_n, next_m])
                    visited[next_n][next_m] = True
                else:
                    if (next_n, next_m) not in touched_cheese:
                        touched_cheese.add((next_n, next_m))


    for rm_n, rm_m in touched_cheese:
        cheese[rm_n][rm_m] = 0


print(cur_time)
print(cheese_cnt)