import sys

n, k = map(int, sys.stdin.readline().split())

value = [0 for i in range(k+1)]

for i in range(n):
    coin = int(sys.stdin.readline().strip())
    if coin <= k:
        value[coin] += 1
    for t in range(1, (k+1) - coin):
        value[t+coin] += value[t]

print(value[-1])