def solution(n):
    answer = 0
    arr = [1, 2]
    
    for i in range(3, n + 1):
        tmp1 = arr[1]
        tmp2 = arr[0] + arr[1]
        arr[1] = tmp2
        arr[0] = tmp1
        
    return arr[1] % 1000000007