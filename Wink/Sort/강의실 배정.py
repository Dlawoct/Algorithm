import sys
import heapq
input = sys.stdin.readline

N = int(input())

times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key= lambda x : x[0])

# 시작 시간 S, 종료 시간 T
# 1) 다음의 S가 T보다 같거나 크면(즉, 시간이 나중이면) 수업을 같은 강의실에서 들을 수 있음 -> 한 수업으로 쳐도 될거 같음
# 2) 다음의 S가 T보다 작으면(즉, 시간이 이전이면) 다른 강의실 하나를 빌려야 됨

heap = []
heapq.heappush(heap, times[0][1])  # 처음 강의 종료 시간

for i in range(1, N):
    if times[i][0] >= heap[0]:  # 1)으로 같은 강의실 취급이므로 pop
        heapq.heappop(heap)

    heapq.heappush(heap, times[i][1])   # 종료 시간 최신화

print(len(heap))