def solution(queue1, queue2):
    
    total = queue1 + queue2
    
    total_sum = sum(total)
    
    acc = [0]
    
    for i in range(len(total)):
        acc.append(acc[-1] + total[i])
    
    if total_sum % 2 != 0:
        return -1
    
    start, end = 0, len(queue1)
    
    cnt = 0
    
    while start < end and start < len(total) and end < len(total):
        
        cur_sum = acc[end] - acc[start]
        
        if cur_sum == total_sum // 2:
            return cnt
        
        if cur_sum > total_sum // 2:
            start += 1
        else:
            end += 1
                
        cnt += 1
    
    return -1