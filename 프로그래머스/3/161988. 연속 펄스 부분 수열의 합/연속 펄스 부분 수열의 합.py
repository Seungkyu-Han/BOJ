def solution(sequence):
    
    pulse = []
    reverse_pulse = []
    
    is_even = True
    
    for element in sequence:
        if is_even:
            pulse.append(element)
            reverse_pulse.append(- element)
            is_even = False
        else:
            pulse.append(-element)
            reverse_pulse.append(element)
            is_even = True
            
    dp = -float('inf')
    reverse_dp = -float('inf')
    
    result = - float('inf')
    
    for i in range(len(sequence)):
        original = dp + pulse[i]
        if_start = pulse[i]
        reverse_original = reverse_dp + reverse_pulse[i]
        reverse_if_start = reverse_pulse[i]
        
        dp = max(original, if_start)
        reverse_dp = max(reverse_original, reverse_if_start)
        
        result = max(dp, reverse_dp, result)
    
            
    return result