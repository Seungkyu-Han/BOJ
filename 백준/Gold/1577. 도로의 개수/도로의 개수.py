import sys

N, M = map(int, sys.stdin.readline().split())

road = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
road[0][0] = 1

blocked = set()

K = int(sys.stdin.readline())

for i in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    blocked.add((min(a, c), min(b, d), max(a, c), max(b, d)))


for n in range(N + 1):
    for m in range(M + 1):
        if n > 0 and (n - 1, m, n, m) not in blocked:
            road[m][n] += road[m][n - 1]
        if m > 0 and (n, m - 1, n, m) not in blocked:
            road[m][n] += road[m - 1][n]


print(road[-1][-1])