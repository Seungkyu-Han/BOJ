import sys

a, b, c = map(int, sys.stdin.readline().split())

if c % 2 == 0:
    print(a)
else:
    print(a ^ b)