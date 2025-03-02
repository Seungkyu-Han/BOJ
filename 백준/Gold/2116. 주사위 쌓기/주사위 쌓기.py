import sys

N = int(sys.stdin.readline())

dices: list[list[int]] = []
dices_reverse_dict: list[dict[int, int]]= []

for i in range(N):
    cur_dice: list[int] = list(map(int, sys.stdin.readline().split()))

    dices.append(cur_dice)

    cur_dict: dict[int, int] = dict()

    for j in range(6):
        cur_dict[cur_dice[j]] = j

    dices_reverse_dict.append(cur_dict)


find_bottom = [5, 3, 4, 1, 2, 0]


def find_max_face(cur_top_index: int, cur_depth: int):
    result = 0

    for index in range(6):
        if index != cur_top_index and index != find_bottom[cur_top_index] != index:
            result = max(result, dices[cur_depth][index])

    return result


def find_cur_max(cur_top_value: int, cur_depth):
    cur_top_index = dices_reverse_dict[cur_depth][cur_top_value]
    return find_max_face(cur_top_index, cur_depth)


def find_result_by_top_value(cur_top_value: int):
    result = 0

    for depth in range(N):
        result += find_cur_max(cur_top_value, depth)
        cur_top_index = dices_reverse_dict[depth][cur_top_value]
        cur_top_value = dices[depth][find_bottom[cur_top_index]]


    return result


print(max([find_result_by_top_value(i) for i in range(1, 7)]))