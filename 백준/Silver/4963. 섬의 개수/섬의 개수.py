import sys

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, 0, -1, 1]

while True:

    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    land = list()
    visited = [[False for _ in range(w)] for _ in range(h)]

    result = 0

    for _ in range(h):
        land.append(list(map(int, sys.stdin.readline().split())))

    for height in range(h):
        for width in range(w):

            if visited[height][width] is True:
                continue

            if land[height][width] == 0:
                visited[height][width] = True
                continue

            result += 1

            need_visit = [[height, width]]
            visited[height][width] = True

            while need_visit:
                cur_height, cur_width = need_visit.pop(0)

                for i in range(8):
                    target_height, target_width = cur_height + dy[i], cur_width + dx[i]
                    if 0 <= target_height < h and 0 <= target_width < w and land[target_height][target_width] == 1 and not visited[target_height][target_width]:
                        need_visit.append([target_height, target_width])
                        visited[target_height][target_width] = True

    print(result)