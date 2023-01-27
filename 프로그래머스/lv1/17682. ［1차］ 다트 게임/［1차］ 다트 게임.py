def solution(dartResult):
    answer = []
    idxList = [i for i in range(len(dartResult)) if dartResult[i].isdigit() and not dartResult[i-1].isdigit()]
    dartList = []
    
    for i in range(len(idxList) - 1):
        dartList.append(dartResult[idxList[i]:idxList[i+1]])
    dartList.append(dartResult[idxList[-1]:])
    
    for d in dartList:
        if d[1].isdigit(): # 10점인 경우
            point = int(d[0:2])
        else: # 0 ~ 9점인 경우
            point = int(d[0])
        
        square = 1
        if 'D' in d:
            square = 2
        elif 'T' in d:
            square = 3
            
        if '*' in d:
            answer[-1:] *= 2
            answer.append(point ** square * 2)
        elif '#' in d:
            answer.append((point ** square) * (-1))
        else:
            answer.append(point ** square)

    return sum(answer)