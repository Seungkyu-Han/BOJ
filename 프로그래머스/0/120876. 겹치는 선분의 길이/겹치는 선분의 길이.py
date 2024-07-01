def solution(lines):
    line = [0 for i in range(200)]
    
    for start, end in lines:
        for position in range(start, end):
            line[position] += 1
    
    answer = 0
    
    for i in line:
        if i > 1:
            answer += 1
    
    return answer