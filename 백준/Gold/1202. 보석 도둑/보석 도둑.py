import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

jewelry = list()

for _ in range(N):
    heapq.heappush(jewelry, list(map(int, sys.stdin.readline().split())))

for _ in range(K):
    heapq.heappush(jewelry, [int(sys.stdin.readline().strip()), float('inf')])

result = 0
cur_jewelry = list()

while jewelry:

    weight, value = heapq.heappop(jewelry)

    if value == float('inf'):
        if cur_jewelry:
            result += heapq.heappop(cur_jewelry)
    else:
        heapq.heappush(cur_jewelry, value * -1)


print(result * -1)