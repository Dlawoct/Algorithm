N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))
distance = []

for i in range(N-1):
    distance.append(sensor[i+1] - sensor[i])
distance.sort(reverse=True)

if K > N: #
    print(0)
else:
    total = sum(distance)
    for j in range(K-1):
        total -= distance[j]
    print(total)