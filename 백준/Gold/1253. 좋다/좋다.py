import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

result = 0


def isGood(goal):
    left, right = 0, N - 1

    while left < right:
        if A[left] + A[right] == A[goal]:
            if left == goal:
                left += 1
            elif right == goal:
                right -= 1
            else:
                return True
        elif A[left] + A[right] > A[goal]:
            right -= 1
        elif A[left] + A[right] < A[goal]:
            left += 1


for i in range(N):
    result += 1 if isGood(i) is True else 0

print(result)
