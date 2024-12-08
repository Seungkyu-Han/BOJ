import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]


def is_available(number, cur_board, n, m):
    for i in range(9):
        if cur_board[i][m] == number:
            return False
        if cur_board[n][i] == number:
            return False

    block_n, block_m = (n // 3) * 3, (m // 3) * 3

    for i in range(3):
        for j in range(3):
            if cur_board[block_n + i][block_m + j] == number:
                return False

    return True


def back_tracking(cur_board, index):
    if index == 81:
        for row in cur_board:
            print(*row)
        exit(0)

    n = index // 9
    m = index % 9

    if cur_board[n][m] != 0:
        back_tracking(cur_board, index + 1)
    else:
        for num in range(1, 10):
            if is_available(num, cur_board, n, m):
                cur_board[n][m] = num
                back_tracking(cur_board, index + 1)
                cur_board[n][m] = 0


back_tracking(sudoku, 0)