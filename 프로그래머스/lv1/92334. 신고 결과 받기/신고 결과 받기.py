def solution(id_list, report, k):
    report_cnt_dict = {}
    reporter_dict = {}
    mail_cnt = {}
    
    for i in id_list:
        report_cnt_dict[i] = 0
        reporter_dict[i] = []
        mail_cnt[i] = 0
    
    for r in report:
        reporter, reported = r.split()
        if reporter in reporter_dict[reported]:
            continue
        reporter_dict[reported].append(reporter)
        report_cnt_dict[reported] += 1
        
    for user in id_list:
        if report_cnt_dict[user] >= k:
            for reporter in reporter_dict[user]:
                mail_cnt[reporter] += 1
    
    answer = list(mail_cnt.values())
    return answer