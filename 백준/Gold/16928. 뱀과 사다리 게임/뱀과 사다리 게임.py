import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

visited = [float('inf') for _ in range(101)]
jump = [i for i in range(101)]

for _ in range(N + M):
    x, y = map(int, sys.stdin.readline().split())

    jump[x] = y


need_visit = deque()

# position, count
need_visit.append([1, 0])

while need_visit:

    cur_position, cur_count = need_visit.popleft()

    if cur_position == 100:
        print(cur_count)
        break

    for dice in range(1, 7):

        next_position = cur_position + dice

        if 0 < next_position < 101 and visited[next_position] == float('inf'):
            visited[next_position] = cur_count
            need_visit.append([jump[next_position], cur_count + 1])

