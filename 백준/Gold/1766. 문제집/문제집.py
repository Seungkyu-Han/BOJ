import heapq
import sys

N, M = map(int, sys.stdin.readline().split())

inDegree = [0 for _ in range(N + 1)]
outDegree = [set() for _ in range(N + 1)]

zeroDegreeSet = set([i for i in range(1, N + 1)])

for _ in range(M):
    easy, hard = map(int, sys.stdin.readline().split())

    inDegree[hard] += 1
    outDegree[easy].add(hard)

    if hard in zeroDegreeSet:
        zeroDegreeSet.remove(hard)

zeroDegreeHeap = list(zeroDegreeSet)
heapq.heapify(zeroDegreeHeap)

result = []

while zeroDegreeHeap:

    cur_node = heapq.heappop(zeroDegreeHeap)

    result.append(cur_node)

    for next_node in outDegree[cur_node]:
        inDegree[next_node] -= 1
        if inDegree[next_node] == 0:
            heapq.heappush(zeroDegreeHeap, next_node)

print(*result)