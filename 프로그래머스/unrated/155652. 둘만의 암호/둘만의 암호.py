def solution(s, skip, index):
    answer = ''
    
    for a in s:
        cnt = 0
        a = ord(a)
        while cnt < index:
            a += 1
            if a > 122:
                a -= 26
            if chr(a) not in skip:
                cnt += 1
        answer += chr(a)
        
    return answer