import math

def solution(r1, r2):
    answer = 0
    star = 0
    r1_square = r1 * r1
    r2_square = r2 * r2
    
    for i in range(1, r2 + 1):
        if r1_square - i * i >= 0:
            start = math.ceil(math.sqrt(r1_square - i * i))
        else:
            start = 0
        final = math.floor(math.sqrt(r2_square - i * i))
        answer += (final - start + 1)
                
    return answer * 4