import sys

n, m = map(int, sys.stdin.readline().split())

square = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if square[i][j] == 1:
            dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1


result = 0

for i in range(n):
    for j in range(m):
        result = max(dp[i + 1][j + 1], result)

print(result ** 2)