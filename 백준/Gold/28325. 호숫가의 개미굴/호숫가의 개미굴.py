import sys

N = int(sys.stdin.readline())

C = list(map(int, sys.stdin.readline().split()))

visited = [False for _ in range(N)]

result = 0

for i in range(N):

    if C[i] > 0:
        result += C[i]
        continue

    left, right = i - 1 if i - 1 >= 0 else N - 1, i + 1 if i + 1 < N else 0

    if visited[left] or visited[right]:
        continue
    else:
        visited[i] = True
        result += 1

print(result)