def solution(num, total):
    start = total // num - num // 2 + 1 if num % 2 == 0 else total // num - num // 2
    answer = [i + start for i in range(num)]
    return answer