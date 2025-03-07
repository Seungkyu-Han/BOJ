import sys

N = int(sys.stdin.readline())

# 목표
P = list(map(int, sys.stdin.readline().split()))

# 섞이는 거
S = list(map(int, sys.stdin.readline().split()))

card = [i for i in range(N)]


def shake():

    result = [0 for _ in range(N)]

    for i in range(N):
        result[i] = S[card[i]]

    return result

cnt = 0

while True:

    flag = True

    for i in range(N):
        if card[i] % 3 != P[i]:
            flag = False
            break
    if flag:
        print(cnt)
        break

    flag = True

    for i in range(N):
        if card[i] != i:
            flag = False
            break

    if flag and cnt > 0:
        print(-1)
        break

    card = shake()
    cnt += 1