import sys

N, M = map(int, input().split())

myset = set()

for i in range(N):
    myset.add(sys.stdin.readline().strip())

total = 0

for i in range(M):
    ans = sys.stdin.readline().strip()
    if ans in myset:
        total += 1
print(total)