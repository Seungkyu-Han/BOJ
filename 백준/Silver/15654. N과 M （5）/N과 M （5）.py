import sys

N, M = map(int, sys.stdin.readline().split())

candidate = list(map(int, sys.stdin.readline().split()))

candidate.sort()

def back_tracking(cur_numbers, n, m, visited):

    if len(cur_numbers) == m:
        print(*cur_numbers)
        return

    for index in range(0, n):
        if visited[index]:
            continue
        cur_numbers.append(candidate[index])
        visited[index] = True
        back_tracking(cur_numbers, n, m, visited)
        cur_numbers.pop()
        visited[index] = False

back_tracking([], N, M, [False for _ in range(N)])