def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        my_list = [array[n] for n in range(i-1, j)]
        my_list.sort()
        answer.append(my_list[k-1])
    
    return answer