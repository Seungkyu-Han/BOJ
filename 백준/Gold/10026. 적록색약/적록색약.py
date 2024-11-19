import sys

N = int(sys.stdin.readline())

graph = [list(sys.stdin.readline().strip()) for _ in range(N)]

type1_visited = [[False for _ in range(N)] for _ in range(N)]
type2_visited = [[False for _ in range(N)] for _ in range(N)]



type1_result = 0
type2_result = 0

for i in range(N):
    for j in range(N):
        if not type1_visited[i][j]:

            type1_result += 1

            type1_need_visit = [[i, j]]

            target1 = graph[i][j]

            while type1_need_visit:

                cur_i, cur_j = type1_need_visit.pop()

                for next_i, next_j in [[cur_i - 1, cur_j], [cur_i + 1, cur_j], [cur_i, cur_j - 1], [cur_i, cur_j + 1]]:
                    if 0 <= next_i < N and 0 <= next_j < N and not type1_visited[next_i][next_j]:
                        if graph[next_i][next_j] == target1:
                            type1_visited[next_i][next_j] = True
                            type1_need_visit.append([next_i, next_j])


        if not type2_visited[i][j]:

            type2_result += 1

            type2_need_visit = [[i, j]]

            target2 = graph[i][j]

            while type2_need_visit:
                cur_i, cur_j = type2_need_visit.pop()

                for next_i, next_j in [[cur_i - 1, cur_j], [cur_i + 1, cur_j], [cur_i, cur_j - 1], [cur_i, cur_j + 1]]:
                    if 0 <= next_i < N and 0 <= next_j < N and not type2_visited[next_i][next_j]:
                        if graph[next_i][next_j] == target2 or\
                            (graph[next_i][next_j] == 'R' and target2 == 'G') or \
                                (graph[next_i][next_j] == 'G' and target2 == 'R'):
                            type2_visited[next_i][next_j] = True
                            type2_need_visit.append([next_i, next_j])

print(f'{type1_result} {type2_result}')