def solution(order):
    cnt = 0
    assist = []
    i = 1
    
    while i != len(order) + 1:
        assist.append(i)
        while assist and assist[-1] == order[cnt]:
            assist.pop()
            cnt += 1
        
        i += 1
    
    return cnt