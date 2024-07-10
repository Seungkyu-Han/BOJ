import sys

arr = [0 for i in range(10001)]

for _ in range(int(sys.stdin.readline())):
    arr[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(arr[i]):
        print(i)