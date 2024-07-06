import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
reversed_A = list(reversed(A))

count, reversed_count = 0, 1

for i in range(N):
    for t in range(i + 1, N):
        if A[i] > A[t]:
            A[i], A[t] = A[t], A[i]
            count += 1
        if reversed_A[i] > reversed_A[t]:
            reversed_A[i], reversed_A[t] = reversed_A[t], reversed_A[i]
            reversed_count += 1


print(min(count, reversed_count))