import sys

def next_directions(cur_direction) -> list[int]:
    return [(cur_direction - 1) % 4, (cur_direction - 2) % 4, (cur_direction - 3) % 4, (cur_direction - 4) % 4]

def next_pos(cur_r, cur_c, cur_direction) -> list[int]:
    if cur_direction == 0:
        return [cur_r - 1, cur_c]
    elif cur_direction == 1:
        return [cur_r, cur_c + 1]
    elif cur_direction == 2:
        return [cur_r + 1, cur_c]
    else:
        return [cur_r, cur_c - 1]

def go_back_pos(cur_r, cur_c, cur_direction):
    if cur_direction == 0:
        return [cur_r + 1, cur_c]
    elif cur_direction == 1:
        return [cur_r, cur_c - 1]
    elif cur_direction == 2:
        return [cur_r - 1, cur_c]
    else:
        return [cur_r, cur_c + 1]


N, M = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

find_0 = sum(room[i].count(0) for i in range(N))

result = 0

while True:

    if room[r][c] == 0:
        result += 1
        room[r][c] = 2
    else:
        next_direction = next_directions(d)

        flag = False

        for next_d in next_direction:
            next_r, next_c = next_pos(r, c, next_d)
            if room[next_r][next_c] == 0:
                r, c = next_r, next_c
                d = next_d
                flag = True
                break

        if not flag:
            next_r, next_c = go_back_pos(r, c, d)
            if room[next_r][next_c] == 1:
                break
            r, c = next_r, next_c
print(result)