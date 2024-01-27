import sys

n = int(sys.stdin.readline().strip())

line = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)])

dp = [0 for i in range(n)]

for i in range(n):
    count = 1
    for t in range(i):
        if line[i][1] > line[t][1]:
            count = max(count, dp[t] + 1)
    dp[i] = count

print(n - max(dp))
