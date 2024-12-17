import sys

N = int(sys.stdin.readline())

liquid = sorted(list(map(int, sys.stdin.readline().split())))

result = [0, 1, 2]

for i in range(N - 2):
    left = i + 1
    right = N - 1

    while left < right:

        cur_liquid = liquid[i] + liquid[left] + liquid[right]

        if abs(liquid[result[0]] + liquid[result[1]] + liquid[result[2]]) > abs(cur_liquid):
            result = [i, left, right]

        if cur_liquid >= 0:
            right -= 1
        else:
            left += 1

for i in result:
    print(liquid[i], end = ' ')