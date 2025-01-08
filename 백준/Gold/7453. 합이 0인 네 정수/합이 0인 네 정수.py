import sys

A, B, C, D = [], [], [], []

n = int(sys.stdin.readline())

for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())

    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


def solve(a_list, b_list, c_list, d_list):
    result = 0

    value_dict = dict()

    for cur_a in a_list:
        for cur_b in b_list:
            value = - cur_a - cur_b
            value_dict[value] = value_dict.get(value, 0) + 1

    for cur_c in c_list:
        for cur_d in d_list:
            value = cur_c + cur_d
            result += value_dict.get(value, 0)
    return result

print(solve(A, B, C, D))