import sys

size = []

for i in range(int(sys.stdin.readline())):
    size.append(list(map(int, sys.stdin.readline().split())))

for standard_weight, standard_height in size:
    rank = 1
    for weight, height in size:
        if weight > standard_weight and height > standard_height:
            rank += 1

    print(rank)