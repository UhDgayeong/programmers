def solution(n):
    answer = 0
    my_arr = [i for i in range(1, n + 1) if i % 2 == 0]
    return sum(my_arr)