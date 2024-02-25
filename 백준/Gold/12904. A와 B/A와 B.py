import sys

S = list(sys.stdin.readline().strip())
T = list(sys.stdin.readline().strip())

while len(T) > len(S):
    if T[-1] == 'A':
        T.pop(-1)
    else:
        T.pop(-1)
        T.reverse()

print(1 if S == T else 0)