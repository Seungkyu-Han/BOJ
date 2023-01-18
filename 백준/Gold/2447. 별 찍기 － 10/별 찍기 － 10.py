import sys
sys.setrecursionlimit(10**6)

def star(len):
    if len == 1:
        return ['*']
    Stars = star(len//3)
    L = []

    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(len//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline())
print('\n'.join(star(n)))