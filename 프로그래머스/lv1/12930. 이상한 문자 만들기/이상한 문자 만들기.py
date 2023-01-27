def solution(s):
    str_list = s.split(' ')
    answer = []
    for l in str_list:
        tmp = []
        for i in range(len(l)):
            if i % 2 == 0:
                tmp.append(l[i].upper())
            else:
                tmp.append(l[i].lower())
        answer.append(''.join(tmp))
    return ' '.join(answer)