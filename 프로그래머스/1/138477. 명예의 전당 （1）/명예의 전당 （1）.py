def solution(k, score):
    answer = []
    honor = []
    
    first_len = min(k, len(score))
    
    for i in range(first_len):
        honor.append(score[i])
        honor.sort()
        answer.append(min(honor))
    
    for j in range(first_len, len(score)):
        honor.append(score[j])
        honor.sort()
        answer.append(honor[-k])
        
    return answer