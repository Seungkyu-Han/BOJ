import sys

N = int(sys.stdin.readline())

fruits = list(map(int, sys.stdin.readline().split()))

cur_fruit = [0 for _ in range(10)]

left, right = 0, 0
cur_fruit[fruits[left]] += 1

result = 1

while right + 1 < N:

    if cur_fruit[fruits[right + 1]] > 0 or cur_fruit.count(0) > 8:
        right += 1
        cur_fruit[fruits[right]] += 1
        result = max(result, right - left + 1)
    else:
        cur_fruit[fruits[left]] -= 1
        left += 1

print(result)