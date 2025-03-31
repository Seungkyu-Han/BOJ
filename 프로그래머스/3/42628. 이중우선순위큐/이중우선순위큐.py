import heapq

def solution(operations):
    
    answer = 0
    
    value_dict = dict()
    min_heap = []
    max_heap = []
    
    for operation in operations:
        command, value = operation.split()
        if command == 'I':
            value = int(value)
            
            if value in value_dict:
                value_dict[value] += 1
            else:
                value_dict[value] = 1
            
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
        else:
            if value == '1' and max_heap:
                cur_value = heapq.heappop(max_heap) * -1
                
                while max_heap and value_dict[cur_value] == 0:
                    cur_value = heapq.heappop(max_heap) * -1
                
                if value_dict[cur_value] > 0:
                    value_dict[cur_value] -= 1
            elif value == '-1' and min_heap:
                cur_value = heapq.heappop(min_heap)
                
                while min_heap and value_dict[cur_value] == 0:
                    cur_value = heapq.heappop(min_heap)
                
                if value_dict[cur_value] > 0:
                    value_dict[cur_value] -= 1
    min_value = float('inf')
    max_value = -float('inf')
    
    for key in value_dict.keys():
        if value_dict[key] > 0:
            min_value = min(min_value, key)
            max_value = max(max_value, key)
    
    if min_value == float('inf') and max_value == -float('inf'):
        return [0, 0]
    else:
        return [max_value, min_value]