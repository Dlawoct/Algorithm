# 제일 마지막에 끝나는 시간을 먼저?
# 경우의 수 : 딱딱 맞아 떨어질 때, 시간이 겹칠때?

N = int(input())
arr = []
time = 0

for i in range(N):
    ti, si = map(int, input().split())
    arr.append([si, ti]) # [[5,3], [14,8], [20,5], [16,1]]

arr.sort(reverse=True) # [[20, 5], [16, 1], [14, 8], [5, 3]]
# if 15시 이상까지 일을 끝내야하면 그대로 그 시간에서 마이너스
# else 15시 미만이면 예정된 끝내야 되는 시간에서 걸리는 시간 마이너스
time = arr[0][0] - arr[0][1] # time == 15
for j in range(1,N): # 1, 2, 3
    if arr[j][0] >= time:
        time -= arr[j][1]
    else:
        time = arr[j][0] - arr[j][1]
if time >=0:
    print(time)
else:
    print(-1)
