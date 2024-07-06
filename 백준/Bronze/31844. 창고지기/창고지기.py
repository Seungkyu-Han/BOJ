stock = list(input())

robot_index = stock.index('@')
box_index = stock.index('#')
target_index = stock.index('!')

is_line = False

if robot_index < box_index < target_index or target_index < box_index < robot_index:
    print(abs(target_index - robot_index) - 1)
else:
    print(-1)