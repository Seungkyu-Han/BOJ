def solution(n):
    
    answer = find_queens([], n)    
    
    return answer


def find_queens(cur_list, n):
    
    if len(cur_list) == n:
        return 1
    
    result = 0
    
    for i in range(n):
        if is_avaiable(cur_list, i):
            cur_list.append(i)
            result += find_queens(cur_list, n)
            cur_list.pop()
            
    return result
1, 3
2, 2
3, 1
def is_avaiable(cur_queens, cur_pos):
    
    cur_x, cur_y = len(cur_queens), cur_pos
    
    for x in range(len(cur_queens)):
        y = cur_queens[x]
        if (y == cur_pos) or (cur_y - y == cur_x - x) or (x + y == cur_x + cur_y):
            return False
        
    return True