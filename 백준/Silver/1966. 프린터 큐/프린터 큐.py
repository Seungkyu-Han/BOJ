import sys
import heapq
from collections import deque

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())

    print_list = list(map(int, sys.stdin.readline().split()))

    print_queue = deque()
    print_heap = []

    for i in range(len(print_list)):
        print_queue.append([print_list[i], i])
        heapq.heappush(print_heap,  -1 * print_list[i])

    count = 1

    while print_queue:

        if print_queue[0][0] == print_heap[0] * -1:
            if print_queue[0][1] == M:
                break
            else:
                print_queue.popleft(), heapq.heappop(print_heap)
                count += 1
        else:
            print_queue.append(print_queue.popleft())

    print(count)
