def solution(s):
    arr = []
    
    for i in s:
        if i in arr[-1:]:
            arr.pop()
        else:
            arr.append(i)   

    return 1 if len(arr) == 0 else 0