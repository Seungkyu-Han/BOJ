import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline().strip())):
    heapq.heappush(heap, int(sys.stdin.readline().strip()))

result = 0

while len(heap) > 1:
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)

    result += (A + B)
    heapq.heappush(heap, A + B)

print(result)