import sys

M, N = map(int, sys.stdin.readline().split())

pokemon = [sys.stdin.readline().strip() for _ in range(M)]

for _ in range(N):
    question = sys.stdin.readline().rstrip()
    if question.isnumeric():
        print(pokemon[int(question) - 1])
    else:
        print(pokemon.index(question) + 1)