def solution(babbling):
    answer = 0
    for word in babbling:
        while word:
            if len(word) < 2:
                break
            elif len(word) >= 3:
                if word[0:3] == 'aya' or word[0:3] == 'woo':
                    word = word[3:]
                elif word[0:2] == 'ye' or word[0:2] == 'ma':
                    word = word[2:]
                else:
                    break
            else:
                if word[0:2] == 'ye' or word[0:2] == 'ma':
                    word = word[2:]
                else:
                    break

                
            
        if len(word) == 0:
            answer += 1
        print(word)
                
    return answer