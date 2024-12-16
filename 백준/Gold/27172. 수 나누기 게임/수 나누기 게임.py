import sys

N = int(sys.stdin.readline())

card = list(map(int, sys.stdin.readline().split()))
s = set(card)
m = max(card)

game = [0 for _ in range(m + 1)]

for i in card:
    if i != m:
        for j in range(2 * i, m + 1, i):
            if j in s:
                game[i] += 1
                game[j] -= 1

for i in card:
    print(game[i], end = ' ')