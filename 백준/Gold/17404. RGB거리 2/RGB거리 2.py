import sys

N = int(sys.stdin.readline())


# 1 -> 2, 3
# 2 -> 1, 3
# 3 -> 1, 2

houses = []

for _ in range(N):
    house1, house2, house3 = map(int, sys.stdin.readline().split())
    houses.append([house1, house2, house3])

dp = [float('inf'), houses[0][1], houses[0][2]]

for i in range(1, N - 1):
    next_0, next_1, next_2 = houses[i][0] + min(dp[1], dp[2]), houses[i][1] + min(dp[0], dp[2]), houses[i][2] + min(dp[0], dp[1])

    dp = [next_0, next_1, next_2]

result = min(dp[1:]) + houses[N - 1][0]


dp = [houses[0][0], float('inf'), houses[0][2]]

for i in range(1, N - 1):
    next_0, next_1, next_2 = houses[i][0] + min(dp[1], dp[2]), houses[i][1] + min(dp[0], dp[2]), houses[i][2] + min(dp[0], dp[1])

    dp = [next_0, next_1, next_2]

result = min(result, min(dp[0], dp[2]) + houses[N - 1][1])

dp = [houses[0][0], houses[0][1], float('inf')]

for i in range(1, N - 1):
    next_0, next_1, next_2 = houses[i][0] + min(dp[1], dp[2]), houses[i][1] + min(dp[0], dp[2]), houses[i][2] + min(dp[0], dp[1])

    dp = [next_0, next_1, next_2]

result = min(result, min(dp[0], dp[1]) + houses[N - 1][2])

print(result)