import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp = []

for i in range(N):
    result = 1
    for j in range(i):
        if dp[j] + 1 > result and A[j] < A[i]:
            result = dp[j] + 1
    dp.append(result)

print(max(dp))