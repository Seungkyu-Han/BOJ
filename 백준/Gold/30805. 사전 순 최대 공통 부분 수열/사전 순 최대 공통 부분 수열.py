import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

result = []

while A and B:
    ab_set = set(A) & set(B)
    if not ab_set:
        break
    cur_max = max(ab_set)
    a_index = A.index(cur_max)
    b_index = B.index(cur_max)

    A = A[a_index + 1:]
    B = B[b_index + 1:]

    result.append(cur_max)

print(len(result))
if result:
    print(*result)