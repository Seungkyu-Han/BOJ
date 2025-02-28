import sys
import math

N = int(sys.stdin.readline())

C = list(map(int, sys.stdin.readline().split()))


def solve(n, c):
    total = sum(c)

    if total == 0:
        return n // 2

    start_index = 0

    for i in range(n):
        if c[i] > 0:
            start_index = i
            break

    result = 0
    cur_length = 0

    for i in range(start_index + 1, n):
        if c[i] == 0:
            cur_length += 1
        else:
            result += c[i]
            result += math.ceil(cur_length / 2)
            cur_length = 0

    for i in range(start_index + 1):
        if c[i] == 0:
            cur_length += 1
        else:
            result += c[i]
            result += math.ceil(cur_length / 2)
            cur_length = 0

    return result

print(solve(N, C))