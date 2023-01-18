import sys

target = int(sys.stdin.readline())

total = 0

for i in range(int(sys.stdin.readline())):
    money, cnt = map(int, sys.stdin.readline().split())
    total += (money * cnt)

if total == target:
    print('Yes')
else:
    print('No')