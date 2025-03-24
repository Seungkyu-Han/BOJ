import sys

N, K = map(int, sys.stdin.readline().split())

destination = sum([1 << i for i in range(N)])
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


distance_dict: list[dict[int, int]] = [dict() for _ in range(N)]
distance_dict[K][1 << K] = 0

def solve(cur_node: int, visited: int, spent_time: int):

    if visited == destination:
        distance_dict[cur_node][visited] = spent_time
        return spent_time

    result = float('inf')

    for index in range(N):
        next_visited = visited | 1 << index
        next_time = spent_time + graph[cur_node][index]

        if next_visited in distance_dict[index]:
            if distance_dict[index][next_visited] > next_time:
                distance_dict[index][next_visited] = next_time
                result = min(result, solve(index, next_visited, next_time))

        else:
            distance_dict[index][next_visited] = next_time
            result = min(result, solve(index, next_visited, next_time))

    return result

print(solve(K, 1 << K, 0))