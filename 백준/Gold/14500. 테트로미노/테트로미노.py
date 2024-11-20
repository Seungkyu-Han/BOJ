import sys

N, M = map(int, sys.stdin.readline().split())


graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def shape1(y, x):
    def_result = 0

    if x + 3 < M:
        def_result = max(def_result, sum(graph[y][x:x+4]))

    if y + 3 < N:
        def_result = max(def_result,
                     graph[y][x] + graph[y+1][x] + graph[y+2][x] + graph[y+3][x])

    return def_result

def shape2(y, x):
    if x + 1 < M and y + 1 < N:
        return graph[y][x] + graph[y+1][x] + graph[y][x+1] + graph[y+1][x+1]
    else:
        return 0

def shape3(y, x):

    def_result = 0

    if y + 2 < N and x + 1 < M:
        target = (graph[y][x] + graph[y + 1][x] + graph[y + 2][x]) + (
                    graph[y][x + 1] + graph[y + 1][x + 1] + graph[y + 2][x + 1])

        cur_min = min(
            graph[y][x] + graph[y + 1][x],
            graph[y + 1][x] + graph[y + 2][x],
            graph[y][x + 1] + graph[y + 1][x + 1],
            graph[y + 1][x + 1] + graph[y + 2][x + 1],

            graph[y][x + 1] + graph[y + 2][x],
            graph[y][x] + graph[y + 2][x + 1],

            graph[y][x] + graph[y + 2][x],
            graph[y][x + 1] + graph[y + 2][x + 1]
        )

        def_result = max(def_result, target - cur_min)


    if y + 1 < N and x + 2 < M:
        target = (graph[y][x] + graph[y + 1][x]) + (graph[y][x + 1] + graph[y + 1][x + 1]) + (
                    graph[y][x + 2] + graph[y + 1][x + 2])

        cur_min = min(
            graph[y + 1][x + 1] + graph[y + 1][x + 2],
            graph[y + 1][x] + graph[y + 1][x + 1],
            graph[y][x + 1] + graph[y][x + 2],
            graph[y][x] + graph[y][x + 1],

            graph[y][x] + graph[y + 1][x + 2],
            graph[y + 1][x] + graph[y][x + 2],

            graph[y][x] + graph[y][x + 2],
            graph[y + 1][x] + graph[y + 1][x + 2]
        )

        def_result = max(def_result, target - cur_min)

    return def_result

result = 0

for i in range(N):
    for j in range(M):
        result = max(result, shape1(i, j), shape2(i, j), shape3(i, j))

print(result)