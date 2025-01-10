def solution(s):
    answer = 0
    
    for i in range(len(s)):
        stack = []
        
        for j in range(i, len(s)):
            if s[j] == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif s[j] == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            elif s[j] == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s[j])
            
        
        for j in range(i):
            if s[j] == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif s[j] == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            elif s[j] == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s[j])
        if len(stack) == 0:
            answer += 1
    
    return answer