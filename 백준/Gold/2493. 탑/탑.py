import sys

N = int(sys.stdin.readline())

tops = list(map(int, sys.stdin.readline().split()))

stack = []

result = []

for i in range(len(tops)):

    while stack and tops[stack[-1]]  < tops[i]:
        stack.pop()

    if len(stack) == 0:
        result.append(0)
    else:
        result.append(stack[-1] + 1)

    stack.append(i)

print(*result)