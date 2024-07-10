import sys
from collections import deque


def parenthesis(ps):
    stack = deque()
    for ch in ps:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack or stack.pop() != '(':
                return False
    return True if len(stack) == 0 else False


for _ in range(int(sys.stdin.readline())):
    input_string = sys.stdin.readline().strip()
    print('YES' if parenthesis(input_string) else 'NO')