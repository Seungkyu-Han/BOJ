import bisect
import sys
from _collections import deque

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

position = []
dp = [-1_000_000_001]

for i in range(N):
    if dp[-1] < A[i]:
        dp.append(A[i])
        position.append(len(dp) - 1)
    else:
        index = bisect.bisect_left(dp, A[i])
        dp[index] = A[i]
        position.append(index)

length = len(dp) - 1
print(length)

result = deque()

for i in range(N - 1, -1, -1):
    if position[i] == length:
        result.appendleft(A[i])
        length -= 1

while result:
    print(result.popleft(), end = ' ')
print()