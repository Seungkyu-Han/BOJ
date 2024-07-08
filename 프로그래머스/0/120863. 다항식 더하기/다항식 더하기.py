def solution(polynomial):
    exp = [0, 0]
    for op in polynomial.split():
        if op == '+':
            pass
        else:
            if op[-1] == 'x':
                if len(op) == 1:
                    exp[0] += 1
                else:
                    exp[0] += int(op[:-1])
            else:
                exp[1] += int(op)
    answer = ''
    if exp[0] > 0:
        answer += f'{exp[0]}x' if exp[0] > 1 else 'x'
    if exp[0] > 0 and exp[1] > 0:
        answer += ' + '
    if exp[1] > 0:
        answer += f'{exp[1]}'
    return answer