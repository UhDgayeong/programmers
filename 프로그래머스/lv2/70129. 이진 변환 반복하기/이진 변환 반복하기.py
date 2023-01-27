def solution(s):
    cnt = 0
    zero_cnt = 0
    while s != '1':
        cnt += 1
        new_bin = len([i for i in s if i == '1'])
        zero_cnt += len(s) - new_bin
        s = format(new_bin, 'b')

    return cnt, zero_cnt