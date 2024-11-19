import sys

N, M = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

acc = [0]

for i in range(N):
    acc.append(acc[-1] + array[i])

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())

    print(acc[end] - acc[start - 1])