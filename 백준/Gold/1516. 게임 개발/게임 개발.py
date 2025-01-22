import sys

N = int(sys.stdin.readline())

graph = dict()
time = dict()
dp = dict()

def find_time(node):

    if node in dp:
        return dp[node]

    cur_time = 0

    for next_node in graph[node]:
        cur_time = max(cur_time, find_time(next_node))
    result = cur_time + time[node]

    dp[node] = result

    return result

for i in range(N):
    cur_node = i + 1

    input_list = list(map(int, sys.stdin.readline().split()))

    time[cur_node] = input_list[0]

    graph[cur_node] = input_list[1:-1]


for i in range(1, N + 1):
    print(find_time(i))