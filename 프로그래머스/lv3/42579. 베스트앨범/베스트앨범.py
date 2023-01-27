from collections import defaultdict

def solution(genres, plays):
    answer = []
    g_dict = defaultdict(list)
    cnt_dict = defaultdict(int)
    
    for key, val in enumerate(genres):
        g_dict[val].append((plays[key], key))
        cnt_dict[val] += plays[key]
    
    g_dict = dict(g_dict)
    cnt_dict = sorted(cnt_dict.items(), key = lambda x: x[1], reverse = True)
    
    # 장르별 플레이 횟수 내림차순 정렬
    for g in g_dict:
        g_dict[g] = sorted(g_dict[g], key = lambda x : (-x[0], x[1]))

    for c in cnt_dict:
        for idx, val in enumerate(g_dict[c[0]]):
            answer.append(val[1])
            if idx == 1:
                break

    return answer