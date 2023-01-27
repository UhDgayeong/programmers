from collections import Counter

def solution(N, stages):
    cnt_dict = dict(Counter(stages))
    fail_dict = {}
    for i in range(N):
        if i+1 not in cnt_dict:
            fail_dict[i+1] = 0
        else:
            fail_dict[i+1] = cnt_dict[i + 1] /  sum(cnt_dict.values())
            del cnt_dict[i+1]
    
    sorted_dict = sorted(fail_dict.items(), key = lambda item: item[1], reverse = True)
    return [i[0] for i in sorted_dict]