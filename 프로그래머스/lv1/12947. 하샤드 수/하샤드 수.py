def solution(x):
    x_list = [int(i) for i in str(x)]
    return x % sum(x_list) == 0