import sys

N = int(sys.stdin.readline())

result = 0

N = N ^ (N * -1)

for i in range(32):
    if N >> i & 1:
        result += 1

print(result)