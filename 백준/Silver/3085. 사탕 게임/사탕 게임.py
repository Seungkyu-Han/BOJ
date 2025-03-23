import sys

input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

def find_max():
    max_count = 1

    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    for j in range(N):
        count = 1
        for i in range(1, N):
            if board[i][j] == board[i - 1][j]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    return max_count

def solve():
    max_result = find_max()

    for i in range(N):
        for j in range(N):
            if j + 1 < N and board[i][j] != board[i][j + 1]:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                max_result = max(max_result, find_max())
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

            if i + 1 < N and board[i][j] != board[i + 1][j]:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                max_result = max(max_result, find_max())
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

    return max_result

print(solve())
