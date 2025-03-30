import heapq
import sys

N = int(sys.stdin.readline())

max_day = 0

days = dict()

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())

    max_day = max(max_day, d)

    if d in days:
        days[d].append(w)
    else:
        days[d] = [w]


day_heap = []

result = 0

for i in range(max_day, 0, -1):

    if i in days:
        for w in days[i]:
            heapq.heappush(day_heap, -w)

    if day_heap:
        result += (heapq.heappop(day_heap) * -1)

print(result)