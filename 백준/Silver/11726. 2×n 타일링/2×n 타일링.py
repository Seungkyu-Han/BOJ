import sys

n = int(sys.stdin.readline())

square = [1 for i in range(n + 1)]

for i in range(2, n + 1):
    square[i] = square[i-1] + square[i-2]

print(square[-1] % 10007)