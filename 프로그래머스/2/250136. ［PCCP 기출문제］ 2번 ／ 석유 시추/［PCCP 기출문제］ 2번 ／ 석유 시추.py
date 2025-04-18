def solution(land):
    answer = 0
    return max(dfs(land))

def dfs(land):
    x_length = len(land[0])
    y_length = len(land)
    
    acc = [0 for _ in range(x_length)]
    
    visited = [[False for _ in range(x_length)] for _ in range(y_length)]
    
    for x in range(x_length):
        for y in range(y_length):
            if visited[y][x]:
                continue
            
            
            visited[y][x] = True
                
            if land[y][x] == 0:
                continue
            
            min_x, max_x = x, x
            cur = 1
            
            need_visit = [[y, x]]
            
            while need_visit:
                
                cur_y, cur_x = need_visit.pop()
                
                for next_y, next_x in [[cur_y + 1, cur_x], [cur_y - 1, cur_x], [cur_y, cur_x + 1], [cur_y, cur_x - 1]]:
                    if 0 <= next_x < x_length and 0 <= next_y < y_length and visited[next_y][next_x] is False and land[next_y][next_x] == 1:
                        visited[next_y][next_x] = True
                        min_x, max_x = min(min_x, next_x), max(max_x, next_x)
                        need_visit.append([next_y, next_x])
                        cur += 1
            for to_x in range(min_x, max_x + 1):
                acc[to_x] += cur
                        
    return acc
                    