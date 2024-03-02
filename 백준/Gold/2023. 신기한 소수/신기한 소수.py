import sys

N = int(sys.stdin.readline().strip())

prime = [2, 3, 5, 7]


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def wow_prime(cur_number):
    if len(str(cur_number)) == N:
        print(cur_number)
    else:
        for t in range(1, 10):
            if t % 2 != 0 and is_prime(cur_number * 10 + t):
                wow_prime(cur_number * 10 + t)


for i in prime:
    wow_prime(i)