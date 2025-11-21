def solution(s):
    answer = []
    last = {}
    
    for i, chr in enumerate(s):
        if chr in last:
            answer.append(i - last[chr])
            last[chr] = i
        else:
            answer.append(-1)
            last[chr] = i
    
    return answer