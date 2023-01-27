def solution(survey, choices):
    char_list = {"RT" : [0, 0], "CF" : [0, 0], "JM" : [0, 0], "AN" : [0, 0]}
    for idx, s in enumerate(survey):
        front = s[0]
        second = s[1]
        
        is_reverse = 0
        if s not in char_list.keys():
            is_reverse = 1
            s = s[::-1]
        
        if choices[idx] < 4: # 앞쪽 선택지
            char_list[s][is_reverse] += abs(choices[idx] - 4)
        else : # 중간 밑 뒷쪽 선택지
            char_list[s][~is_reverse] += abs(choices[idx] - 4)
    
    answer = ''
    for c in char_list:
        answer += c[char_list.get(c).index(max(char_list.get(c)))]
    return answer