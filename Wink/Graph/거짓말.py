# 거짓말쟁이가 안되면서, 과장된 이야기를 할 수 있어야함
# 진실을 아는 사람이 있으면 거짓말 x 
# 진실을 아는 사람과 다른 사람이 같이 있는 파티도 x
# set을 이용해서 집합을 생각하자

# N: 사람의 수, M: 파티의 수
N, M = map(int, input().split())

# 진실을 아는 사람의 수, 해당 숫자
known = set(input().split()[1:])

# 파티에 참가하는 사람 수, 누구누구인지
party = []
for i in range(M):
    party.append(set(input().split()[1:]))
    
for j in range(M):
    for p in party:
        if p & known:   # 교집합이 있으면, 즉 이 파티에 진실을 알고있는 사람이 있으면
           known = known.union(p)   # known에 해당 인원들을 추가한다
           
cnt = 0
for t in party:
    if t & known:   # 최종적으로 만약에 이 파티에 아는 사람이 있으면 못 간다
        continue
    cnt += 1
    
print(cnt)