import sys

N, M = map(int, sys.stdin.readline().split())

candidate = sorted(list(set(map(int, sys.stdin.readline().split()))))


def back_tracking(cur_numbers, cur_index, m):
    if len(cur_numbers) == m:
        print(*cur_numbers)
        return

    for index in range(cur_index, len(candidate)):
        cur_numbers.append(candidate[index])
        back_tracking(cur_numbers, index, m)
        cur_numbers.pop()


back_tracking([], 0, m = M)