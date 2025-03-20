from collections import deque
import sys

L, W = map(int, sys.stdin.readline().split())

island = [list(sys.stdin.readline().rstrip()) for _ in range(L)]

def bfs(start_l, start_w):
    visited = [[-1 for _ in range(W)] for _ in range(L)]
    visited[start_l][start_w] = 0

    need_visit = deque()
    need_visit.append([start_l, start_w, 0])

    while need_visit:

        cur_l, cur_w, cur_cnt = need_visit.popleft()

        for next_l, next_w in [[cur_l + 1, cur_w], [cur_l - 1, cur_w], [cur_l, cur_w + 1], [cur_l, cur_w - 1]]:
            if 0 <= next_l < L and 0 <= next_w < W and island[next_l][next_w] == 'L' and visited[next_l][next_w] == -1:
                visited[next_l][next_w] = cur_cnt + 1
                need_visit.append([next_l, next_w, cur_cnt + 1])

    fun_result = 0

    for i in range(L):
        for j in range(W):
            if visited[i][j] >= 0:
                fun_result = max(fun_result, visited[i][j])

    return fun_result




result = 0

for l in range(L):
    for w in range(W):
        if island[l][w] == 'L':
            result = max(result, bfs(l, w))

print(result)