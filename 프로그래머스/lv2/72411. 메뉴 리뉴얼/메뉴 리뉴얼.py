from itertools import combinations
from collections import defaultdict

def join_list(arr):
    return "".join(sorted(arr))

def solution(orders, course):
    answer = []
    my_dict = defaultdict(int)
    
    for order in orders:
        len_order = len(order)
        for i in course:
            if i > len_order:
                break
            combi = list(map(join_list, list(combinations(order, i))))
            for c in combi:
                my_dict[c] += 1
                
    my_dict = dict(my_dict)
    course_dict = defaultdict(list)
    
    for m in my_dict:
        if my_dict[m] >= 2:
            course_dict[len(m)].append(m)
            
    for cd in course_dict.items():
        max_cd = 0
        tmp_arr = []
        for c in cd[1]:
            if my_dict[c] == max_cd:
                tmp_arr.append(c)
            elif my_dict[c] > max_cd:
                max_cd = my_dict[c]
                tmp_arr = [c]
        answer.extend(tmp_arr)
    
    answer.sort()
    return answer