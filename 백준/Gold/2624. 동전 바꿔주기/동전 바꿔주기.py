import sys

T = int(sys.stdin.readline())

K = int(sys.stdin.readline())

coins: list[list[int]] = list()

for i in range(K):
    p, n = map(int, sys.stdin.readline().split())

    coins.append([p, n])


dp = [0 for _ in range(T + 1)]
dp[0] = 1
cur_max = 0

for p, n in coins:
    for i in range(cur_max, -1, -1):
        if dp[i] > 0:
            for j in range(1, n + 1):
                if p * j + i > T:
                    break
                else:
                    dp[p * j + i] += dp[i]
                    cur_max = max(cur_max, p * j + i)


print(dp[-1])