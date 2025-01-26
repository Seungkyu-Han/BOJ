import sys

N, M = map(int, sys.stdin.readline().split())

books = sorted(list(map(int, sys.stdin.readline().split())))

left, right = 0, N - 1
left_step = max(abs(books[left]), abs(books[right]))

result = 0

while left <= N - 1 and books[left] <= 0:

    if left > N - 1:
        break

    result += abs(books[left]) * 2

    for i in range(M):
        if left <= N - 1 and books[left] <= 0:
            left += 1
        else:
            break



while right >= 0 and books[right] >= 0:
    if right < 0:
        break

    result += abs(books[right]) * 2

    for i in range(M):
        if right >= 0 and books[right] >= 0:
            right -= 1
        else:
            break


print(result - left_step)