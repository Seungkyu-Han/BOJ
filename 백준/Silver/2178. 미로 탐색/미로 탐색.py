import sys

N, M = map(int, sys.stdin.readline().split())

miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[float('inf') for _ in range(M)] for _ in range(N)]

bfs = [[0, 0, 0]]

result = -1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while bfs:
    count, x, y = bfs.pop(0)

    if x == N - 1 and y == M - 1:
        result = count
        break

    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M and miro[x + dx[i]][y + dy[i]] == 1 and visited[x + dx[i]][y + dy[i]] > count + 1:
            bfs.append([count + 1, x + dx[i], y + dy[i]])
            visited[x + dx[i]][y + dy[i]] = count + 1


print(result + 1)