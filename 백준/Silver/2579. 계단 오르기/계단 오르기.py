import sys

N = int(sys.stdin.readline())

step = [0 for _ in range(300)]
dp = [0 for _ in range(300)]

for i in range(N):
    step[i] = int(sys.stdin.readline())

dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[0], step[1]) + step[2]

for i in range(3, N):
    dp[i] = max(dp[i - 2], dp[i - 3] + step[i - 1]) + step[i]

print(dp[N - 1])