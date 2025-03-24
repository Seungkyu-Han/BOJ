import sys
import heapq

N, C = map(int, sys.stdin.readline().split())

post = [[] for _ in range(N + 1)]

M = int(sys.stdin.readline())

for i in range(M):
    start, end, box = map(int, sys.stdin.readline().split())

    heapq.heappush(post[end], [start * -1, box])

answer = 0
weight = 0
car = []

for i in range(N, 0, -1):
    while car and car[0][0] == i * -1:
        start, box = heapq.heappop(car)
        answer += box
        weight -= box

    while post[i]:
        start, box = heapq.heappop(post[i])

        if weight + box >= C:
            heapq.heappush(car, [start, C - weight])
            weight = C
        else:
            heapq.heappush(car, [start, box])
            weight += box

print(answer)