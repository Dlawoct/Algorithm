def solution(a, b):
    answer = ''
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return days[(sum(month_day[:a-1]) + b - 1) % 7]

