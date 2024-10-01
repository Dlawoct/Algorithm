# 올바른 배열
# 배열의 각 원소 n의 n+4까지의 숫자 배열을 만들고 현재 배열과 비교?
# 만약에 있으면 5 - n개 해서 가장 작은 숫자 고르기

N = int(input())
elements = []
difference = []

for i in range(N):
    elements.append(int(input()))

for j in range(N):
    new_elements = [0] * 5
    for k in range(5):
        new_elements[k] = elements[j] + k  
    
    for l in elements:
        if l in new_elements:
            new_elements.remove(l)
    
    difference.append(len(new_elements))
    
print(min(difference))