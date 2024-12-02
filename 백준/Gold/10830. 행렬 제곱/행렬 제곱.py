import sys

N, B = map(int, sys.stdin.readline().split())

array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def multi_array(cur_array1, cur_array2):
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i1 in range(N):
        for i2 in range(N):
            result[i1][i2] = sum(cur_array1[i1][i] * cur_array2[i][i2] for i in range(N)) % 1000

    return result


def dc(degree):

    if degree == 1:
        return array

    if degree % 2 == 0:
        half_result = dc(degree // 2)
        return multi_array(half_result, half_result)
    else:
        half_result = dc(degree // 2)
        return multi_array(multi_array(half_result, half_result), array)


for row in dc(B):
    for col in row:
        print(col % 1000, end = ' ')
    print()