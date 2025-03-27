import sys

N = int(sys.stdin.readline())

crains = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

boxes = list(map(int, sys.stdin.readline().split()))

is_shipped = [False for _ in range(M)]

crains.sort()

boxes.sort()

def solve():

    if boxes[-1] > crains[-1]:
        return -1

    crains_start_index = [-1 for _ in range(N)]

    cur_start_index = 0

    for i in range(M):
        while boxes[i] > crains[cur_start_index]:
            crains_start_index[cur_start_index] = i - 1
            cur_start_index += 1
        crains_start_index[cur_start_index] = i

    for i in range(cur_start_index + 1, N):
        crains_start_index[i] = M - 1
        

    cur_shipped = crains_start_index.copy()
    shipped_count = 0

    for i in range(1, 10001):

        for j in range(N):
            if cur_shipped[j] == -1:
                continue

            cur_index = cur_shipped[j]
            while cur_index > -1 and is_shipped[cur_index] is True:
                cur_index -= 1

            if cur_index > -1:
                is_shipped[cur_index] = True
                shipped_count += 1
            cur_shipped[j] = cur_index

        if shipped_count == M:
            return i

    return 10000
    
    

print(solve())