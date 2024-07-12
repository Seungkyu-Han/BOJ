import sys

N, r, c = map(int, sys.stdin.readline().split())


def z(n, cur_r, cur_c):
    if n == 0:
        return 0
    size = 2 ** n
    plus = (size // 2) ** 2
    if cur_r < size // 2 and cur_c < size // 2:
        return z(n - 1, cur_r, cur_c)
    elif cur_r < size // 2 <= cur_c:
        return z(n - 1, cur_r, cur_c - size // 2) + plus
    elif cur_c < size // 2 <= cur_r:
        return z(n - 1, cur_r - size // 2, cur_c) + plus * 2
    else:
        return z(n - 1, cur_r - size // 2, cur_c - size // 2) + plus * 3


print(z(N, r, c))