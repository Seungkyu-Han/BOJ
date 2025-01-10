import sys

N, M = map(int, sys.stdin.readline().split())

room = []
cctv = []

for i in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))

cur_room = [[True for _ in range(M)] for _ in range(N)]


def up_detect(cur_n, cur_m, func_room):
    copied_room = [[True for _ in range(M)] for _ in range(N)]

    for copy_n in range(N):
        for copy_m in range(M):
            copied_room[copy_n][copy_m] = func_room[copy_n][copy_m]

    for func_up_n in range(cur_n, -1, -1):
        if room[func_up_n][cur_m] < 6:
            copied_room[func_up_n][cur_m] = False
        else:
            break
    return copied_room

def down_detect(cur_n, cur_m, func_room):
    copied_room = [[True for _ in range(M)] for _ in range(N)]

    for copy_n in range(N):
        for copy_m in range(M):
            copied_room[copy_n][copy_m] = func_room[copy_n][copy_m]

    for func_up_n in range(cur_n, N):
        if room[func_up_n][cur_m] < 6:
            copied_room[func_up_n][cur_m] = False
        else:
            break
    return copied_room

def left_detect(cur_n, cur_m, func_room):
    copied_room = [[True for _ in range(M)] for _ in range(N)]

    for copy_n in range(N):
        for copy_m in range(M):
            copied_room[copy_n][copy_m] = func_room[copy_n][copy_m]

    for func_up_m in range(cur_m, -1, -1):
        if room[cur_n][func_up_m] < 6:
            copied_room[cur_n][func_up_m] = False
        else:
            break
    return copied_room

def right_detect(cur_n, cur_m, func_room):
    copied_room = [[True for _ in range(M)] for _ in range(N)]

    for copy_n in range(N):
        for copy_m in range(M):
            copied_room[copy_n][copy_m] = func_room[copy_n][copy_m]
    for func_up_m in range(cur_m, M):
        if room[cur_n][func_up_m] < 6:
            copied_room[cur_n][func_up_m] = False
        else:
            break
    return copied_room


for n in range(N):
    for m in range(M):
        if 1 <= room[n][m] <= 4:
            cctv.append([n, m])

        elif room[n][m] == 5:
            cur_room = up_detect(n, m, cur_room)
            cur_room = down_detect(n, m, cur_room)
            cur_room = left_detect(n, m, cur_room)
            cur_room = right_detect(n, m, cur_room)




def backtracking(backtracking_cctv, backtracking_room):

    if len(backtracking_cctv) == 0:
        result = 0
        for n_cctv in range(N):
            for m_cctv in range(M):
                if backtracking_room[n_cctv][m_cctv] and room[n_cctv][m_cctv] != 6:
                    result += 1
        return result

    cur_n, cur_m = backtracking_cctv[-1]

    if room[cur_n][cur_m] == 1:

        up_detect_room = up_detect(cur_n, cur_m, backtracking_room)
        down_detect_room = down_detect(cur_n, cur_m, backtracking_room)
        left_detect_room = left_detect(cur_n, cur_m, backtracking_room)
        right_detect_room = right_detect(cur_n, cur_m, backtracking_room)

        return min(
            backtracking(backtracking_cctv[:-1], up_detect_room),
            backtracking(backtracking_cctv[:-1], down_detect_room),
            backtracking(backtracking_cctv[:-1], left_detect_room),
            backtracking(backtracking_cctv[:-1], right_detect_room),
        )

    elif room[cur_n][cur_m] == 2:

        up_down_detect_room = up_detect(cur_n, cur_m, backtracking_room)
        up_down_detect_room = down_detect(cur_n, cur_m, up_down_detect_room)

        left_right_detect_room = left_detect(cur_n, cur_m, backtracking_room)
        left_right_detect_room = right_detect(cur_n, cur_m, left_right_detect_room)

        return min(
            backtracking(backtracking_cctv[:-1], up_down_detect_room),
            backtracking(backtracking_cctv[:-1], left_right_detect_room)
        )

    elif room[cur_n][cur_m] == 3:

        up_right_detect_room =  up_detect(cur_n, cur_m, backtracking_room)
        up_right_detect_room = right_detect(cur_n, cur_m, up_right_detect_room)

        right_down_detect_room = right_detect(cur_n, cur_m, backtracking_room)
        right_down_detect_room = down_detect(cur_n, cur_m, right_down_detect_room)

        down_left_detect_room = down_detect(cur_n, cur_m, backtracking_room)
        down_left_detect_room = left_detect(cur_n, cur_m, down_left_detect_room)

        left_up_detect_room = left_detect(cur_n, cur_m, backtracking_room)
        left_up_detect_room = up_detect(cur_n, cur_m, left_up_detect_room)

        return min(
            backtracking(backtracking_cctv[:-1], up_right_detect_room),
            backtracking(backtracking_cctv[:-1], right_down_detect_room),
            backtracking(backtracking_cctv[:-1], down_left_detect_room),
            backtracking(backtracking_cctv[:-1], left_up_detect_room),
        )

    elif room[cur_n][cur_m] == 4:
        up_right_down_detect_room = up_detect(cur_n, cur_m, backtracking_room)
        up_right_down_detect_room = right_detect(cur_n, cur_m, up_right_down_detect_room)
        up_right_down_detect_room = down_detect(cur_n, cur_m, up_right_down_detect_room)

        right_down_left_detect_room = right_detect(cur_n, cur_m, backtracking_room)
        right_down_left_detect_room = down_detect(cur_n, cur_m, right_down_left_detect_room)
        right_down_left_detect_room = left_detect(cur_n, cur_m, right_down_left_detect_room)

        down_left_up_detect_room = down_detect(cur_n, cur_m, backtracking_room)
        down_left_up_detect_room = left_detect(cur_n, cur_m, down_left_up_detect_room)
        down_left_up_detect_room = up_detect(cur_n, cur_m, down_left_up_detect_room)

        left_up_right_detect_room = left_detect(cur_n, cur_m, backtracking_room)
        left_up_right_detect_room = up_detect(cur_n, cur_m, left_up_right_detect_room)
        left_up_right_detect_room = right_detect(cur_n, cur_m, left_up_right_detect_room)

        return min(
            backtracking(backtracking_cctv[:-1], up_right_down_detect_room),
            backtracking(backtracking_cctv[:-1], right_down_left_detect_room),
            backtracking(backtracking_cctv[:-1], down_left_up_detect_room),
            backtracking(backtracking_cctv[:-1], left_up_right_detect_room),
        )

print(backtracking(cctv, cur_room))