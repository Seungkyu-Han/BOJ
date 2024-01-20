import sys

first_word = list(sys.stdin.readline().strip())
second_word = list(sys.stdin.readline().strip())

max_length = max(len(first_word), len(second_word))

dp = [[0 for i in range(max_length + 1)] for t in range(max_length + 1)]

for i in range(len(first_word)):
    for t in range(len(second_word)):
        if first_word[i] == second_word[t]:
            dp[i][t] = dp[i-1][t-1] + 1
        else:
            dp[i][t] = max(dp[i][t-1], dp[i-1][t])


print(dp[len(first_word) - 1][len(second_word) - 1])