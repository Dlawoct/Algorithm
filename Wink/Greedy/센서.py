N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))
distance = []

# 각 센서 사이의 거리를 구함
for i in range(N-1):
    distance.append(sensor[i+1] - sensor[i])
distance.sort(reverse=True)

if K > N: # 집중국이 센서보다 많은 경우 거리가 0임
    print(0)
else: # 제일 큰 거리를 잘라 짧은 거리들만 계산
    total = sum(distance)
    for j in range(K-1):
        total -= distance[j]
    print(total)