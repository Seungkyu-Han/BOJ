import sys

sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())

palindrome = list(map(int, sys.stdin.readline().split()))

dp = [[0 for i in range(N)] for t in range(N)]

for i in range(N):
    dp[i][i] = 2


def palindrome_dp(start, end):
    if dp[start][end] == 2 or start >= end:
        return 2
    elif dp[start][end] == 1:
        return 1
    elif palindrome[start] == palindrome[end]:
        dp[start][end] = palindrome_dp(start + 1, end - 1)
        return dp[start][end]
    else:
        return 1


M = int(sys.stdin.readline())

for i in range(M):
    S, E = map(int, sys.stdin.readline().split())

    print(1 if palindrome_dp(S-1, E-1) == 2 else 0)