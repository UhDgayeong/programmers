def solution(n):
    ans = 1
    
    while n > 1:
        q, r = divmod(n, 2)
        
        if r == 1 and n != 1:
            ans += 1
        if format(q, 'b').count('1') == 1:
            break
        n = q

    return ans