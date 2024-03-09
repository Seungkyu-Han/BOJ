import sys

N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))


def cut(height):
    result = 0
    for i in tree:
        result += max(0, i - height)
    return result


left, right = 0, max(tree)

while left <= right:
    mid = (left + right) // 2
    cur_height = cut(mid)

    if cur_height >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)