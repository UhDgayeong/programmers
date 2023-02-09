def solution(babbling):
    answer = 0
    dup_arr = ["ayaaya", "yeye", "woowoo", "mama"]
    continuer = False
    
    for b in babbling:
        for d in dup_arr:
            if d in b:
                continuer = True
        
        if continuer == True:
            continuer = False
            continue
            
        b = b.replace("aya", " ")
        b = b.replace("ye", " ")
        b = b.replace("woo", " ")
        b = b.replace("ma", " ")
        b = b.replace(" ", "")
        
        if b == "":
            answer += 1
            
    return answer