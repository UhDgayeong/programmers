from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    list_dict = defaultdict(list)
    
    for r in records:
        time, num, io = r.split(" ")
        list_dict[num].append(time)
        
    list_dict = dict(sorted(list_dict.items()))
    
    for d in list_dict:
        max_idx = len(list_dict[d]) - 1
        fee = 0
        times = 0
        for idx, val in enumerate(list_dict[d]):
            if idx % 2 == 0: # in
                time = 0
                in_h, in_m = map(int, val.split(":"))
                if idx != max_idx: # out 기록 있는 in
                    out_h, out_m = map(int, list_dict[d][idx+1].split(":"))
                    time = (out_h * 60 + out_m) - (in_h * 60 + in_m)
                else: # out 기록 없는 in
                    time = 1439 - (in_h * 60 + in_m)
                times += time
                    
        if times <= fees[0]:
            fee += fees[1]
        else: # 기본 시간 초과
            fee += fees[1] + math.ceil((times - fees[0]) / fees[2]) * fees[3]
        
        answer.append(fee)
                           
    return answer