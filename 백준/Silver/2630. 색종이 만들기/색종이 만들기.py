import sys

N = int(sys.stdin.readline().strip())

paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]


def cut_paper(cur_n, cur_x, cur_y):
    if cur_n == 1:
        if paper[cur_y][cur_x] == 0:
            # 하얀색 -1
            return [1, 0]
        else:
            # 파란색 -2
            return [0, 1]

    length = cur_n // 2

    a = cut_paper(length, cur_x, cur_y)
    b = cut_paper(length, cur_x, cur_y + length)
    c = cut_paper(length, cur_x + length, cur_y)
    d = cut_paper(length, cur_x + length, cur_y + length)

    if a == [1, 0] and b == [1, 0] and c == [1, 0] and d == [1, 0]:
        return [1, 0]
    elif a == [0, 1] and b == [0, 1] and c == [0, 1] and d == [0, 1]:
        return [0, 1]
    else:
        return [a[0] + b[0] + c[0] + d[0], a[1] + b[1] + c[1] + d[1]]

result = cut_paper(N, 0, 0)

print(result[0])
print(result[1])