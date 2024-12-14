import sys
import heapq

N = int(sys.stdin.readline())

pos = []
neg = []
result = 0

for _ in range(N):
    input_number = int(sys.stdin.readline())
    if input_number > 0:
        heapq.heappush(pos, -input_number)
    else:
        heapq.heappush(neg, input_number)

while pos:

    cur_number = - heapq.heappop(pos)

    if pos:
        next_number = -heapq.heappop(pos)
        if cur_number == 1 or next_number == 1:
            cur_number += next_number
        else:
            cur_number *= next_number

    result += cur_number

while neg:

    cur_number = heapq.heappop(neg)

    if neg:
        cur_number *= heapq.heappop(neg)

    result += cur_number

print(result)