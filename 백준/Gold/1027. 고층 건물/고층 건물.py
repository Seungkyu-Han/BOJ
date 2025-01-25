import sys

# grad, y point
def get_grad(x1, y1, x2, y2):
    if y1 == y2:
        return 0
    else:
        return (y2 - y1) / (x2 - x1)

def get_equation(x1, y1, x2, y2):
    if y1 == y2:
        grad = 0
    else:
        grad = (y2 - y1) / (x2 - x1)

    y_point = y1 - grad * x1

    return grad, y_point


def get_height(grad, y_point, x):
    return grad * x + y_point


N = int(sys.stdin.readline())

heights = list(map(int, sys.stdin.readline().split()))


result = 0

for i in range(N):
    #left
    cur = 0
    cur_x1, cur_y1 = i, heights[i]
    cur_left = float('inf')
    for j in range(i - 1, -1, -1):
        cur_x2, cur_y2 = j, heights[j]
        cur_grad = get_grad(cur_x1, cur_y1, cur_x2, cur_y2)

        if cur_grad < cur_left:
            cur += 1
            cur_left = cur_grad

    #right
    cur_right =  - float('inf')
    for j in range(i + 1, N):
        cur_x2, cur_y2 = j, heights[j]
        cur_grad = get_grad(cur_x1, cur_y1, cur_x2, cur_y2)

        if cur_grad > cur_right:
            cur += 1
            cur_right = cur_grad

    result = max(result, cur)


print(result)