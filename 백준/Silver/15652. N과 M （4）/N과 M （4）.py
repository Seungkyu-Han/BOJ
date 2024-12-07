import sys

N, M = map(int, sys.stdin.readline().split())


def back_tracking(cur_numbers, n, m):

    if len(cur_numbers) == m:
        print(*cur_numbers)
        return
    start_number = 1 if len(cur_numbers) == 0 else cur_numbers[-1]

    for i in range(start_number, n + 1):
        cur_numbers.append(i)
        back_tracking(cur_numbers, n, m)
        cur_numbers.pop()

back_tracking([], N, M)