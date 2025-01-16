import heapq

def solution(n, roads, sources, destination):
    
    answer = []
    graph = {i + 1: [] for i in range(n)}
    
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [float('inf') for _ in range(n + 1)]
    visited[destination] = 0
    
    #count, node
    need_visit = []
    heapq.heappush(need_visit, [0, destination])
    
    while need_visit:
        
        cur_cnt, cur_node = heapq.heappop(need_visit)
        
        if cur_cnt > visited[cur_node]:
            continue
            
        for next_node in graph[cur_node]:
            if visited[next_node] > cur_cnt + 1:
                visited[next_node] = cur_cnt + 1
                heapq.heappush(need_visit, [cur_cnt + 1, next_node])
                
    for source in sources:
        answer.append(visited[source] if visited[source] != float('inf') else -1)
    
    return answer