import sys

N = int(sys.stdin.readline().strip())

M = int(sys.stdin.readline().strip())

IOI = list(sys.stdin.readline().strip())

count = 0
result = 0

first = False
second = False

for i in range(len(IOI)):
    cur_char = IOI[i]
    if cur_char == 'I':
        if first and second:
            second = False
            count += 1
            if count >= N:
                result += 1
        else:
            first = True
            second = False
            count = 0
    else:
        if first and second:
            first = False
            second = False
            count = 0
        elif first:
            second = True
        else:
            first = False
            second = False
            count = 0

print(result)