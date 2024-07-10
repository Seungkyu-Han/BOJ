import sys

stack = []

for _ in range(int(sys.stdin.readline())):

    money = int(sys.stdin.readline())

    if money > 0:
        stack.append(money)
    else:
        stack.pop()

print(sum(stack))