import sys

N, M = map(int, sys.stdin.readline().split())


def count_passwords(n, m):
    dp = [[0] * 27 for _ in range(m + 1)]

    for j in range(1, 27):
        dp[1][j] = 1

    for i in range(2, m + 1):
        for j in range(1, 27):
            for k in range(1, 27):
                if abs(j - k) >= n:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % 1000000007

    result = 0
    for j in range(1, 27):
        result = (result + dp[m][j]) % 1000000007

    return result


print(count_passwords(N, M))