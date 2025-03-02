import sys

N, M, L = map(int, sys.stdin.readline().split())

pieces = [int(sys.stdin.readline()) for _ in range(M)]
pieces.append(L)


def cut_cake(length: int) -> int:
    result = 0

    cur_length = 0

    for cur_pos in pieces:
        if (cur_pos - cur_length) >= length:
            result += 1
            cur_length = cur_pos


    return result


for i in range(N):
    cnt = int(sys.stdin.readline())

    left, right = 0, L

    while left <= right:

        mid = (left + right) // 2

        cur_cnt = cut_cake(mid)

        if cur_cnt > cnt:
            left = mid + 1
        else:
            right = mid - 1

    print(right)