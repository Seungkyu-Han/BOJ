from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

queue = deque([i+1 for i in range(N)])

print("<", end='')

for i in range(N - 1):
    for t in range(K - 1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=", ")

print(queue.popleft(), end=">\n")