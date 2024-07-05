import sys

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    house = [i + 1 for i in range(n)]

    for i in range(k):
        tmp_house = [sum(house[:i + 1]) for i in range(n)]
        house = tmp_house

    print(house[-1])
