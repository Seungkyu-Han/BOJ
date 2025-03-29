import sys


N, M = map(int, sys.stdin.readline().split())

start = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

end = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]


def solve():

    if N < 3 or M < 3:
        for i in range(N):
            for j in range(M):
                if start[i][j] != end[i][j]:
                    return -1
        return 0
    result = 0
    for i in range(N):
        for j in range(M):
            if i > N - 3 or j > M - 3:
                if start[i][j]!= end[i][j]:
                    return -1
            
            elif start[i][j] != end[i][j]:
                result += 1
                for next_i in range(3):
                    for next_j in range(3):
                        if i + next_i < N and j + next_j < M:
                            start[i + next_i][j + next_j] = 1 if start[i + next_i][j + next_j] == 0 else 0
                        
    return result

print(solve())
