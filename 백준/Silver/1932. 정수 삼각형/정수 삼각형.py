import sys

n = int(sys.stdin.readline())

max_list = [0 for i in range(n)]

for i in range(n):
    level = list(map(int, sys.stdin.readline().split()))
    cur_max_list = list()

    for t in range(i+1):
        if t == 0:
            cur_max_list.append(max_list[0] + level[0])
        elif t == i:
            cur_max_list.append(max_list[-1] + level[i])
        else:
            cur_max_list.append(max(max_list[t-1], max_list[t]) + level[t])
    max_list = cur_max_list

print(max(max_list))