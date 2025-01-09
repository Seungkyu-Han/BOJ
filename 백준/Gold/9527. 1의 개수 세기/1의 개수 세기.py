import sys

A, B = map(int, sys.stdin.readline().split())


def find_acc_1(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1

    start, end = 1, 2
    result = 0
    cur = 1

    while not (start <= num < end):

        result += cur

        cur = (cur * 2) + start

        start *= 2
        end *= 2

    remain = num - start + 1

    return result + remain + find_acc_1(remain - 1)


print(find_acc_1(B) - find_acc_1(A - 1))