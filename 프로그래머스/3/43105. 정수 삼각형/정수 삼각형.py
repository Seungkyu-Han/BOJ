def solution(triangle):
    answer = 0
    
    dp = [triangle[0][0]]
    
    for tri in range(1, len(triangle)):
        cur_dp = []
        for i in range(tri + 1):
            if i == 0:
                cur_dp.append(dp[0] + triangle[tri][i])
            elif i == tri:
                cur_dp.append(dp[-1] + triangle[tri][i])
            else:
                cur_dp.append(max(dp[i], dp[i - 1]) + triangle[tri][i])
        dp = cur_dp.copy()
                
    answer = max(dp)
    return answer