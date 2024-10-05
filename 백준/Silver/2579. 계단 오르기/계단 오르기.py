# 계단은 한번에 한개 or 두개, 연속된 세개 계단은 안됨
# 마지막 계단은 무조건
# 위의 조건을 만족 시키는 점수의 최댓값

# 마지막 계단을 무조건 밟아야하니 마지막에서 시작?
# 마지막 + a(전칸) => 무조건 a의 전전칸
# 마지막 + b(전전칸) => b의 전칸 or b의 전전칸
# => b의 전칸을 고른 경우 => b의 전칸의 전전칸
# => b의 전전칸을 고른 경우 => b의 전전칸의 전칸 or b의 전전칸의 전전칸
# 두가지 경우의 수: 마지막 + 전칸 + 전전칸 or 마지막 + 전전칸 + (전전전칸 & 전전전전칸)


N = int(input())
stair = []
mx = [0] * 301

for i in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[0])
elif N == 2:
    print(stair[0] + stair[1])
else:
    mx[0] = stair [0]
    mx[1] = stair[0] + stair [1]
    mx[2] = max(stair[0]+stair[2], stair[1] + stair[2])
    
    for i in range(3,N):
        mx[i] = max(mx[i-3] + stair[i-1] + stair[i], mx[i-2] + stair[i])
        
    print(mx[N-1])