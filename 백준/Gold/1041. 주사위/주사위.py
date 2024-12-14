import sys

N = int(sys.stdin.readline())

dice = list(map(int, sys.stdin.readline().split()))
sorted_dice = sorted(dice)

if N == 1:
    print(sum(sorted_dice[:5]))
else:
    face = ((N - 2) ** 2) * sorted_dice[0] * 5

    corner = float('inf')

    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5

    for index1, index2 in [[A, B], [A, C], [A, D], [A, E], [B, C], [B, D], [B, F], [C, E], [C, F], [D, E], [D, F], [E, F]]:
        small_corner = min(dice[index1], dice[index2])
        big_corner = max(dice[index1], dice[index2])
        corner = min(corner, (small_corner * 12 + big_corner * 8) * (N - 2))


    vertex = float('inf')

    for index1, index2, index3 in [[A, B, C], [A, B, D], [A, C, E], [A, D, E], [B, C, F], [B, D, F], [C, E, F], [D, E, F]]:
        vertex1 = dice[index1]
        vertex2 = dice[index2]
        vertex3 = dice[index3]
        small_vertex = min(vertex1, vertex2, vertex3)
        big_vertex = max(vertex1, vertex2, vertex3)
        middle_vertex = (vertex1 + vertex2 + vertex3) - small_vertex - big_vertex


        cur_vertex = (small_vertex * 8 + middle_vertex * 8 + big_vertex * 4)

        if vertex > cur_vertex:
            vertex = cur_vertex

    print(face + corner + vertex)