import sys

N = int(sys.stdin.readline())

lines: list[list[int]] = []

for i in range(N):
    lines.append(list(map(int, sys.stdin.readline().split())))

lines.sort(key = lambda x: x[0])

total = lines[0][1] - lines[0][0]
cur_end = lines[0][1]

for start, end in lines[1:]:
    if start <= cur_end:
        if end <= cur_end:
            continue
        else:
            total += (end - cur_end)
            cur_end = end
    else:
        total += (end - start)
        cur_end = end
print(total)