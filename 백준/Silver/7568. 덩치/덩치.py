import sys

size = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

for standard_weight, standard_height in size:
    rank = 1
    for weight, height in size:
        if weight > standard_weight and height > standard_height:
            rank += 1

    print(rank)