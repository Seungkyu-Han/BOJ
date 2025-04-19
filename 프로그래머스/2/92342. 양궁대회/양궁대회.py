def solution(n, info):
    score, answer = back_tracking([0 for _ in range(11)], info, n, 0)
    
    if score <= 0:
        return [-1]
    
    return answer

def back_tracking(ryan, apeech, n, cur_score):
    
    if cur_score == 11:
        
        if n > 0:
            return [-1, [0 for _ in range(11)]]
        
        a_score = 0
        r_score = 0
        
        for i in range(10):
            score = 10 - i
            if ryan[i] == 0 and apeech[i] == 0:
                continue
            
            if ryan[i] <= apeech[i]:
                a_score += score
            else:
                r_score += score
        
        return [r_score - a_score, ryan.copy()]
    
    result = -1
    result_ryan = [0 for _ in range(11)]
    
    
    for j in range(n + 1):
        ryan[cur_score] += j
        cur = back_tracking(ryan, apeech, n - j, cur_score + 1)
        if cur[0] > result:
            result = cur[0]
            result_ryan = cur[1]
        if cur[0] == result:
            flag = False
            for k in range(10, -1, -1):
                if result_ryan[k] > cur[1][k]:
                    flag = False
                    break
                elif result_ryan[k] < cur[1][k]:
                    flag = True
                    break
            if flag:
                result_ryan = cur[1]
        ryan[cur_score] -= j
    
        
    return [result, result_ryan]
        