all = int(input())
n = int(input())
sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum = sum + (a*b)
    
if sum == all:
    print("Yes")
else:
    print("No")