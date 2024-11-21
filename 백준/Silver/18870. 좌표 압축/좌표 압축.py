import sys

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

sorted_array = sorted(set(array))
array_dict = dict()

for i in range(len(sorted_array)):
    array_dict[sorted_array[i]] = i

for i in range(N):
    print(array_dict[array[i]], end=' ')

print()