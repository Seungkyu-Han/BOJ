def solution(common):
    if common[0] + common[2] == common[1] * 2:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[2] // common[1])