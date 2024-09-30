# 보물
# B의 최대값에 A의 최솟값을 곱해야 함
# B의 값을 0-N까지 인덱스 지정해서 이에 따라 A를 정렬하고 곱하기

S = 0
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#lambda 함수를 이용해 B의 크기 순대로 range(len(B))를 정렬해 b_idx 리스트 생성
B_idx = sorted(range(len(B)), key= lambda k : B[k])
A.sort(reverse = True)

A_sorted = [0] * N

#B의 인덱스에 따라 A를 정렬
for i in range(N):
    A_sorted[B_idx[i]] = A[i]

for k in range(N):
    S += A_sorted[k] * B[k]
    
print(S)