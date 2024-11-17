import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

person = {}

for _ in range(N):
    person[sys.stdin.readline().strip()] = 1

for _ in range(M):
    who = sys.stdin.readline().strip()
    if who in person:
        person[who] += 1

heap = []

for k, v in person.items():
    if v == 2:
        heapq.heappush(heap, k)

print(len(heap))

while heap:
    print(heapq.heappop(heap))