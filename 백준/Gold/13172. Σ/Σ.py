import sys

target = 1000000007


def ans(n, s):
    return s * multi(n, target - 2) % target


def multi(b, t):
    if t == 1:
        return b % target

    if t % 2 == 0:
        tmp = multi(b, t // 2)
        return (tmp ** 2) % target
    else:
        return b * multi(b, t - 1) % target

total = 0

m = int(sys.stdin.readline())

for i in range(m):
    n, s = map(int, sys.stdin.readline().split())
    total += ans(n, s)
    total %= target

print(total)