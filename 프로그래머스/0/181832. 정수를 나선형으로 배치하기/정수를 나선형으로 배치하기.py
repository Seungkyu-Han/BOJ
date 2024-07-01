def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    position = [0, 0]
    
    # right, down, left, up = 0, 1, 2, 3
    direction = 0
    limit = [n - 1, n - 1, 0, 1]
    
    for i in range(1, (n * n) + 1):
        answer[position[0]][position[1]] = i
        if direction == 0:
            if position[1] >= limit[0]:
                position = [position[0] + 1, position[1]]
                direction = 1
                limit[0] = limit[0] - 1
            else:
                position = [position[0], position[1] + 1]
        elif direction == 1:
            if position[0] >= limit[1]:
                position = [position[0], position[1] - 1]
                direction = 2
                limit[1] = limit[1] - 1
            else:
                position = [position[0] + 1, position[1]]
        elif direction == 2:
            if position[1] <= limit[2]:
                position = [position[0] - 1, position[1]]
                direction = 3
                limit[2] = limit[2] + 1
            else:
                position = [position[0], position[1] - 1]
        elif direction == 3:
            if position[0] <= limit[3]:
                position = [position[0], position[1] + 1]
                direction = 0
                limit[3] = limit[3] + 1
            else:
                position = [position[0] - 1, position[1]]
    
    return answer