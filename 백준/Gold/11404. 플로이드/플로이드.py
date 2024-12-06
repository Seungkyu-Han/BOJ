import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

city = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    city[i][i] = 0

for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    city[start - 1][end - 1] = min(weight, city[start - 1][end - 1]) 


for index1 in range(n):
    for index2 in range(n):
        for index3 in range(n):
            city[index2][index3] = min(city[index2][index3], city[index2][index1] + city[index1][index3])


for i in range(n):
    for j in range(n):
        print(city[i][j] if city[i][j] != float('inf') else 0, end=' ')
    print()