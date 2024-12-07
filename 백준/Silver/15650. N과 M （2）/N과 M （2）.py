import sys

N, M = map(int, sys.stdin.readline().split())


def back_tracking(cur_numbers, n, m):

    if len(cur_numbers) == m + 1:
        for number in cur_numbers[1:]:
            print(number, end=' ')
        print()
        return

    for i in range(cur_numbers[-1] + 1, n + 1):
        cur_numbers.append(i)
        back_tracking(cur_numbers, n, m)
        cur_numbers.pop()

back_tracking([0], N, M)