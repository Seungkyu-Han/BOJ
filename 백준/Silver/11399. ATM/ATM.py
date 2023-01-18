import sys

num = int(sys.stdin.readline())

mytime = list(map(int, sys.stdin.readline().split()))

mytime.sort()

result = 0

for i in range(num, 0, -1):
    result += (mytime.pop(0)) * i

print(result)

