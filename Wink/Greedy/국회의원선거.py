# 다솜이의 득표와 다른 모든 사람들의 득표를 비교한다
# 다솜이 보다 크거나 같은 득표 수가 있으면 하나씩 빼고 더한다
# 만약 나머지 모든 득표가 다솜이 보다 작으면 종료한다

# 시간 초과
# N = int(input())
# all = [0] * N
# sum = 0

# for j in range(N):
#     all[j] = int(input())
    
# while True:
#     for i in range(1,N):
#         if N == 1:
#             sum = 0
#             break
#         elif all[0] > all[i]:
#             break
#         elif all[0] <= all[i]:
#             all[0] += 1
#             all[i] -= 1
#             sum += 1
#     if all[0] > max(all[1:]):
#         break
# print(sum)

# 우선 순위 큐로 구현, 부모 노드가 제일 큰 Max Heap 사용
# 큰 순서대로 큐에 넣고 하나씩 빼서 비교
import heapq

N = int(input())
all = [int(input()) for k in range(N)]
ds = all[0]
ot = [-i for i in all[1:]] 
heapq.heapify(ot) # max heap으로 변환
sum = 0

while ot and -ot[0] >= ds:
    max_ot = -heapq.heappop(ot)
    max_ot -= 1
    ds += 1
    sum += 1
    heapq.heappush(ot, -max_ot)
    
print(sum)