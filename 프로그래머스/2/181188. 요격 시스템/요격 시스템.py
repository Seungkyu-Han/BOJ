def solution(targets):
    answer = 0
    
    cur_index = -1
    
    targets.sort(key = lambda x: x[1])
    
    for cur_start, cur_end in targets:
        if cur_start > cur_index:
            cur_index = cur_end - 1
            answer += 1
    
    return answer