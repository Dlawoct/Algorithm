num = int(input())
area = [[0 for i in range(100)] for _ in range(100)]
result = 0
for j in range(num):
    x, y = map(int, input().split())
    
    for k in range(x, x+10):
        for l in range(y, y+10):
            area[k][l] = 1
for c in area:
    result += sum(c)
print(result)