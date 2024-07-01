def solution(dots):
    for i in range(4):
        for t in range(4):
            if i == t:
                continue
            for k in range(4):
                if k == t or k == i:
                    continue
                j = 6 - i - t - k
                line1 = (dots[i][1] - dots[t][1]) / (dots[i][0] - dots[t][0])
                line2 = (dots[k][1] - dots[j][1]) / (dots[k][0] - dots[j][0])
                if line1 == line2:
                    return 1
    return 0