def solution(edges):
    answer = []
    
    in_edge = dict()
    out_edge = dict()
    
    end_vertex = 1
    start_point = 0
    
    donut = 0
    stick = 0
    eight = 0
    
    for u, v in edges:
        if u not in out_edge:
            out_edge[u] = [v]
        else:
            out_edge[u].append(v)
        if v not in in_edge:
            in_edge[v] = [u]
        else:
            in_edge[v].append(u)
        end_vertex = max(end_vertex, u, v)
    
    for i in range(1, end_vertex + 1):
        if i not in in_edge and i in out_edge and len(out_edge[i]) > 1:
            start_point = i
            break
    
    for vertex in out_edge[start_point]:
        #detect type
        is_end = False
        
        cur_node = vertex
        while not is_end:
            
            if cur_node not in out_edge:
                stick += 1
                is_end = True
                break
            
            
            candidates = out_edge[cur_node]
            
            if len(candidates) > 1:
                eight += 1
                is_end = True
                break
                
            cur_node = candidates[0]
            
            if cur_node == vertex:
                donut += 1
                is_end = True
                break

    
    return [start_point, donut, stick, eight]