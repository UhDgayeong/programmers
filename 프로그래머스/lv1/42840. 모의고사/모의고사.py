def solution(answers):
    first_dict = {0:1, 1:2, 2:3, 3:4, 4:5}
    second_dict = {0:2, 1:1, 2:2, 3:3, 4:2, 5:4, 6:2, 7:5}
    third_dict = {0:3, 1:3, 2:1, 3:1, 4:2, 5:2, 6:4, 7:4, 8:5, 9:5}
            
    first_list = [1 for i in range(len(answers)) if answers[i] == first_dict[i%5]]
    second_list = [1 for i in range(len(answers)) if answers[i] == second_dict[i%8]]
    third_list = [1 for i in range(len(answers)) if answers[i] == third_dict[i%10]]
    
    cnt_list = list(map(sum, [first_list, second_list, third_list]))
    answer = [i+1 for i in range(len(cnt_list)) if cnt_list[i] == max(cnt_list)]

    return answer