def solution(grid):
    
    # 0: 위에서 들어옴
    # 1: 오른쪽에서 들어옴
    # 2: 아래에서 들어옴
    # 3: 왼쪽에서 들어옴

    answer = []
    
    y_length = len(grid)
    x_length = len(grid[0])
    
    visited = [[[False, False, False, False] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                if visited[i][j][d]:
                    continue
                    
                cur_i, cur_j, cur_d = i, j, d
                
                length = 0
                
                while visited[cur_i][cur_j][cur_d] is False:
                    
                    length += 1
                    visited[cur_i][cur_j][cur_d] = True
                    
                    if grid[cur_i][cur_j] == 'S':
                        if cur_d == 0:
                            cur_i = (cur_i + 1) % y_length
                        elif cur_d == 1:
                            cur_j = (cur_j - 1 + x_length) % x_length
                        elif cur_d == 2:
                            cur_i = (cur_i - 1 + y_length) % y_length
                        else:
                            cur_j = (cur_j + 1) % x_length
                    elif grid[cur_i][cur_j] == 'L':
                        if cur_d == 0:
                            cur_j = (cur_j + 1) % x_length
                        elif cur_d == 1:
                            cur_i = (cur_i + 1) % y_length
                        elif cur_d == 2:
                            cur_j = (cur_j - 1 + x_length) % x_length
                        else:
                            cur_i = (cur_i - 1 + y_length) % y_length
                        cur_d = (cur_d + 3) % 4
                    else:
                        if cur_d == 0:
                            cur_j = (cur_j - 1 + x_length) % x_length
                        elif cur_d == 1:
                            cur_i = (cur_i - 1 + y_length) % y_length
                        elif cur_d == 2:
                            cur_j = (cur_j + 1) % x_length
                        else:
                            cur_i = (cur_i + 1) % y_length
                        cur_d = (cur_d + 1) % 4
                        
                answer.append(length)
                
    answer.sort()
                        
    
    return answer