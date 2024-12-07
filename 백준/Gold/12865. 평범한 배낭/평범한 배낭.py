import sys

N, K = map(int, sys.stdin.readline().split())

bag = [0 for _ in range(K + 1)]

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())

    for i in range(K - W, -1, -1):
        bag[i + W] = max(bag[i + W], bag[i] + V)

print(max(bag))