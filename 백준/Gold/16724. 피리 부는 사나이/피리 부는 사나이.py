import sys

N, M = map(int, sys.stdin.readline().split())

flute = []

for i in range(N):
    flute.append(list(sys.stdin.readline().rstrip()))

visited = [[False for _ in range(M)] for _ in range(N)]

result = 0

for n in range(N):
    for m in range(M):
        if visited[n][m]:
            continue

        result += 1

        need_visit = [[n, m]]
        visited[n][m] = True

        while need_visit:

            cur_n, cur_m = need_visit.pop()

            # UP
            next_n, next_m = cur_n - 1, cur_m
            if 0 <= next_n < N and 0 <= next_m < M and visited[next_n][next_m] == False:
                if flute[next_n][next_m] == 'D':
                    need_visit.append([next_n, next_m])
                    visited[next_n][next_m] = True

            # DOWN
            next_n, next_m = cur_n + 1, cur_m
            if 0 <= next_n < N and 0 <= next_m < M and visited[next_n][next_m] == False:
                if flute[next_n][next_m] == 'U':
                    need_visit.append([next_n, next_m])
                    visited[next_n][next_m] = True

            # LEFT
            next_n, next_m = cur_n, cur_m - 1
            if 0 <= next_n < N and 0 <= next_m < M and visited[next_n][next_m] == False:
                if flute[next_n][next_m] == 'R':
                    need_visit.append([next_n, next_m])
                    visited[next_n][next_m] = True

            # RIGHT
            next_n, next_m = cur_n, cur_m + 1
            if 0 <= next_n < N and 0 <= next_m < M and visited[next_n][next_m] == False:
                if flute[next_n][next_m] == 'L':
                    need_visit.append([next_n, next_m])
                    visited[next_n][next_m] = True

            # FORWARD
            if flute[cur_n][cur_m] == 'U':
                next_n, next_m = cur_n - 1, cur_m
            elif flute[cur_n][cur_m] == 'D':
                next_n, next_m = cur_n + 1, cur_m
            elif flute[cur_n][cur_m] == 'L':
                next_n, next_m = cur_n, cur_m - 1
            else:
                next_n, next_m = cur_n, cur_m + 1

            if not visited[next_n][next_m]:
                need_visit.append([next_n, next_m])
                visited[next_n][next_m] = True

print(result)