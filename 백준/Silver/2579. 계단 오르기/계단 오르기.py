import sys

N = int(sys.stdin.readline())

stair = [int(sys.stdin.readline()) for _ in range(N)]

if N == 1:
    print(stair[0])
elif N == 2:
    print(stair[0] + stair[1])
elif N == 3:
    print(max(stair[0], stair[1]) + stair[2])
elif N >= 4:
    dp = [stair[0], stair[0] + stair[1], max(stair[0], stair[1]) + stair[2]]

    for i in range(3, N):
        dp.append(stair[i] + max(dp[-2], dp[-3] + stair[i-1]))

    print(dp[-1])