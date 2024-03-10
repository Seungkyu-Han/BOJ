import sys

K, N = map(int, sys.stdin.readline().split())

lan = list()
max_lan = 0

for i in range(K):
    cur_lan = int(sys.stdin.readline().strip())
    lan.append(cur_lan)
    max_lan = max(max_lan, cur_lan)


def cur_lan(length):
    result = 0
    for lan_length in lan:
        result += (lan_length // length)
    return result


left, right = 0, max_lan

while left <= right:
    mid = (left + right) // 2
    mid = max(1, mid)
    lan_count = cur_lan(mid)

    if lan_count >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)