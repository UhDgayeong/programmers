from collections import Counter

def solution(priorities, location):
    answer = 1
    len_p = len(priorities)
    
    while True:
        print(priorities)
        if priorities[0] == max(priorities): # 맨 앞에 문서가 제일 큰 중요도 -> 출력 해당
            if location == 0: # 찾으려는 해당 문서이면
                break
            priorities.pop(0)
            answer += 1
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else: # 맨 앞에 문서가 제일 큰 중요도가 아님 -> 빼서 뒤로 넣음
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    
    return answer