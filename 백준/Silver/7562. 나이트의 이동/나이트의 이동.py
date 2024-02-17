from collections import deque
import sys

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(int(sys.stdin.readline())):
    i = int(sys.stdin.readline().strip())

    start_y, start_x = map(int, sys.stdin.readline().split())

    dest_y, dest_x = map(int, sys.stdin.readline().split())

    visited = [[float('inf') for _ in range(i)] for _ in range(i)]
    visited[start_y][start_x] = 0

    need_visit = deque()

    need_visit.append([0, start_y, start_x])

    result = -1

    while need_visit:

        cur_cnt, cur_y, cur_x = need_visit.popleft()

        if cur_y == dest_y and cur_x == dest_x:
            result = cur_cnt

        for index in range(8):
            next_y, next_x = cur_y + dy[index], cur_x + dx[index]
            if 0 <= next_y < i and 0 <= next_x < i and visited[next_y][next_x] > cur_cnt + 1:
                need_visit.append([cur_cnt + 1, next_y, next_x])
                visited[next_y][next_x] = cur_cnt + 1

    print(result)