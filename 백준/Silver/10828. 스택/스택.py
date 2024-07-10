import sys

stack = []

for _ in range(int(sys.stdin.readline())):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)