def solution(numbers):
    answer = []
    
    for num in numbers:
        result = 0
        
        bin_arr = []
        
        while num > 0:
            bin_arr.append(num % 2)
            num //= 2
            
        index = -1
        
        for i in range(len(bin_arr)):
            if bin_arr[i] == 0:
                index = i
                break
        if len(bin_arr) == 0:
            result = 1
        
        elif index == -1:
            bin_arr[-1] = 0
            bin_arr.append(1)
            for i in range(len(bin_arr)):
                result += (bin_arr[i] * (2 ** i))
            
        else:
            bin_arr[i] = 1
            if i > 0:
                bin_arr[i - 1] = 0
            for i in range(len(bin_arr)):
                result += (bin_arr[i] * (2 ** i))
        
        answer.append(result)
        
    
    return answer