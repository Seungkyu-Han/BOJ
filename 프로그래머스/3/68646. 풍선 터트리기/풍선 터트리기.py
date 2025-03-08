import heapq

def solution(a):
    answer = min(2, len(a))
    
    right_min_list = [0 for _ in range(len(a))]
    right_min_list[-1] = a[-1]
    
    for i in range(len(a) - 2, -1, -1):
        right_min_list[i] = min(right_min_list[i + 1], a[i])
    
    left_min = a[0]
    
    for i in range(1, len(a) - 1):
        right_min = right_min_list[i + 1]
        cur = a[i]
        
        if left_min > cur or right_min > cur:
            answer += 1
        
        left_min = min(left_min, cur)
    
    return answer