import sys

N, M, H = map(int, sys.stdin.readline().split())

jump = [[False for _ in range(H + 1)] for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    jump[b][a] = True


def check_ladder():
    for start in range(1, N + 1):
        cur_ladder = start
        for position in range(1, H + 1):
            if jump[cur_ladder - 1][position]:
                cur_ladder -= 1
            elif cur_ladder != N and jump[cur_ladder][position]:
                cur_ladder += 1
        if cur_ladder != start:
            return False
    return True


def back_tracking(cur_n, cur_h, count):

    if count == 4 or (cur_n > N and cur_h > H):
        return -1

    if check_ladder():
        return count

    result = 4

    for n in range(cur_n, N):
        if jump[n][cur_h] is False:
            jump[n][cur_h] = True
            cur_result = back_tracking(n + 1, cur_h, count + 1)
            if cur_result != -1:
                result = min(cur_result, result)
            jump[n][cur_h] = False

    for h in range(cur_h + 1, H + 1):
        for n in range(1, N):
            if jump[n][h] is False:
                jump[n][h] = True
                cur_result = back_tracking(n + 1, h, count + 1)
                if cur_result != -1:
                    result = min(cur_result, result)
                jump[n][h] = False

    return result if result != 4 else -1

print(back_tracking(1, 1, 0))