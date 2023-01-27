def solution(arr1, arr2):
    answer = []
    for ar1, ar2 in zip(arr1, arr2):
        tmp = []
        for a1, a2 in zip(ar1, ar2):
            tmp.append(a1 + a2)
        answer.append(tmp)
    return answer