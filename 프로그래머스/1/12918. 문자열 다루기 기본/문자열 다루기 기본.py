def solution(s):
    answer = False
    if (len(s) == 4 or len(s) == 6):
        for i in s:
            if '0' <= i <= '9':
                answer = True
            else:
                return False
            
    return answer
    