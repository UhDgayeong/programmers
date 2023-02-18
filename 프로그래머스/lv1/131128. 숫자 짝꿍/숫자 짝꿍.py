from collections import Counter

def solution(X, Y):
    x_cnt = dict(Counter(X))
    y_cnt = dict(Counter(Y))
    arr = []
    for item in x_cnt:
        if item in y_cnt:
            tmp = x_cnt[item] if x_cnt[item] < y_cnt[item] else y_cnt[item]
            arr.extend([item] * tmp)
    
    if not arr:
        return '-1'
    arr_cnt = dict(Counter(arr))
    if len(arr_cnt) == 1 and '0' in arr_cnt:
        return '0'
    
    arr.sort(reverse = True)
    answer = ''.join(arr)
    return answer