import sys

N, M = map(int, sys.stdin.readline().split())

square = []

# B, W
board = [[[0 for i in range(M)] for t in range(N)] for k in range(2)]

for _ in range(N):
    square.append(sys.stdin.readline().strip())

for i in range(N):
    for t in range(M):
        if (square[i][t] == 'W' and (i + t) % 2 == 0) or (square[i][t] == 'B' and (i + t) % 2 != 0):
            board[0][i][t] = 1
        else:
            board[1][i][t] = 1

result = 64

for i in range(N - 7):
    for t in range(M - 7):
        tmp = [0, 0]
        for k in range(8):
            for m in range(8):
                tmp[0] += board[0][i + k][t + m]
                tmp[1] += board[1][i + k][t + m]

        result = min(result, min(tmp))

print(result)