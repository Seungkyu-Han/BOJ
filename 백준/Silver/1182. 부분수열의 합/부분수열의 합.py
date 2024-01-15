import sys

N, S = map(int, sys.stdin.readline().split())

input_list = list(map(int, sys.stdin.readline().split()))


def find(param_list, cur_num):
    if len(param_list) == 0:
        if cur_num == S:
            return 1
        else:
            return 0

    return find(param_list[1:], cur_num + param_list[0]) + find(param_list[1:], cur_num)


result = find(input_list, 0)

if S == 0:
    print(result - 1)
else:
    print(result)