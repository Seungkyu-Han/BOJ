import sys

N = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split()))

fuel = list(map(int, sys.stdin.readline().split()))

min_fuel = [fuel[0] for _ in range(N - 1)]

for i in range(1, N - 1):
    min_fuel[i] = min(fuel[i], min_fuel[i - 1])

print(sum([distance[i] * min_fuel[i] for i in range(N - 1)]))