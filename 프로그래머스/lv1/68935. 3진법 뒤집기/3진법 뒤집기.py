def solution(n):
    r_list = []
    while n >= 3 :
        n, r = divmod(n, 3)
        r_list.append(str(r))
    r_list.append(str(n))

    return int(''.join(r_list), 3)