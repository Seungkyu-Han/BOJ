def solution(n):
    answer = 0
    
    if n % 2 == 1:
        return 0
    
    n //= 2
    
    dp = [0 for _ in range(5000 + 1)]
    
    dp[0] = 1
    
    for i in range(1, n + 1):
        cur = 0
        for j in range(0, i - 1):
            cur += dp[j] * 2
            
        dp[i] = (dp[i - 1] * 3 + cur) % 1_000_000_007

    
    return dp[n]