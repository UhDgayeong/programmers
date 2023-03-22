def solution(keymap, targets):
    answer = []
    k_dict = {}
    
    for km in keymap:
        for idx, val in enumerate(km):
            if val not in k_dict:
                k_dict[val] = idx + 1
            else:
                if k_dict[val] > idx + 1:
                    k_dict[val] = idx + 1
                    
    for tg in targets:
        tmp = 0
        break_point = False
        for t in tg:
            if t not in k_dict:
                answer.append(-1)
                break_point = True
                break
            else:
                tmp += k_dict[t]        
        
        if break_point != True :
            answer.append(tmp)
        break_point = False
        
    return answer