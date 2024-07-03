import sys


def getLan(length):
    total = 0

    for i in lan:
        total += (i // length)

    return total


K, N = map(int, sys.stdin.readline().split())

lan = [int(sys.stdin.readline()) for i in range(K)]


left, right = 1, max(lan)

while left <= right:

    mid = (left + right) // 2

    result = getLan(mid)

    if result >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)