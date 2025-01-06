import sys

step = list(map(int, sys.stdin.readline().split()))

dp = [[float('inf') for i in range(25)]]

dp[0][0] = 0


def next_step(cur_pos, next_pos):
    if cur_pos == next_pos:
        return 1
    elif cur_pos == 0:
        return 2
    elif abs(cur_pos - next_pos) % 2 == 1:
        return 3
    else:
        return 4


for cur_step in step[:-1]:
    cur_dp = [float('inf') for i in range(25)]

    for left in range(5):
        for right in range(5):
            left_move = cur_step * 5 + right
            right_move = left * 5 + cur_step

            cur_dp[left_move] = min(cur_dp[left_move], dp[-1][left * 5 + right] + next_step(left, cur_step))
            cur_dp[right_move] = min(cur_dp[right_move], dp[-1][left * 5 + right] + next_step(right, cur_step))

    dp.append(cur_dp)


result = float('inf')

for i in range(25):
    result = min(result, dp[-1][i])

print(result)