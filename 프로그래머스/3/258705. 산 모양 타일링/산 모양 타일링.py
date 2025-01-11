def solution(n, tops):
    answer = 0
    
    exist = [0 for _ in range(n)]
    not_exist = [0 for _ in range(n)]

    
    if tops[0] == 0:
        exist[0] = 3
        not_exist[0] = 2
    else:
        exist[0] = 4
        not_exist[0] = 3
    
    for i in range(n - 1):
        if tops[i + 1] == 0:
            exist[i + 1] = (exist[i] * 2 + not_exist[i]) % 10007
            not_exist[i + 1] = (exist[i] + not_exist[i]) % 10007
        else:
            exist[i + 1] = (exist[i] * 3 + not_exist[i]) % 10007
            not_exist[i + 1] = (exist[i] * 2 + not_exist[i]) % 10007
            
    answer = exist[-1]
    
    return answer