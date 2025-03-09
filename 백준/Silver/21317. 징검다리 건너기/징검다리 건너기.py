import sys

N = int(sys.stdin.readline())

jump = [list(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]
e3 = int(sys.stdin.readline())
dp = [[float('inf') for _ in range(N)] for _ in range(2)]
dp[0][0], dp[1][0] = 0, 0

for i in range(N - 1):
    e1, e2 = jump[i]

    # not use e3
    dp[0][i + 1] = min(dp[0][i + 1], dp[0][i] + e1)
    if i + 2 < N:
        dp[0][i + 2] = min(dp[0][i + 2], dp[0][i] + e2)

    # already use e3
    dp[1][i + 1] = min(dp[1][i + 1], dp[1][i] + e1)
    if i + 2 < N:
        dp[1][i + 2] = min(dp[1][i + 2], dp[1][i] + e2)

    # use e3
    if i + 3 < N:
        dp[1][i + 3] = min(dp[1][i + 3], dp[0][i] + e3)


print(dp[0][-1] if dp[0][-1] < dp[1][-1] else dp[1][-1])