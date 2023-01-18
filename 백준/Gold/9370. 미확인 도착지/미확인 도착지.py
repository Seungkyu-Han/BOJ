import heapq
import sys

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    dp = [100000000 for i in range(n + 1)]
    dp[start] = 0
    while heap:

        we, nu = heapq.heappop(heap)

        if dp[nu] < we:
            continue

        for ne, nw in s[nu]:
            wei = we + nw
            if dp[ne] > wei:
                dp[ne] = wei
                heapq.heappush(heap, [wei, ne])
    return dp


t = int(sys.stdin.readline())
for _ in range(t):
    n, m, c = map(int, sys.stdin.readline().split())
    start, g, h = map(int, sys.stdin.readline().split())
    s = [[] for i in range(n + 1)]
    de = []
    for j in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        s[a].append([b, d])
        s[b].append([a, d])
    for k in range(c):
        de.append(int(sys.stdin.readline()))
    start_ = dijkstra(start)
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    ans = []
    for l in de:
        if start_[g] + g_[h] + h_[l] == start_[l] or start_[h] + h_[g] + g_[l] == start_[l]:
            ans.append(l)
    ans.sort()
    print(*ans)