import sys, heapq

n = int(sys.stdin.readline())

max_day = 0

lectures = [[] for _ in range(10001)]
result = 0

max_day = 0

for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())

    max_day = max(max_day, d)

    lectures[d].append(p)

result = 0
lecture_heap = []

for today in range(max_day, 0, -1):

    for today_pay in lectures[today]:
        heapq.heappush(lecture_heap, today_pay * -1)

    today_max = 0

    if lecture_heap:
        today_max = heapq.heappop(lecture_heap) * -1

    result += today_max

print(result)
