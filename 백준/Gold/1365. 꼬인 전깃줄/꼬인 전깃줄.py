import sys
import bisect

N = int(sys.stdin.readline())

pole = list(map(int, sys.stdin.readline().split()))

dp = [-1]

for i in range(N):

    if dp[-1] < pole[i]:
        dp.append(pole[i])
    else:
        index = bisect.bisect_left(dp, pole[i])

        dp[index] = pole[i]

connected_pole_cnt = len(dp) - 1

print(N - connected_pole_cnt)