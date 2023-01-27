def solution(clothes):
    clothes_dict = {}
    answer = 1
    
    for c in clothes:
        try:
            if clothes_dict[c[1]]:
                clothes_dict[c[1]] += 1
        except:
            clothes_dict[c[1]] = 1

    for i in clothes_dict.values():
        answer *= i + 1
        
    return answer - 1