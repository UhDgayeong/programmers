def rule_check(c):
    if c.islower():
        return c
    elif c.isdigit():
        return c
    elif c == '-' or c == '_' or c == '.':
        return c
    else:
        return ''

def solution(new_id):
    new_id = new_id.lower() #1단계
    id_list = list(filter(rule_check, new_id)) #2단계
    for i in range(len(id_list) - 1): #3단계
        if id_list[i] == '.' and id_list[i+1] == '.':
            id_list[i] = ''
            
    id_str = ''.join(id_list)
    if id_str[0] == '.': #4단계
        id_str = id_str[1:]
    if id_str[-1:] == '.':
        id_str = id_str[:-1]
        
    if id_str == '': #5단계
        id_str = 'a'
        
    if len(id_str) >= 16: #6단계
        id_str = id_str[0:15]
        if id_str[-1] == '.':
            id_str = id_str[0:14]
    if len(id_str) <= 2: #7단계
        while len(id_str) < 3:
            id_str = id_str + id_str[-1]
    
    return id_str