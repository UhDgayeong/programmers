def solution(word):
    key_dict = {0:781, 1:156, 2:31, 3:6, 4:1}
    val_dict = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    
    answer = len(word)
    for key, val in enumerate(word):
        answer += val_dict[val] * key_dict[key]
        
    return answer