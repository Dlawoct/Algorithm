def solution(a, b):
    answer = 0
    max_num = max(a,b)
    min_num = min(a,b)
    
    return sum([i for i in range(min_num, max_num+1)])