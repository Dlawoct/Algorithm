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