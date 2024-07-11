def solution(n):
    arr = [0 for i in range(10)]
    while n > 0:
        arr[n % 10] += 1
        n //= 10
    answer = 0
    for i in range(9, -1, -1):
        for t in range(arr[i]):
            answer *= 10
            answer += i
            
    return answer