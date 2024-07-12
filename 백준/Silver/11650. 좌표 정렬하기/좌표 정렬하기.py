import sys

for x, y in list(sorted([list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))])):
    print(x, y)