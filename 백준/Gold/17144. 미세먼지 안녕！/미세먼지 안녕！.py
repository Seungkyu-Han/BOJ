import sys

R, C, T = map(int, sys.stdin.readline().split())

room = []

fresher = []

for i in range(R):
    cur_row = list(map(int, sys.stdin.readline().split()))

    if cur_row[0] == -1:
        fresher.append(i)

    room.append(cur_row)



for i in range(T):
    # spread
    cur_room = [[0 for _ in range(C)] for _ in range(R)]
    cur_room[fresher[0]][0] = -1
    cur_room[fresher[1]][0] = -1

    for r in range(R):
        for c in range(C):
            if room[r][c] == -1 or room[r][c] == 0:
                continue
            spread_count = 0
            for next_r, next_c in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= next_r < R and 0 <= next_c < C and room[next_r][next_c] != -1:
                    cur_room[next_r][next_c] += (room[r][c]//5)
                    spread_count += 1
            cur_room[r][c] += (room[r][c] - (room[r][c] //5 ) * spread_count)

    room = cur_room[:][:]

    # spin

    # up fresher
    # up, down
    for r in range(fresher[0] - 1, -1, -1):
        room[r + 1][0] = room[r][0]

    # up, left
    for c in range(1, C):
        room[0][c - 1] = room[0][c]

    # up, up
    for r in range(1, fresher[0] + 1):
        room[r - 1][C - 1] = room[r][C - 1]

    # up, right
    for c in range(C - 1, 1, -1):
        room[fresher[0]][c] = room[fresher[0]][c - 1]

    room[fresher[0]][0] = -1
    room[fresher[0]][1] = 0

    # down fresher
    # down, up
    for r in range(fresher[1] + 1, R):
        room[r - 1][0] = room[r][0]

    # down, left
    for c in range(1, C):
        room[R - 1][c - 1] = room[R - 1][c]

    # down, down
    for r in range(R - 2, fresher[1] - 1, -1):
        room[r + 1][C - 1] = room[r][C - 1]

    # down, right
    for c in range(C - 1, 1, -1):
        room[fresher[1]][c] = room[fresher[1]][c - 1]

    room[fresher[1]][0] = -1
    room[fresher[1]][1] = 0

result = 0

for r in range(R):
    for c in range(C):
        if 0 < room[r][c]:
            result += room[r][c]
print(result)