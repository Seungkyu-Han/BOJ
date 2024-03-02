import sys

T = int(sys.stdin.readline().strip())

prime = [True for _ in range(10001)]

for i in range(2, int(10001 ** 0.5) + 1):
    if prime[i]:
        for t in range(i + 1, 10001):
            if t % i == 0:
                prime[t] = False

for _ in range(T):
    n = int(sys.stdin.readline().strip())

    for i in range(n // 2 + 1):
        if prime[n // 2 - i] and prime[n // 2 + i]:
            print(n // 2 - i, n // 2 + i)
            break

