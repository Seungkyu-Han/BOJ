import sys

K = int(sys.stdin.readline())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())

    graph = {i + 1: [] for i in range(V)}
    visited = {i + 1: 0 for i in range(V)}

    for _ in range(E):
        v1, v2 = map(int, sys.stdin.readline().split())

        graph[v1].append(v2)
        graph[v2].append(v1)

    flag = True

    for i in range(1, V + 1):
        if visited[i] != 0:
            continue
        need_visit = [i]
        visited[i] = 1

        while need_visit:

            cur_node = need_visit.pop()

            for next_node in graph[cur_node]:
                if visited[next_node] == visited[cur_node]:
                    flag = False
                    need_visit = []
                    break
                elif visited[next_node] == 0:
                    visited[next_node] = visited[cur_node] * -1
                    need_visit.append(next_node)

    print("YES" if flag else "NO")