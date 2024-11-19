import sys

N = int(sys.stdin.readline())

people = sorted(list(map(int, sys.stdin.readline().split())))

result = 0

for i in range(N):
    result += ((N - i) * people[i])

print(result)