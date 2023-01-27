import itertools

def solution(k, dungeons):
    answer_list = []
    dungeons = [tuple(d) for d in dungeons] #리스트를 튜플로 변경
    permutation = set(list(itertools.permutations(dungeons, len(dungeons)))) # 중복 조합 제거한 순열
    len_dungeons = len(dungeons)
    
    for p in permutation:
        answer = 0
        fatig = k
        
        for min_fatig, need_fatig in p:
            if fatig >= min_fatig:
                fatig -= need_fatig
                answer += 1
                
        if answer == len_dungeons: # 모든 던전 탐험이 가능한 경우
            return answer
        
        answer_list.append(answer)
        
    return max(answer_list)