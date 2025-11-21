import math
def solution(number, limit, power):
    answer = []
    for n in range(1,number+1):
        cnt = 0
        
        for i in range(1,int(math.sqrt(n)+1)):
            if n % i == 0:
                cnt += 1
                if i ** 2 != n:
                    cnt += 1  
        if cnt > limit:
            cnt = power
            
        answer.append(cnt)
        
    return sum(answer)

# 기사단은 1~number
# 자기 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매
# 제한수치가 있어, 제한수치보다 큰 공격력을 가진 무기 사려면 협약 기관에서 정한 무기 사야함
# 1부터 number까지 각 약수의 갯수를 구하고, 넘으면 power로 치환 and Sum 후 반환
