import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

A.sort()

def solve():
    i = 0
    cur_index = 0

    while i <= 1_000_000_000:

        if i + 1 < A[cur_index]:
            return i + 1

        i += A[cur_index]
        cur_index += 1

        if cur_index >= N:
            return i + 1

print(solve())
