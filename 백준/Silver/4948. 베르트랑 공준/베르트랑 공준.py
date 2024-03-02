import sys

number = [True for i in range(123456 * 2 + 1)]

for i in range(2, int((2 * 123456 + 1) ** 0.5) + 1):
    if number[i]:
        for t in range(i + 1, 2 * 123456 + 1):
            if t % i == 0:
                number[t] = False


while True:
    n = int(sys.stdin.readline().strip())

    if n == 0:
        break

    print(number[n + 1: 2 * n + 1].count(True))