def solution(rows, columns, queries):
    answer = []
    
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i * columns + j + 1
            
    for y1, x1, y2, x2 in queries:
        left_top = matrix[y1 - 1][x1 - 1]
        right_top = matrix[y1 - 1][x2 - 1]
        left_bottom = matrix[y2 - 1][x1 - 1]
        right_bottom = matrix[y2 - 1][x2 - 1]
        
        print(left_top, right_top, left_bottom, right_bottom)
        
        result = min(left_top, right_top, left_bottom, right_bottom)
        
        #to right
        for i in range(x2 - 1, x1 - 1, -1):
            matrix[y1 - 1][i] = matrix[y1 - 1][i-1]
            result = min(result, matrix[y1 - 1][i])
            
        #to bottom
        for i in range(y2 - 1, y1, -1):
            matrix[i][x2 - 1] = matrix[i - 1][x2 - 1]
            result = min(result, matrix[i][x2 - 1])
        matrix[y1][x2 - 1] = right_top
        result = min(result, matrix[y1 - 1][x2 - 1])
        
        #to top
        for i in range(y1 - 1, y2 - 1):
            matrix[i][x1 - 1] = matrix[i + 1][x1 - 1]
            result = min(result, matrix[i][x1 - 1])
        
        #to left
        for i in range(x1 - 1, x2 - 2):
            matrix[y2 - 1][i] = matrix[y2 - 1][i + 1]
            result = min(result, matrix[y2 - 1][i])
        
        matrix[y2 - 1][x2 - 2] = right_bottom
        result = min(result, matrix[y2 - 1][x2 - 2])
        
        answer.append(result)
    
    return answer