# 깊이 탐색? 경우의 수 증가, 모든 값 연산
# 계단오르기 같이 뒤에서 부터 누적하기

N = int(input())
Triangle = []

for i in range(N):
    # [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    Triangle.append(list(map(int, input().split())))

for j in range(N-1, 0, -1): # 4, 3, 2, 1 
    for k in range(j): # k == 4) 0, 1, 2, 3
        Triangle[j-1][k] += max(Triangle[j][k], Triangle[j][k+1])
        
print(Triangle[0][0])
