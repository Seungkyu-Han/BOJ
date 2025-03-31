import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

operator = list(map(int, sys.stdin.readline().split()))

def back_tracking(cur_number, number_index) -> list[int]:
    
    if number_index >= N:
        return [cur_number, cur_number]
        
    min_result = float('inf')
    max_result = - float('inf')
    
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            if i == 0:
                result = back_tracking(cur_number + numbers[number_index], number_index + 1)
            elif i == 1:
                result = back_tracking(cur_number - numbers[number_index], number_index + 1)
            elif i == 2:
                result = back_tracking(cur_number * numbers[number_index], number_index + 1)
            else:
                next_result = abs(cur_number) // abs(numbers[number_index])
                if (cur_number > 0 and numbers[number_index] < 0):
                    next_result *= -1
                elif (cur_number < 0 and numbers[number_index] > 0):
                    next_result *= -1
                result = back_tracking(next_result, number_index + 1)
            min_result = min(min_result, result[1])
            max_result = max(max_result, result[0])
            operator[i] += 1
           
    
    return [max_result, min_result]
    
for result in back_tracking(numbers[0], 1):
    print(result)