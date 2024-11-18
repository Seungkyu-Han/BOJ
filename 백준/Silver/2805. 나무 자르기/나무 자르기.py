import sys

N, M = map(int, sys.stdin.readline().split())

woods = list(map(int, sys.stdin.readline().split()))


def cut_wood(length):
    result = 0

    for wood in woods:
        result += max((wood - length), 0)
    return result



left, right = 0, 2_000_000_000

while left <= right:
    mid = (left + right) // 2

    cur_result = cut_wood(mid)

    if cur_result >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)