import sys

for _ in range(int(sys.stdin.readline().strip())):

    M, N, K = map(int, sys.stdin.readline().split())

    land = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        m, n = map(int, sys.stdin.readline().split())
        land[n][m] = 1

    result = 0

    visited = [[False for _ in range(M)] for _ in range(N)]

    for n in range(N):
        for m in range(M):
            if visited[n][m] or land[n][m] == 0:
                continue

            result += 1

            need_visit = [[n, m]]
            visited[n][m] = False

            while need_visit:

                cur_n, cur_m = need_visit.pop()

                for next_n, next_m in [[cur_n, cur_m + 1], [cur_n, cur_m - 1], [cur_n + 1, cur_m], [cur_n - 1, cur_m]]:
                    if 0 <= next_n < N and 0 <= next_m < M:
                        if land[next_n][next_m] == 1 and visited[next_n][next_m] is False:
                            need_visit.append([next_n, next_m])
                            visited[next_n][next_m] = True
    print(result)