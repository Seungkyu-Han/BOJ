from collections import deque
import sys
import heapq

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

result_list = list()

M, N, K = map(int, sys.stdin.readline().split())

paper = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            paper[x][y] = 1

for x in range(N):
    for y in range(M):
        if paper[x][y] == 0:
            need_visit = deque()

            paper[x][y] = -1
            need_visit.append([x, y])

            result = 0

            while need_visit:

                cur_x, cur_y = need_visit.popleft()

                result += 1

                for i in range(4):
                    next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                    if 0 <= next_x < N and 0 <= next_y < M and paper[next_x][next_y] == 0:
                        paper[next_x][next_y] = -1
                        need_visit.append([next_x, next_y])

            heapq.heappush(result_list, result)

print(len(result_list))

while result_list:
    print(heapq.heappop(result_list), end=' ')