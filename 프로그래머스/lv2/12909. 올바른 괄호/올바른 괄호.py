def solution(s):  
    check = 0
    for a in s:
        if a == '(':
            check += 1
        else: #')'
            check -= 1
            if check == -1:
                return False
        
    if check > 0:
        return False
    return True