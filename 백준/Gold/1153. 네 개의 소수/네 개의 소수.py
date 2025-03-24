import sys

N = int(sys.stdin.readline())

is_prime = [True for _ in range(N + 1)]

sqrt_n = int(N ** 0.5)
for i in range(2, sqrt_n + 1):
    if is_prime[i]:
        for j in range(2 * i, N + 1, i):
            is_prime[j] = False

is_prime[0], is_prime[1] = False, False


def divide_4_prime(remain_num, remain_cnt, cur_nums) -> list[int]:
    if remain_num < 2 and remain_cnt > 1:
        return []

    if remain_cnt == 1:
        if remain_num >= 2 and is_prime[remain_num]:
            return cur_nums + [remain_num]
        else:
            return []


    for index in range(cur_nums[-1], N + 1):
        if index > remain_num:
            break

        if is_prime[index]:
            cur_result = divide_4_prime(remain_num - index, remain_cnt - 1, cur_nums + [index])
            if len(cur_result) == 5:
                return cur_result
    return []


result = divide_4_prime(N, 4, [0])

if len(result) == 5:
    print(*result[1:])
else:
    print(-1)