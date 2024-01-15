import sys

N = int(sys.stdin.readline())

schedule_list = []

for i in range(N):
    T, P = map(int, sys.stdin.readline().split())
    schedule_list.append([T, P])


def consult(today, cur):
    if today == N:
        return cur
    elif today > N:
        return 0
    else:
        return max(consult(today + 1, cur), consult(today + schedule_list[today][0], cur + schedule_list[today][1]))


print(consult(0, 0))