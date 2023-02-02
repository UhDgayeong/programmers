def solution(s):
    answer = []
    s_list = []
    
    num = ''
    tmp_list = []
    for a in s[:-1]:
        if a != '{':
            if a != '}' and a != ',': # 숫자인 경우
                num += a
            else: # }이나 ,인 경우
                if num != '':
                    tmp_list.append(int(num))
                if a == '}': # }인 경우
                    s_list.append(tmp_list)
                    tmp_list = []
                num = ''

    s_list = sorted(s_list, key = lambda x : len(x))
    
    for s in s_list:
        for i in s:
            if i not in answer:
                answer.append(i)
            
    return answer

