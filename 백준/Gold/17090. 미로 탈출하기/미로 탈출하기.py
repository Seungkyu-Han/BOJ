import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())

miro = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

parent = [[(i, j) for j in range(M)] for i in range(N)]
# -1 cur visit
# 0 not visited
# 1 false
# 2 true
result = [[0 for j in range(M)] for i in range(N)]

def find(cur_i, cur_j):
    if parent[cur_i][cur_j] != (cur_i, cur_j):
        parent[cur_i][cur_j] = find(parent[cur_i][cur_j][0], parent[cur_i][cur_j][1])
    return parent[cur_i][cur_j]


def next_direction(cur_i, cur_j):
    next_i, next_j = cur_i, cur_j
    if miro[cur_i][cur_j] == 'U':
        next_i -= 1
    elif miro[cur_i][cur_j] == 'R':
        next_j += 1
    elif miro[cur_i][cur_j] == 'D':
        next_i += 1
    elif miro[cur_i][cur_j] == 'L':
        next_j -= 1
    return next_i, next_j

def visit(cur_i, cur_j):
    if result[cur_i][cur_j] != 0:
        if result[cur_i][cur_j] == 2:
            return 2
        else:
            return 1

    result[cur_i][cur_j] = -1

    next_i, next_j = next_direction(cur_i, cur_j)

    if 0 <= next_i < N and 0 <= next_j < M:
        result[cur_i][cur_j] = visit(next_i, next_j)
        return result[cur_i][cur_j]
    else:
        result[cur_i][cur_j] = 2
        return 2

for i in range(N):
    for j in range(M):
        if result[i][j] == 0:
            visit(i, j)

cnt = 0

for i in range(N):
    for j in range(M):
        if result[i][j] == 2:
            cnt += 1

print(cnt)