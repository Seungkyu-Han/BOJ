import sys
from _collections import deque

N, M = map(int, sys.stdin.readline().split())

cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count = 0

for cheese_slice in cheese:
    count += cheese_slice.count(1)

result = 0

while count > 0:
    touched = set()
    melted = set()
    visited = [[False for _ in range(M)] for _ in range(N)]

    need_visit = deque()

    # n, m
    need_visit.append([0, 0])
    visited[0][0] = True

    while need_visit:

        cur_n, cur_m = need_visit.popleft()

        for next_n, next_m in [[cur_n - 1, cur_m], [cur_n + 1, cur_m], [cur_n, cur_m - 1], [cur_n, cur_m + 1]]:
            if 0 <= next_n < N and 0 <= next_m < M and not visited[next_n][next_m]:
                if cheese[next_n][next_m] == 0:
                    visited[next_n][next_m] = True
                    need_visit.append([next_n, next_m])
                else:
                    if (next_n, next_m) not in touched:
                        touched.add((next_n, next_m))
                    else:
                        melted.add((next_n, next_m))
                        visited[next_n][next_m] = True


    for melted_n, melted_m in melted:
        cheese[melted_n][melted_m] = 0
        count -= 1
    result += 1

print(result)