import sys

N = int(sys.stdin.readline())

sugar = [-1 for i in range(N + 3)]

sugar[3] = 1
sugar[4] = -1
sugar[5] = 1

for i in range(6, N+1):
    if sugar[i-3] == -1 and sugar[i-5] == -1:
        sugar[i] = -1

    elif sugar[i-3] == -1:
        sugar[i] = sugar[i-5] + 1

    elif sugar[i-5] == -1:
        sugar[i] = sugar[i-3] + 1

    else:
        sugar[i] = min(sugar[i-3], sugar[i-5]) + 1

print(sugar[N])