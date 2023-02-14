def solution(ingredient):
    answer = 0
    arr = []
    for i in ingredient:
        if i == 1 and len(arr) >= 3:
            if arr[-1] == 3 and arr[-2] == 2 and arr[-3] == 1:
                for _ in range(3):
                    arr.pop()
                answer += 1
                continue
            
        arr.append(i)
    return answer