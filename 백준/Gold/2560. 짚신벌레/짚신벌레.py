import sys

a, b, d, N = map(int, sys.stdin.readline().split())

days = [0 for _ in range(N + 1)]

days[0] = 1

total_bugs = 0
adult_bugs = 0

for i in range(a, N + 1):
    adult_bugs += days[i - a]
    if i >= b:
        adult_bugs -= days[i - b]

    days[i] = adult_bugs % 1000

print(sum(days[-d:]) % 1000)
