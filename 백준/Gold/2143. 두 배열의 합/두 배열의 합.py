import sys

T = int(sys.stdin.readline())

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().split()))

dp = dict()

acc_a = [0]
acc_b = [0]

result = 0

for i in range(n):
    acc_a.append(acc_a[-1] + A[i])

for i in range(m):
    acc_b.append(acc_b[-1] + B[i])

for i in range(n + 1):
    for j in range(i + 1, n + 1):
        value = acc_a[j] - acc_a[i]
        if value in dp:
            dp[value] += 1
        else:
            dp[value] = 1

for i in range(m + 1):
    for j in range(i + 1, m + 1):
        value =  T - (acc_b[j] - acc_b[i])
        if value in dp:
            result += dp[value]

print(result)