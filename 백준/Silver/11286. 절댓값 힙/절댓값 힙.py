import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    value = int(sys.stdin.readline())

    if value == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, [max(value, value * -1), value])
