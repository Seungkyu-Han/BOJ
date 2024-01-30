import sys

N = int(sys.stdin.readline().strip())

P = sorted(list(map(int, sys.stdin.readline().split())))

cur_time = 0
result = 0

for i in P:
    cur_time += i
    result += cur_time

print(result)