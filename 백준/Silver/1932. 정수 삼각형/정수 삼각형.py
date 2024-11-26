import sys

N = int(sys.stdin.readline())

triangle = []

for _ in range(N):
    triangle.append(list(map(int, sys.stdin.readline().split())))

dp = [0]

for i in range(N):
    tmp = []

    for j in range(i + 1):
        if j == 0:
            tmp.append(dp[0] + triangle[i][j])
        elif j == i:
            tmp.append(dp[-1] + triangle[i][j])
        else:
            tmp.append(max(dp[j], dp[j-1]) + triangle[i][j])

    dp = tmp

print(max(dp))
