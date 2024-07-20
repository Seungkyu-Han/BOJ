import sys

N, M = map(int, sys.stdin.readline().split())

apart = []

for i in range(1, M + 1):
    hand1, hand2 = map(int, sys.stdin.readline().split())

    apart.append([hand1, i])
    apart.append([hand2, i])

apart.sort()

print(apart[N % (2 * M) - 1][1])