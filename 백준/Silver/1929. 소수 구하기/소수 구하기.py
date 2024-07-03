import sys
import math

M, N = map(int, sys.stdin.readline().split())

prime = [True for i in range(N + 1)]

for i in range(2, math.floor(math.sqrt(N)) + 1):
    if prime[i]:
        for t in range(2 * i, N + 1, i):
            prime[t] = False

for i in range(max(2, M), N + 1):
    if prime[i]:
        print(i)