import sys

N = int(sys.stdin.readline())

# max, min
dp = [[0 for _ in range(3)] for _ in range(2)]

for i in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))

    # max
    max_1 = max(dp[0][0], dp[0][1]) + numbers[0]
    max_2 = max(dp[0]) + numbers[1]
    max_3 = max(dp[0][1], dp[0][2]) + numbers[2]
    dp[0][0], dp[0][1], dp[0][2] = max_1, max_2, max_3

    #min
    min_1 = min(dp[1][0], dp[1][1]) + numbers[0]
    min_2 = min(dp[1]) + numbers[1]
    min_3 = min(dp[1][1], dp[1][2]) + numbers[2]
    dp[1][0], dp[1][1], dp[1][2] = min_1, min_2, min_3

print(f'{max(dp[0])} {min(dp[1])}')
