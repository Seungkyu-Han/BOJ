import sys
from _collections import deque

N, K = map(int, sys.stdin.readline().split())

result = -1
result_count = 0

visited = [float('inf') for _ in range(100001)]
visited[N] = 0
need_visit = deque()
#cur_position, cur_count
need_visit.append([N, 0])

while need_visit:

    cur_position, cur_count = need_visit.popleft()


    if cur_position == K:
        if result == -1:
            result = cur_count
        result_count += 1

    if 0 < result < cur_count:
        break

    for next_position in [cur_position - 1, cur_position + 1, cur_position * 2]:
        if 0 <= next_position <= 100000 and visited[next_position] >= cur_count + 1:
            visited[next_position] = cur_count + 1
            need_visit.append([next_position, cur_count + 1])

print(result)
print(result_count)