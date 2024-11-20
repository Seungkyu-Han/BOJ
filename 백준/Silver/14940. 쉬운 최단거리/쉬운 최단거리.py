import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

origin_map = []

start_y, start_x = -1, -1

for i in range(n):
    input_list = list(map(int, sys.stdin.readline().split()))

    for j in range(m):
        if input_list[j] == 2:
            start_y, start_x = i, j
    origin_map.append(input_list)

destination_map = [[float('inf') for _ in range(m)] for _ in range(n)]

need_visit = deque()

need_visit.append([start_y, start_x, 0])

while need_visit:

    cur_y, cur_x, cur_count = need_visit.popleft()

    if cur_count > destination_map[cur_y][cur_x]:
        continue

    for next_y, next_x in [[cur_y - 1, cur_x], [cur_y + 1, cur_x], [cur_y, cur_x - 1], [cur_y, cur_x + 1]]:
        if 0 <= next_y < n and 0 <= next_x < m and origin_map[next_y][next_x] == 1 and destination_map[next_y][next_x] > cur_count + 1:
            destination_map[next_y][next_x] = cur_count + 1
            need_visit.append([next_y, next_x, cur_count + 1])


destination_map[start_y][start_x] = 0

for i in range(n):
    for j in range(m):
        if origin_map[i][j] == 0:
            print(0, end=' ')

        elif destination_map[i][j] == float('inf'):
            print(-1, end=' ')
        else:
            print(destination_map[i][j], end=' ')
    print()