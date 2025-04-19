import sys

input_str = list(sys.stdin.readline().rstrip())

stack = []
total_score = 0
cur_score = 1

index = 0

while index < len(input_str):
    cur = input_str[index]

    if cur == '(':
        if index + 1 < len(input_str) and input_str[index + 1] == ')':
            index += 1
            total_score += cur_score * 2
        else:
            stack.append('(')
            cur_score *= 2

    elif cur == '[':
        if index + 1 < len(input_str) and input_str[index + 1] == ']':
            index += 1
            total_score += cur_score * 3
        else:
            stack.append('[')
            cur_score *= 3

    elif cur == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            cur_score //= 2
        else:
            break

    else:
        if stack and stack[-1] == '[':
            stack.pop()
            cur_score //= 3
        else:
            break
    index += 1

if stack or index != len(input_str):
    print(0)
else:
    print(total_score)
