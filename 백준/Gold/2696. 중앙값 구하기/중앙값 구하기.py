import math
import heapq
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M = int(sys.stdin.readline())

    test_case = []

    for i in range(M // 10 + 1):
        test_case += list(map(int, sys.stdin.readline().split()))

    rep_cnt = math.ceil(M / 2)

    result = []

    print(rep_cnt)

    small_heap = []
    median = test_case[0]
    big_heap = []

    result.append(median)

    for i in range(1, M, 2):
        pre_index = i
        cur_index = i + 1

        pre_num = test_case[pre_index]
        cur_num = test_case[cur_index]

        if pre_num <= median:
            heapq.heappush(small_heap, pre_num * - 1)
        else:
            heapq.heappush(big_heap, pre_num)

        if cur_num <= median:
            heapq.heappush(small_heap, cur_num * -1)
        else:
            heapq.heappush(big_heap, cur_num)

        if len(small_heap) > len(big_heap):
            heapq.heappush(big_heap, median)
            median = heapq.heappop(small_heap) * -1
        elif len(small_heap) < len(big_heap):
            heapq.heappush(small_heap, median * -1)
            median = heapq.heappop(big_heap)

        result.append(median)

    for i in range(len(result)):
        if i != 0 and i % 10 == 0:
            print()
        print(result[i], end = ' ')
    print()