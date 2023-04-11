def solution(order):
    answer = 0
    order = str(order)
    for o in order:
        if o == "3" or o == "6" or o == "9":
            answer += 1
    return answer