def solution(n, s, a, b, fares):
    answer = 0
    
    graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    
    for u, v, weight in fares:
        graph[u][v] = weight
        graph[v][u] = weight
        
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    
    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                graph[start][end] = min(graph[start][end], 
                                        graph[start][mid] + graph[mid][end])
                
    result = float('inf')
    
    
    for i in range(1, n + 1):
        result = min(result, 
                    graph[s][i] + graph[i][a] + graph[i][b])
    
    return result