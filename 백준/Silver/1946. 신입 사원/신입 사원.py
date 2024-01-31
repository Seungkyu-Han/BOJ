import sys

for i in range(int(sys.stdin.readline().strip())):
    candidate = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))])
    top = 0
    result = 1

    for t in range(1, len(candidate)):
        if candidate[t][1] < candidate[top][1]:
            top = t
            result += 1

    print(result)