import sys


for _ in range(int(sys.stdin.readline())):
    K = int(sys.stdin.readline())

    novel = list(map(int, sys.stdin.readline().split()))

    dp = [[float('inf') for _ in range(K)] for _ in range(K)]

    for i in range(K):
        dp[i][i] = 0

    for i in range(1, K):
        for j in range(K):
            sum_value =  + sum(novel[j:j+i + 1])
            if j + i > K - 1:
                break

            for k in range(i):
                dp[j][j + i] = min(dp[j][j + i], dp[j][j + k] + dp[j + k + 1][j + i] + sum_value)
    print(dp[0][-1])