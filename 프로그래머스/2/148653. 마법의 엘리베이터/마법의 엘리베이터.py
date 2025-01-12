def solution(storey):
    
    need_visit = []
    
    visited = dict()
    
    need_visit.append([storey, 0])
    visited[storey] = 0
    
    while need_visit:
        cur_storey, cnt = need_visit.pop()
        
        if visited[cur_storey] < cnt:
            continue
        
        #up
        up_cur_cnt = 10 - (cur_storey % 10)
        up_next = (cur_storey + up_cur_cnt) // 10
        up_cnt = cnt + up_cur_cnt
        
        if up_next not in visited or visited[up_next] > up_cnt:
            visited[up_next] = up_cnt
            need_visit.append([up_next, up_cnt])
        
        #down
        down_cur_cnt = cur_storey % 10
        down_next = cur_storey // 10
        down_cnt = cnt + down_cur_cnt
        
        if down_next not in visited or visited[down_next] > down_cnt:
            visited[down_next] = down_cnt
            need_visit.append([down_next, down_cnt])
        
    
    
    answer = visited[0]
    return answer