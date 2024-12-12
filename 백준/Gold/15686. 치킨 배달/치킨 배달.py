import sys

sys.setrecursionlimit(50)


N, M = map(int, sys.stdin.readline().split())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken = []
houses = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append([r, c])
        elif city[r][c] == 2:
            chicken.append([r, c])


def distances(cur_chicken, param_houses):

    distances_result = 0

    for house_r, house_c in param_houses:
        each_house_max = float('inf')
        for chicken_r, chicken_c in cur_chicken:
            each_house_max = min(each_house_max, abs(house_r - chicken_r) + abs(house_c - chicken_c))

        distances_result += each_house_max
    return distances_result


def back_tracking(cur_chicken, m, cur_index, param_houses):

    back_tracking_result = float('inf')

    if len(cur_chicken) >= m:
        return distances(cur_chicken, param_houses)

    for i in range(cur_index + 1, len(chicken)):
        cur_chicken.append(chicken[i])
        back_tracking_result = min(back_tracking_result, back_tracking(cur_chicken, m, i, param_houses))
        cur_chicken.pop()

    return back_tracking_result

print(back_tracking([], M, -1, houses))