import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

need_visit = deque()
need_visit.append([0, N])
visited = [False for _ in range(100001)]
visited[N] = True

while need_visit:
    cur_count, cur_position = need_visit.popleft()

    if cur_position == K:
        print(cur_count)
        break

    for next_position in [cur_position + 1, cur_position - 1, cur_position * 2]:
         if 0 <= next_position <= 100000 and visited[next_position] is False:
            need_visit.append([cur_count + 1, next_position])
            visited[next_position] = True
