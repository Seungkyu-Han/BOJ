import sys

N, M = map(int, sys.stdin.readline().split())

ice = []

for i in range(N):
    ice.append(list(map(int, sys.stdin.readline().split())))

year = 0

while True:
    piece = 0

    visited = set()

    for n in range(N):
        for m in range(M):
            if ice[n][m] == 0 or (n, m) in visited:
                continue
            piece += 1
            visited.add((n, m))
            need_visit = [[n, m]]

            while need_visit:

                cur_n, cur_m = need_visit.pop()

                for next_n, next_m in [[cur_n - 1, cur_m], [cur_n + 1, cur_m], [cur_n, cur_m - 1], [cur_n, cur_m + 1]]:
                    if 0 <= next_n < N and 0 <= next_m < M and ice[next_n][next_m] != 0 and (next_n, next_m) not in visited:
                        need_visit.append([next_n, next_m])
                        visited.add((next_n, next_m))

    if piece == 0:
        print(0)
        break
    elif piece >= 2:
        print(year)
        break

    year += 1
    #melt
    this_year = [[0 for _ in range(M)] for _ in range(N)]

    for n in range(N):
        for m in range(M):
            if ice[n][m] == 0:
                continue
            point = 0
            if n - 1 >= 0 and ice[n - 1][m] == 0:
                point += 1
            if n + 1 < N and ice[n + 1][m] == 0:
                point += 1
            if m - 1 >= 0 and ice[n][m - 1] == 0:
                point += 1
            if m + 1 < M and ice[n][m + 1] == 0:
                point += 1
            this_year[n][m] = max(0, ice[n][m] - point)

    for n in range(N):
        for m in range(M):
            ice[n][m] = this_year[n][m]

