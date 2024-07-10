from collections import deque
import sys

queue = deque()

for _ in range(int(sys.stdin.readline())):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0 if queue else 1)
    elif command[0] == 'front':
        if queue:
            data = queue.popleft()
            print(data)
            queue.appendleft(data)
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            data = queue.pop()
            print(data)
            queue.append(data)
        else:
            print(-1)