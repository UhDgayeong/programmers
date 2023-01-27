def solution(arr1, arr2):
    answer = []
    arr2_col = len(arr2[0])

    for row in arr1:
        temp = []
        for _ in range(arr2_col):
            tmp = 0
            for idx, val in enumerate(row):
                tmp += (val * arr2[idx][_])
            temp.append(tmp)
        answer.append(temp)
    return answer