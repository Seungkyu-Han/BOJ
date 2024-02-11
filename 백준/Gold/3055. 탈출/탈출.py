import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

result = 0

move = deque()
water = deque()

target_r, target_c = -1, -1

arrive = False

forest = [list(sys.stdin.readline().strip()) for _ in range(R)]

for r in range(R):
    for c in range(C):
        if forest[r][c] == 'S':
            move.append([r, c])
            forest[r][c] = '.'
        elif forest[r][c] == 'D':
            target_r, target_c = r, c
        elif forest[r][c] == '*':
            water.append([r, c])


while move:

    # 물 먼저 이동
    next_water = deque()

    while water:

        cur_r, cur_c = water.popleft()

        for next_r, next_c in [[cur_r, cur_c - 1], [cur_r, cur_c + 1], [cur_r - 1, cur_c], [cur_r + 1, cur_c]]:
            if 0 <= next_r < R and 0 <= next_c < C and forest[next_r][next_c] == '.':
                forest[next_r][next_c] = '*'
                next_water.append([next_r, next_c])

    water = next_water

    # 비버 이동 가능 한 곳으로 이동

    next_move = deque()

    visited = [[False for _ in range(C)] for _ in range(R)]

    while move:

        cur_r, cur_c = move.popleft()

        if cur_r == target_r and cur_c == target_c:
            arrive = True
            break

        for next_r, next_c in [[cur_r, cur_c - 1], [cur_r, cur_c + 1], [cur_r - 1, cur_c], [cur_r + 1, cur_c]]:
            if 0 <= next_r < R and 0 <= next_c < C and (forest[next_r][next_c] == '.' or forest[next_r][next_c] == 'D') and visited[next_r][next_c] is False:
                next_move.append([next_r, next_c])
                visited[next_r][next_c] = True

    move = next_move

    if arrive:
        break

    result += 1

print(result if arrive else 'KAKTUS')