import sys

n = int(sys.stdin.readline().strip())

target_a, target_b = map(int, sys.stdin.readline().split())

family = [[float('inf') for _ in range(n)] for _ in range(n)]

for _ in range(int(sys.stdin.readline().strip())):
    a, b = map(int, sys.stdin.readline().split())
    family[a-1][b-1] = 1
    family[b-1][a-1] = 1

for i in range(n):
    for t in range(n):
        for k in range(n):
            if t != k:
                family[t][k] = min(family[t][k], family[t][i] + family[i][k])


print(family[target_a - 1][target_b - 1] if family[target_a - 1][target_b - 1] != float('inf') else -1)