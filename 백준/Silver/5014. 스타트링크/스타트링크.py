import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

stair = [float('inf') for _ in range(F + 1)]
stair[S] = 0

need_visit = deque()

need_visit.append(S)

while need_visit:

    cur_stair = need_visit.popleft()

    if cur_stair == G:
        break

    next_up, next_down = cur_stair + U, cur_stair - D

    next_cnt = stair[cur_stair] + 1

    if 0 < next_up <= F and stair[next_up] > next_cnt:
        stair[next_up] = next_cnt
        need_visit.append(next_up)

    if 0 < next_down <= F and stair[next_down] > next_cnt:
        stair[next_down] = next_cnt
        need_visit.append(next_down)


print(stair[G] if stair[G] != float('inf') else "use the stairs")