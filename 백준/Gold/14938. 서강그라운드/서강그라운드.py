import sys

n, m, r = map(int, sys.stdin.readline().split())

field = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    field[i][i] = 0

item = list(map(int, sys.stdin.readline().split()))

for _ in range(r):
    v1, v2, weight = map(int, sys.stdin.readline().split())

    field[v1 - 1][v2 - 1] = weight
    field[v2 - 1][v1 - 1] = weight


for i1 in range(n):
    for i2 in range(n):
        for i3 in range(n):
            field[i2][i3] = min(field[i2][i3], field[i2][i1] + field[i1][i3])

result = 0

for i1 in range(n):
    cur_result = 0
    for i2 in range(n):
        if field[i1][i2] <= m:
            cur_result += item[i2]
    result = max(result, cur_result)

print(result)