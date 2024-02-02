import sys
import heapq

heap = []

N = int(sys.stdin.readline().strip())

for i in range(N):
    S, T = map(int, sys.stdin.readline().split())

    heapq.heappush(heap, [S, T])

room = list()
heapq.heappush(room, heap[0][1])
heapq.heappop(heap)

while heap:
    heap_S, heap_T = heapq.heappop(heap)

    if room[0] <= heap_S:
        heapq.heappush(room, heap_T)
        heapq.heappop(room)
    else:
        heapq.heappush(room, heap_T)


print(len(room))