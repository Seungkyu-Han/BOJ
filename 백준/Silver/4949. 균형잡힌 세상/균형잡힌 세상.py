import sys

while True:
    input_str = sys.stdin.readline().rstrip()

    if input_str == '.':
        break

    stack = []
    flag = True

    for ch in input_str:
        if ch == '[':
            stack.append(ch)
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break

    print('yes' if flag and len(stack) == 0 else 'no')