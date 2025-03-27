import sys
import heapq

n = int(sys.stdin.readline())

buildings = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    heapq.heappush(buildings, [x, y])

stack = []
result = 0

while buildings:

    x, y = heapq.heappop(buildings)

    if y == 0:
        stack = []
        continue

    if len(stack) == 0 or stack[-1] < y:
        result += 1
        stack.append(y)
    elif stack[-1] > y:
        while stack:
            if stack[-1] > y:
                stack.pop()
            else:
                break
        if len(stack) == 0 or stack[-1] < y:
            result += 1
            stack.append(y)

print(result)
