import sys

N, M, x, y, k = map(int, sys.stdin.readline().split())

# up 0, down 1, front 2, back 3, left 4, right 5
dice = [0, 0, 0, 0, 0, 0]


def throw_dice(cur_dice, cur_direction):

    if cur_direction == 1:
        return [
            cur_dice[4], cur_dice[5], cur_dice[2], cur_dice[3], cur_dice[1], cur_dice[0]
        ]
    elif cur_direction == 2:
        return [
            cur_dice[5], cur_dice[4], cur_dice[2], cur_dice[3], cur_dice[0], cur_dice[1]
        ]
    elif cur_direction == 3:
        return [
            cur_dice[2], cur_dice[3], cur_dice[1], cur_dice[0], cur_dice[4], cur_dice[5]
        ]
    else:
        return [
            cur_dice[3], cur_dice[2], cur_dice[0], cur_dice[1], cur_dice[4], cur_dice[5]
        ]


board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

commands = list(map(int, sys.stdin.readline().split()))

position = [x, y]
direction = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]

for command in commands:

    next_n, next_m = position[0] + direction[command][0], position[1] + direction[command][1]

    if 0 <= next_n < N and 0 <= next_m < M:

        position = [next_n, next_m]

        dice = throw_dice(dice, command)

        print(dice[0])

        if board[position[0]][position[1]] == 0:
            board[position[0]][position[1]] = dice[1]
        else:
            dice[1] = board[position[0]][position[1]]
            board[position[0]][position[1]] = 0

    else:
        continue