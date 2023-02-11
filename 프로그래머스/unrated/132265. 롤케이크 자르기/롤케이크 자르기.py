from collections import Counter

def solution(topping):
    answer = 0
    counter_topping = dict(Counter(topping))
    chulsoo = set(topping)
    brother = set()
    
    for i in range(0, len(topping) - 1):
        end = topping.pop()
        brother.add(end)
        counter_topping[end] -= 1
        
        if counter_topping[end] == 0:
            chulsoo.remove(end)
        
        if len(chulsoo) == len(brother):
            answer += 1
                
    return answer