from collections import deque
import sys

def find_length(n):
    cnt = 0

    while n > 0:
        cnt += 1
        n //= 10

    return cnt

def find_not_zero(n):
    cnt = 0

    while n > 0 :
        if n % 10 != 0:
            cnt += 1
        n //= 10
    return cnt

def find_by_index(n, index):
    return (n // (10 ** index)) % 10

def change(n, index1, index2):
    pos1 = find_by_index(n, index1)
    pos2 = find_by_index(n, index2)

    changed = n - (pos1 * (10 ** index1)) - (pos2 * (10 ** index2))
    changed = changed + (pos2 * (10 ** index1)) + (pos1 * (10 ** index2))

    return changed


N, K = map(int, sys.stdin.readline().split())

length = find_length(N)

if length > 2 or find_not_zero(N) > 1:

    visited = set()
    need_visit = deque()
    need_visit.append([0, N])

    result = 0

    while need_visit:

        cur_cnt, cur_num = need_visit.popleft()

        if cur_cnt == K:
            result = max(result, cur_num)
            continue

        next_cnt = cur_cnt + 1

        for i in range(length):
            for j in range(length):
                if i != j and not (i == length - 1 and find_by_index(cur_num, j) == 0):
                    next_num = change(cur_num, i, j)
                    if (next_cnt, next_num) not in visited:
                        visited.add((next_cnt, next_num))
                        need_visit.append([next_cnt, next_num])

    print(result)
else:
    print(-1)