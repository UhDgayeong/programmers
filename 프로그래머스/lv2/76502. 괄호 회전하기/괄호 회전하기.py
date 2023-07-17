def solution(s):
    answer = 0
    
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(-1)
        elif char == ')':
            stack.append(1)
        elif char == '[':
            stack.append(-2)
        elif char == ']':
            stack.append(2)
        elif char == '{':
            stack.append(-3)
        else:
            stack.append(3)
            
    print(stack)
    for i in range(len(s)):
        arr = []
        for val in stack:
            if len(arr) > 0 and val > 0:
                if arr[-1] + val == 0:
                    arr.pop()
                else:
                    arr.append(val)
            else:
                arr.append(val)
        if len(arr) == 0:
            answer += 1
        front = stack[0]
        del stack[0]
        stack.append(front)
            
    
    
    return answer