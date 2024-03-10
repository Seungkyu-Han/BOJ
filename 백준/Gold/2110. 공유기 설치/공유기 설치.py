import sys

N, M = map(int, sys.stdin.readline().split())

house = []

for i in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()


def wifi(length):
    result = 1
    cur = house[0]
    for i in range(1, N):
        if house[i] >= cur + length:
            cur = house[i]
            result += 1

    return result


left = 1
right = house[-1] - house[0]

while left <= right:
    mid = (left + right) // 2
    cnt = wifi(mid)

    if cnt >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)