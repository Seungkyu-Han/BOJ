def solution(quiz):
    answer = []
    for exp in quiz:
        operand1, operator, operand2, equal, result = map(str, exp.split())
        operand1, operand2 = int(operand1), int(operand2)
        if operator == '-':
            if operand1 - operand2 == int(result):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if operand1 + operand2 == int(result):
                answer.append('O')
            else:
                answer.append('X')
    return answer