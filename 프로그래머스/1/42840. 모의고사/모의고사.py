def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_cnt = 0
    two_cnt = 0
    three_cnt = 0
    
    if answers[0] == one[0]:
        one_cnt += 1
    if answers[0] == two[0]:
        two_cnt += 1
    if answers[0] == three[0]:
        three_cnt += 1
    
    for n in range(1, len(answers)):
        if answers[n] == one[n%5]:
            one_cnt += 1
        if answers[n] == two[n%8]:
            two_cnt += 1 
        if answers[n] == three[n%10]:
            three_cnt += 1
    
    max_cnt = max(one_cnt, two_cnt)
    max_cnt = max(max_cnt, three_cnt)
    
    if max_cnt == one_cnt == two_cnt == three_cnt:
        return [1,2,3]
    elif max_cnt == one_cnt == two_cnt:
        return [1,2]
    elif max_cnt == one_cnt == three_cnt:
        return [1,3]
    elif max_cnt == two_cnt == three_cnt:
        return [2,3]
    elif max_cnt == one_cnt:
        return [1]
    elif max_cnt == two_cnt:
        return [2]
    elif max_cnt == three_cnt:
        return [3]
        
# 1, 2, 3, 12, 13, 23, 123
