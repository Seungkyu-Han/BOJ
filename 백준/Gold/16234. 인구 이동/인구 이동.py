import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, L, R = map(int, sys.stdin.readline().split())

nation = list()

for _ in range(N):
    nation.append(list(map(int, sys.stdin.readline().split())))

flag = True

result = 0

while flag:

    flag = False

    visited = [[False for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if visited[r][c] is False:

                visited[r][c] = True

                need_visit = deque()
                change = [[r, c]]

                need_visit.append([r, c])

                people = nation[r][c]

                while need_visit:

                    cur_r, cur_c = need_visit.popleft()

                    for d in range(4):
                        next_r, next_c = cur_r + dx[d], cur_c + dy[d]
                        if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] is False and L <= abs(nation[cur_r][cur_c] - nation[next_r][next_c]) <= R:
                            change.append([next_r, next_c])
                            visited[next_r][next_c] = True
                            need_visit.append([next_r, next_c])
                            people += nation[next_r][next_c]
                            flag = True

                per_people = people // len(change)

                for next_r, next_c in change:
                    nation[next_r][next_c] = per_people

    if flag:
        result += 1

print(result)