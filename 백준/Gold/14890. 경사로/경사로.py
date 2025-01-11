import sys

N, L = map(int, sys.stdin.readline().split())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0

# up_down direction
for i in range(N):

    flag = True

    down_point = []

    up_point = []

    visited = [False for _ in range(N)]

    for j in range(N - 1):

        if paper[j][i] - paper[j + 1][i] == 1:
            down_point.append(j)
        elif paper[j][i] - paper[j + 1][i] == -1:
            up_point.append(j)
        elif paper[j][i] != paper[j + 1][i]:
            flag = False
            break

    for down in down_point:
        if not flag:
            break

        for j in range(1, L + 1):
            if down + j >= N:
                flag = False
                break

            elif paper[down][i] -1 == paper[down + j][i] and not visited[down + j]:
                visited[down + j] = True
            else:
                flag = False
                break


    for up in up_point:
        if not flag:
            break

        for j in range(L):
            if up - j < 0:
                flag = False
                break

            elif paper[up + 1][i] - 1 == paper[up - j][i] and not visited[up - j]:
                visited[up - j] = True
            else:
                flag = False
                break

    if flag:
        result += 1

# left_right direction
for i in range(N):

    flag = True

    down_point = []

    up_point = []

    visited = [False for _ in range(N)]

    for j in range(N - 1):

        if paper[i][j] - paper[i][j + 1] == 1:
            down_point.append(j)
        elif paper[i][j] -  paper[i][j + 1] == -1:
            up_point.append(j)
        elif paper[i][j] != paper[i][j + 1]:
            flag = False
            break

    for down in down_point:
        if not flag:
            break

        for j in range(1, L + 1):
            if down + j >= N:
                flag = False
                break

            elif paper[i][down] -1 == paper[i][down + j] and not visited[down + j]:
                visited[down + j] = True
            else:
                flag = False
                break

    for up in up_point:
        if not flag:
            break

        for j in range(L):
            if up - j < 0:
                flag = False
                break

            elif paper[i][up + 1] - 1 == paper[i][up - j] and not visited[up - j]:
                visited[up - j] = True
            else:
                flag = False
                break

    if flag:
        result += 1




print(result)