import sys

N = int(sys.stdin.readline())

min_list = [0 for i in range(3)]

for i in range(N):
    color = list(map(int, sys.stdin.readline().split()))
    min_list = [
        min(min_list[1], min_list[2]) + color[0],
        min(min_list[0], min_list[2]) + color[1],
        min(min_list[0], min_list[1]) + color[2]
    ]

print(min(min_list))