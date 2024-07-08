def solution(l, r):
    answer = []
    l = l if l % 5 == 0 else l + 5 - (l % 5)
    for i in range(l, r + 1, 5):
        if isZeroOrFive(i):
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer

def isZeroOrFive(number):
    while number > 0:
        if not (number % 10 == 0 or number % 10 == 5):
            return False
        number //= 10
    return True