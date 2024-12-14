import sys
import heapq

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

sensor = sorted(list(set(list(map(int, sys.stdin.readline().split())))))

distances = []

for i in range(len(sensor) - 1):
    heapq.heappush(distances, - (sensor[i + 1] - sensor[i]))

for _ in range(K - 1):
    if distances:
        heapq.heappop(distances)

result = 0

while distances:
    result -= heapq.heappop(distances)

print(result)