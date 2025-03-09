import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

sub = [[] for _ in range(n + 1)]
comp =[0 for _ in range(n + 1)]
boss_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    sub[boss_list[i]].append(i + 1)

for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())

    comp[i] += w

need_visit = deque([1])

while need_visit:

    cur_node = need_visit.popleft()

    for next_node in sub[cur_node]:
        comp[next_node] += comp[cur_node]
        need_visit.append(next_node)


for i in range(1, n + 1):
    print(comp[i], end = ' ')