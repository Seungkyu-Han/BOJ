def solution(plans):
    
    answer = []
    # name, spend_time
     
    plans.sort(key = lambda x: x[1])
    
    # t_p list
    tp = []
    
    for i in range(len(plans)):
        t, p, name = get_plan_element(plans[i])
        tp.append([t, p, name])
        
    print(tp)
        
    # rest_time, name
    stack = []
    
    for i in range(len(tp) - 1):
        cur_time = tp[i + 1][0] - tp[i][0]
        
        stack.append([tp[i][1], tp[i][2]])
        
        while stack and cur_time > 0:
            
            stack_rest_time, stack_name = stack.pop()
            
            if cur_time >= stack_rest_time:
                answer.append(stack_name)
                cur_time -= stack_rest_time
            else:
                stack.append([stack_rest_time - cur_time, stack_name])
                cur_time = 0
    stack.append([tp[-1][1], tp[-1][2]])
    
    while stack:
        
        stack_rest_time, stack_name = stack.pop()
        
        answer.append(stack_name)
    
    return answer


def get_plan_element(plan_element):
    hour, minute = map(int, plan_element[1].split(":"))
    plus_time = int(plan_element[2])
    
    return hour * 60 + minute, plus_time, plan_element[0]

