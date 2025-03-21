def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    
    puddle_set = set()
    
    for cur_puddle_m, cur_puddle_n in puddles:
        puddle_set.add((cur_puddle_m, cur_puddle_n))
    
    for cur_m in range(m):
        for cur_n in range(n):
            for next_m, next_n in [[cur_m + 1, cur_n], [cur_m, cur_n + 1]]:
                if 0 <= next_m < m and 0 <= next_n < n and (next_m + 1, next_n + 1) not in puddle_set:
                    dp[next_n][next_m] = (dp[next_n][next_m] + dp[cur_n][cur_m]) % 1000000007
                    
    return dp[n - 1][m - 1]