import sys

N = int(sys.stdin.readline())

A = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

for number in list(map(int, sys.stdin.readline().split())):
    print(1 if number in A else 0)