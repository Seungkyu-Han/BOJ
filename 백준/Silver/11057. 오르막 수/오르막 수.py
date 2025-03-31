import sys

N = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][k] = (dp[i][k] + dp[i - 1][j]) % 10007
            
print(sum(dp[-1]) % 10007)