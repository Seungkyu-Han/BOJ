import sys

N, M = map(int, sys.stdin.readline().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(N + 1)] for _ in range(N)]

for i1 in range(N):
    for i2 in range(1, N + 1):
        dp[i1][i2] = dp[i1][i2 - 1] + table[i1][i2 - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    result = 0
    for x in range(x1 - 1, x2):
        result += (dp[x][y2] - dp[x][y1 - 1])

    print(result)