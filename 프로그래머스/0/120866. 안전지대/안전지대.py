def solution(board):
    n = len(board)
    for i in range(n):
        for t in range(n):
            if board[i][t] == 0 or board[i][t] == 2:
                continue
            if 0 <= i + 1 < n and 0 <= t + 1 < n and board[i + 1][t + 1] == 0: 
                board[i + 1][t + 1] = 2
            if 0 <= i + 1 < n and board[i + 1][t] == 0:
                board[i + 1][t] = 2
            if 0 <= i + 1 < n and 0 <= t - 1 < n and board[i + 1][t - 1] == 0:
                board[i + 1][t - 1] = 2
            if 0 <= t - 1 < n and board[i][t - 1] == 0:
                board[i][t - 1] = 2
            if 0 <= t + 1 < n and board[i][t + 1] == 0:
                board[i][t + 1] = 2
            if 0 <= i - 1 < n and 0 <= t - 1 < n and board[i - 1][t - 1] == 0:
                board[i - 1][t - 1] = 2
            if 0 <= i - 1 < n and board[i - 1][t] == 0:
                board[i - 1][t] = 2
            if 0 <= i - 1 < n and 0 <= t + 1 < n and board[i - 1][t + 1] == 0:
                board[i - 1][t + 1] = 2
    answer = 0
    for i in range(n):
        print(board[i])
        for t in range(n):
            if board[i][t] == 0:
                answer += 1
    return answer