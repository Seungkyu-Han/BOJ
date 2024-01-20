import sys

N = int(input())

A = list(map(int, sys.stdin.readline().split()))

result = [[None] for i in range(N)]

for i in range(N):
    cur_list = [A[i]]
    for t in range(i):
        if A[i] > A[t]:
            if len(cur_list) < len(result[t]) + 1:
                cur_list = result[t] + [A[i]]
    result[i] = cur_list

result.sort(key= lambda x : len(x))

print(len(result[-1]))