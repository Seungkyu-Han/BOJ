import sys

N = int(sys.stdin.readline())

village = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]

island = list()

for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue

        if village[i][j] == 0:
            visited[i][j] = True
            continue

        need_visit = [[i, j]]

        cur_island = set()
        cur_island.add((i, j))

        while need_visit:

            cur_i, cur_j = need_visit.pop()

            for next_i, next_j in [[cur_i + 1, cur_j], [cur_i - 1, cur_j], [cur_i, cur_j + 1], [cur_i, cur_j - 1]]:
                if 0 <= next_i < N and 0 <= next_j < N and not visited[next_i][next_j] and village[next_i][next_j] == 1:
                    visited[next_i][next_j] = True
                    cur_island.add((next_i, next_j))
                    need_visit.append([next_i, next_j])
        island.append(cur_island)


result = float('inf')

for i in range(len(island)):
    for j in range(i + 1, len(island)):

        for i_x, i_y in island[i]:
            for j_x, j_y in island[j]:
                result = min(result, (abs(i_x - j_x) - 1) + (abs(i_y - j_y) - 1))

print(result + 1)