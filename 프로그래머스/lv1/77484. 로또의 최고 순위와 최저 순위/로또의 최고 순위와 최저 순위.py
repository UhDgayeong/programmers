def solution(lottos, win_nums):
    rank_dict = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    cnt = len([n for n in lottos if n in win_nums])
    zero_cnt = len([n for n in lottos if n == 0])
    return list((rank_dict[cnt+zero_cnt], rank_dict[cnt]))