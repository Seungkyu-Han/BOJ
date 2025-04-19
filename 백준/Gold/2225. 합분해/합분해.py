import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(N + 1)] for _ in range(K)]

for i in range(N + 1):
    dp[0][i] = 1

for index in range(K - 1):

    for i in range(N + 1):
        for j in range(N + 1 - i):
            dp[index+1][i + j] = (dp[index+1][i + j] + dp[index][i]) % 1000000000

print(dp[-1][-1])