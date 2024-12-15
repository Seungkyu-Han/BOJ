import sys

sys.setrecursionlimit(10**6)

N, R, Q = map(int, sys.stdin.readline().split())

graph = {i + 1: set() for i in range(N)}

for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].add(V)
    graph[V].add(U)

need_visit = [R]


while need_visit:

    cur_node = need_visit.pop()

    for next_node in graph[cur_node]:
        graph[next_node].remove(cur_node)
        need_visit.append(next_node)


dp = {i + 1: -1 for i in range(N)}


def find_child(def_node):

    if dp[def_node] != -1:
        return dp[def_node]

    if len(graph[def_node]) == 0:
        dp[def_node] = 1
        return 1

    result = 1

    for next_def_node in graph[def_node]:
        result += find_child(next_def_node)

    dp[def_node] = result

    return result

for _ in range(Q):
    q = int(sys.stdin.readline())

    print(find_child(q))