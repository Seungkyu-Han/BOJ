import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

S = int(sys.stdin.readline())

for i in range(N - 1):
    if S == 0:
        break

    max_value = max(A[i: i + S + 1])
    max_index = A.index(max_value)

    for j in range(max_index - 1, i - 1, -1):
        A[j], A[j + 1] = A[j + 1], A[j]
        S -= 1

print(*A)
