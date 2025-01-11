import sys

R, C = map(int, sys.stdin.readline().split())

miro = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

fire = [[-1 for _ in range(C)] for _ in range(R)]
j = [[-1 for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        if miro[r][c] == 'J':
            j[r][c] = 0
            miro[r][c] = '.'
        elif miro[r][c] == 'F':
            fire[r][c] = 0
            miro[r][c] = '.'

time = 0
result = -1

while result == -1:

    # spread_fire
    for r in range(R):
        for c in range(C):
            if fire[r][c] == time:
                for fire_r, fire_c in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                    if 0 <= fire_r < R and 0 <= fire_c < C and miro[fire_r][fire_c] == '.' and fire[fire_r][fire_c] == -1:
                        fire[fire_r][fire_c] = time + 1

    # exit_j
    j_cnt = 0
    for r in range(R):
        if result != -1:
            break
        for c in range(C):
            if j[r][c] == time:
                j_cnt += 1
                for next_r, next_c in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                    if 0 <= next_r < R and 0 <= next_c < C:
                        if miro[next_r][next_c] == '.' and fire[next_r][next_c] == -1 and j[next_r][next_c] == -1:
                            j[next_r][next_c] = time + 1
                    else:
                        result = time + 1
                        break
    if j_cnt == 0:
        break
        
    time += 1
print(result if result != -1 else "IMPOSSIBLE")