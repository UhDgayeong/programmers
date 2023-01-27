def solution(n, lost, reserve):
    stu_list = [1] * (n + 2)
    reserve.sort()
    
    for r in reserve[:]:
        if r in lost[:]:
            reserve.remove(r)
            lost.remove(r)
            
    for i in lost:
        stu_list[i] = 0

    for r in reserve:
        if stu_list[r-1] == 0:
            stu_list[r-1] = 1
            continue
        elif stu_list[r+1] == 0:
            stu_list[r+1] = 1
    
    answer = len([i for i in stu_list if i == 1]) - 2
    return answer