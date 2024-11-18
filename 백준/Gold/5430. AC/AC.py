import sys
from collections import deque

for _ in range(int(sys.stdin.readline().strip())):

    function = list(sys.stdin.readline().strip())

    n = int(sys.stdin.readline().strip())

    array_input = list(map(str, sys.stdin.readline().strip().replace('[', '').replace(']', '').split(',', )))
    array = []
    if n > 0:
        array = list(map(int, array_input))

    queue = deque(array)\

    isError = False
    isReverse = False

    for func in function:
        if func == 'R':
            isReverse = not isReverse
        else:
            if len(queue) <= 0:
                isError = True
                break
            else:
                if isReverse:
                    queue.pop()
                else:
                    queue.popleft()

    if isError:
        print('error')
    else:
        print('[', end='')
        if isReverse:
            while queue:
                print(queue.pop(), end='')
                if queue:
                    print(",", end='')
        else:
            while queue:
                print(queue.popleft(), end='')
                if queue:
                    print(",", end='')

        print(']\n', end='')