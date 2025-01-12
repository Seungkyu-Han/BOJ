from collections import deque

N, K = map(int, input().split())
first_k = K
target = list(map(int, input().rstrip()))

stack = deque()

for num in target:
    while K > 0 and stack and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

result = list(stack)[:N - first_k]
print("".join(map(str, result)))
