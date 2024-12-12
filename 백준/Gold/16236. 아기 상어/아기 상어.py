import sys
import heapq

N = int(sys.stdin.readline())

size = 2
feed = 0
start_y, start_x = -1, -1

sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            start_y, start_x = i, j
            sea[i][j] = 0
            break
    if start_y != -1 and start_x != -1:
        break

result = 0

need_visit = []
heapq.heappush(need_visit, [0, start_y, start_x])
visited = [[False for _ in range(N)] for _ in range(N)]
visited[start_y][start_x] = True

while need_visit:

    cur_count, cur_y, cur_x = heapq.heappop(need_visit)

    if 0 < sea[cur_y][cur_x] < size:
        sea[cur_y][cur_x] = 0
        feed += 1
        if feed == size:
            size += 1
            feed = 0
        need_visit = []
        heapq.heappush(need_visit, [0, cur_y, cur_x])
        visited = [[False for _ in range(N)] for _ in range(N)]
        visited[cur_y][cur_x] = True
        result += cur_count
    else:
        for next_y, next_x in [[cur_y + 1, cur_x], [cur_y - 1, cur_x], [cur_y, cur_x - 1], [cur_y, cur_x + 1]]:
            if 0 <= next_y < N and 0 <= next_x < N and not visited[next_y][next_x] and sea[next_y][next_x] <= size:
                visited[next_y][next_x] = True
                heapq.heappush(need_visit, [cur_count + 1, next_y, next_x])


print(result)