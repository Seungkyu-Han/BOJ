N = int(input())

dp = [float('inf') for i in range(max(6, N + 1))]

dp[3], dp[5] = 1, 1

for i in range(6, N + 1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(dp[N] if dp[N] != float('inf') else -1)