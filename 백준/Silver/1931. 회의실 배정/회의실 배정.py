import sys

meeting = sorted([list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline().strip()))],
                 key=lambda x: (x[1], x[0]))

time = 0
result = 0

while meeting:
    start_time, end_time = meeting.pop(0)
    if start_time >= time and end_time < 2 ** 31:
        time = end_time
        result += 1

print(result)
