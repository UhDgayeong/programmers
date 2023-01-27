def solution(a, b):
    days_dict = {1:30, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days = b if a != 1 else b - 1
    for m in range(1, a):
        days += days_dict[m]
    
    return day_list[days % 7]