import sys

N = int(sys.stdin.readline())

land = list()

for _ in range(N):
    land.append(list(map(int, sys.stdin.readline().split())))

max_result = 0

for height in range(101):
    result = 0

    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for t in range(N):
            if visited[i][t] is False and land[i][t] > height:
                visited[i][t] = True
                need_visit = [[i, t]]

                result += 1

                while need_visit:
                    cur_i, cur_t = need_visit.pop()

                    for next_i, next_t in [[cur_i + 1, cur_t], [cur_i - 1, cur_t], [cur_i, cur_t + 1], [cur_i, cur_t - 1]]:
                        if 0 <= next_i < N and 0 <= next_t < N and not visited[next_i][next_t] and land[next_i][next_t] > height:
                            need_visit.append([next_i, next_t])
                            visited[next_i][next_t] = True

    max_result = max(max_result, result)

print(max_result)