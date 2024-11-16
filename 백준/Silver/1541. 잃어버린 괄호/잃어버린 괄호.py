import sys

input_str = list(sys.stdin.readline().strip())

expr = list()

cur = ''

for ch in input_str:
    if ch == '+' or ch == '-':
        expr.append(int(cur))
        cur = ''
        expr.append(ch)
    else:
        cur += ch

expr.append(int(cur))

result = 0
flag = True


for cur_expr in expr:
    if cur_expr == '-' and flag:
        flag = False

    if cur_expr != '+' and cur_expr != '-':
        if flag:
            result += cur_expr
        else:
            result -= cur_expr

print(result)
