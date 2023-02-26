def solution(babbling):
    answer = 0
    aywm = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        start = 0
        end = 1
        while end <= len(b):
            if b[start:end] not in aywm:
                if end - start > 3:
                    break
            else:
                start = end
                if end == len(b):
                    answer += 1
            end += 1
                
    return answer