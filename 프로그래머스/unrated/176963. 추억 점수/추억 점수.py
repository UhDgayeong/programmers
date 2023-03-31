def solution(name, yearning, photo):
    answer = []
    name_dict = {}
    for idx, val in enumerate(name):
        name_dict[val] = yearning[idx]
    
    for ph in photo:
        cnt = 0
        for p in ph:
            if p in name_dict:
                cnt += name_dict[p]
        answer.append(cnt)

    return answer