import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp_left = [1 for _ in range(N)]
dp_right = [1 for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_left[i] = max(dp_left[j] + 1, dp_left[i])

for i in range(N):
    for j in range(N - 1, N - 1 - i, -1):
        index = N - 1 - i
        if A[index] > A[j]:
            dp_right[index] = max(dp_right[j] + 1, dp_right[index])

for i in range(N):
    dp[i] = dp_left[i] + dp_right[i] - 1

print(max(dp))