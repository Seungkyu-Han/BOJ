import sys

for _ in range(int(sys.stdin.readline())):
    M ,N, K = map(int, sys.stdin.readline().split())

    cabbage = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):

        X, Y = map(int, sys.stdin.readline().split())

        cabbage[Y][X] = 1

    result = 0

    for x in range(M):
        for y in range(N):
            if cabbage[y][x] == 1:
                result += 1
                need_visit = [(x, y)]
                cabbage[y][x] = 2

                while need_visit:

                    cur_x, cur_y = need_visit.pop()

                    for dx, dy in [(cur_x - 1, cur_y), (cur_x + 1, cur_y), (cur_x, cur_y - 1), (cur_x, cur_y + 1)]:
                        if 0 <= dx < M and 0 <= dy < N:
                            if cabbage[dy][dx] == 1:
                                need_visit.append((dx, dy))
                                cabbage[dy][dx] = 2

    print(result)