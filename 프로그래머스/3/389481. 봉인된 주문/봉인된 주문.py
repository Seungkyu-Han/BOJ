def solution(n, bans):
    answer = ''
    
    bans.sort(key = lambda x: (len(x), x))
    cur_sequence = find_sequence(n)    
    
    for ban in bans:
        ban_sequence = find_ban_sequence(ban)
        if is_front_big(cur_sequence, ban_sequence):
            increase_sequence(cur_sequence)
            
    for ch in reversed(cur_sequence):
        if ch > -1:
            answer = chr(ch + ord('a')) + answer
        else:
            break
    
    return answer


def find_ban_sequence(ban):
    sequence = [-1 for _ in range(11)]
    cnt = 10
    
    for ch in reversed(ban):
        sequence[cnt] = ord(ch) - ord('a')
        cnt -= 1
        
    return sequence

def find_sequence(n):
    sequence = [-1 for _ in range(11)]
    
    cnt = 10
    
    while n > 0:
        n -= 1
        sequence[cnt] = n % 26
        
        n //= 26
        cnt -= 1
    
    return sequence

def is_front_big(front, back):
    
    for i in range(11):
        if front[i] > back[i]:
            return True
        elif front[i] < back[i]:
            return False
    
    return True

def increase_sequence(sequence):
    
    sequence[-1] += 1
    
    for i in range(10, 0, -1):
        if sequence[i] > 25:
            sequence[i] = 0
            sequence[i - 1] += 1
        else:
            break