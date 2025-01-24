import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())

dp = [[-1 for _ in range(n)] for _ in range(n)]

forest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def bfs(cur_x, cur_y):

    if dp[cur_x][cur_y] != -1:
        return dp[cur_x][cur_y]

    result = 1

    for next_x, next_y in [[cur_x + 1, cur_y], [cur_x - 1, cur_y], [cur_x, cur_y - 1], [cur_x, cur_y + 1]]:
        if 0 <= next_x < n and 0 <= next_y < n and forest[cur_x][cur_y] < forest[next_x][next_y]:
            result = max(result, bfs(next_x,next_y) + 1)

    dp[cur_x][cur_y] = result
    return result

answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, bfs(i, j))



print(answer)