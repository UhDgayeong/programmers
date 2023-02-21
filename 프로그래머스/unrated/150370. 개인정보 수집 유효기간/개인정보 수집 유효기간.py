def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    today_year, today_month, today_date = map(int, today.split("."))
    
    for t in terms:
        t, m = t.split(" ")
        terms_dict[t] = int(m)
        
    for idx, val in enumerate(privacies):
        d, t = val.split(" ")
        year, month, date = map(int, d.split("."))
        
        month += terms_dict[t]
        if month > 12:
            year += month // 12
            month = month % 12
            if month == 0:
                year -= 1
                month = 12
        
        if today_year < year:
            continue
        elif today_year == year:
            if today_month < month:
                continue
            elif today_month == month:
                if today_date >= date:
                    answer.append(idx + 1)
            else:
                answer.append(idx + 1)
        else:
            answer.append(idx + 1)
        
    return answer