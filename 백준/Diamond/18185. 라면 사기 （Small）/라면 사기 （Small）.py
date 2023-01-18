import sys

num = int(sys.stdin.readline())
ramen = list(map(int, sys.stdin.readline().split()))

ramen.extend([0, 0])
total = 0

for i in range(num):
    if ramen[i + 1] > ramen[i + 2]:
        tmp = min(ramen[i], ramen[i + 1] - ramen[i + 2])
        ramen[i] -= tmp
        ramen[i + 1] -= tmp
        total += tmp * 5

        tmp = min(ramen[i:i + 3])
        total += tmp * 7
        ramen[i] -= tmp
        ramen[i + 1] -= tmp
        ramen[i + 2] -= tmp
    else:
        tmp = min(ramen[i:i + 3])
        total += tmp * 7
        ramen[i] -= tmp
        ramen[i + 1] -= tmp
        ramen[i + 2] -= tmp

        tmp = min(ramen[i], ramen[i + 1])
        total += tmp * 5
        ramen[i] -= tmp
        ramen[i + 1] -= tmp

    total += ramen[i] * 3
    ramen[i] = 0

print(total)