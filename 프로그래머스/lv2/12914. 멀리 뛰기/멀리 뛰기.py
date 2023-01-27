def solution(n):
    my_list = [1, 1]
    
    for _ in range(n - 1):
        my_list.append(my_list.pop(0) + my_list[-1])
        
    return my_list[-1] % 1234567