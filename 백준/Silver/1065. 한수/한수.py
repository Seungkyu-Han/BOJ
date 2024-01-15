import sys

N = int(sys.stdin.readline())

result = 0


def hansoo(num):
    hansoo_list = []
    while num > 0:
        hansoo_list.append(num % 10)
        num //= 10
    for t in range(len(hansoo_list) - 2):
        if hansoo_list[t+1] - hansoo_list[t] != hansoo_list[t+2] - hansoo_list[t+1]:
            return False

    return True

for i in range(1, N + 1):
    if hansoo(i):
        result += 1

print(result)