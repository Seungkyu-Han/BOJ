import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    dp = [[0, sticker[0][0]], [0, sticker[1][0]]]

    for i in range(1, n):
        up_sticker = max(dp[1][-1] + sticker[0][i], dp[0][-1])
        down_sticker = max(dp[0][-1] + sticker[1][i], dp[1][-1])

        dp[0].append(up_sticker)
        dp[-1].append(down_sticker)

    print(max(dp[0][-1], dp[1][-1]))