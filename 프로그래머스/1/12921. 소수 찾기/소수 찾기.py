import math
def solution(n):
    answer = 0

    for num in range(2, n+1): #2, 3, 4, 5
        is_true = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                is_true = False
                break
                
        if is_true:
            answer += 1
            
    return answer