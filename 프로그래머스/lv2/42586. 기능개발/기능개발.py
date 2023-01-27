import math

def solution(progresses, speeds):
    if len(progresses) == 1:
        return [1]
    answer = []
    time = [math.ceil((100 - p) / s) for (p, s) in zip(progresses, speeds) ]
    print(time)
    
    cnt = 1
    top = time[0]
    for t in time[1:]:
        if top < t :
            top = t
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)  
    
    return answer