import sys

sys.setrecursionlimit(10 ** 6)

# 입력 처리
M, N = map(int, sys.stdin.readline().split())
down_stair = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# visited 배열: -1로 초기화하여 아직 계산되지 않았음을 표시
visited = [[-1 for _ in range(N)] for _ in range(M)]

# 상하좌우 방향 정의
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# DFS 함수
def dfs(x, y):
    # 이미 방문한 경우 값 반환 (메모이제이션)
    if visited[x][y] != -1:
        return visited[x][y]

    # 도착 지점에 도달한 경우
    if x == M - 1 and y == N - 1:
        return 1

    # 초기화
    visited[x][y] = 0

    # 가능한 방향으로 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and down_stair[x][y] > down_stair[nx][ny]:
            visited[x][y] += dfs(nx, ny)

    return visited[x][y]


# 시작점에서 탐색 시작
dfs(0, 0)

# 결과 출력
print(visited[0][0])
