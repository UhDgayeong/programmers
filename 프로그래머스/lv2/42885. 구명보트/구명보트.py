def solution(people, limit):
    people.sort()
    
    f_idx = 0
    e_idx = len(people) - 1
    cnt = 0
    
    while e_idx - f_idx > 0:
        if people[f_idx] + people[e_idx] <= limit:
            cnt += 1
            f_idx += 1
            e_idx -= 1
        else:
            e_idx -= 1
            
    return len(people) - cnt