import sys

N, M = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def dfs():
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    need_visit = [[0, 0]]

    while need_visit:

        cur_n, cur_m = need_visit.pop()
        cur_num = int(board[cur_n][cur_m])

        for next_n, next_m in [[cur_n - cur_num, cur_m], [cur_n + cur_num, cur_m], [cur_n, cur_m - cur_num], [cur_n, cur_m + cur_num]]:
            if 0 <= next_n < N and 0 <= next_m < M and board[next_n][next_m] != 'H':
                if visited[next_n][next_m] < visited[cur_n][cur_m] + 1:
                    visited[next_n][next_m] = visited[cur_n][cur_m] + 1
                    need_visit.append([next_n, next_m])
                    if visited[cur_n][cur_m] >  N * M:
                        return -1

    result = 0

    for n in range(N):
        for m in range(M):
            result = max(result, visited[n][m])
    return result


print(dfs())