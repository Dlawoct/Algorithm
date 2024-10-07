# n = 1 은 1개
# n = 2 는 3개
# n = 3 은 5개 
# n = 4 부터 이전것들 이용

N = int(input())
number = [0] * 1001
# n3 = n1 * 2 + n2
# n4 = n2 * 2 + n3  
number[1] = 1
number[2] = 3
    
for i in range(3,N+1):
    number[i] = 2 * number[i-2] + number[i-1]

print(number[N] % 10007)
