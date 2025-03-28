import sys

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())

a_length, b_length = len(A), len(B)

dp = [[0 for _ in range(b_length)] for _ in range(a_length)]

result = 0

for a in range(a_length):
    for b in range(b_length):
        if A[a] == B[b]:
            if a == 0 or b == 0:
                dp[a][b] = 1
            else:
                dp[a][b] = dp[a - 1][b - 1] + 1

            result = max(result, dp[a][b])

print(result)