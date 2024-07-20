import sys

N, M = map(int, sys.stdin.readline().split())

ans = 1

for i in range(2, min(N, M) + 1):
    ans = ans * i % M

print(ans)