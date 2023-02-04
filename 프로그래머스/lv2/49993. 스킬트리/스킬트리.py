def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        arr = [s for s in st if s in skill]
        string = ''.join(arr)
        if string == skill[:len(string)]:
            answer += 1
            
    return answer