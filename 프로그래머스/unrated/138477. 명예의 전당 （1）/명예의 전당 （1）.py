def solution(k, score):
    hall = score[:k]
    min_hall = score[0]
    answer = []
    
    for s in score[:k]:
        if s <= min_hall:
            answer.append(s)
            min_hall = s
        else:
            answer.append(min_hall)
    
    for s in score[k:]:
        if s > min_hall:
            hall.remove(min_hall)
            hall.append(s)
            min_hall = min(hall)
        answer.append(min_hall)
            
    return answer