def solution(s, skip, index):
    answer = ''
    skips = [i for i in skip]
    
    for j in s:
        num = index
        while (num > 0):
            j = chr((ord(j) - ord('a') + 1) % 26 + ord('a'))
            if not j in skips:
                num -= 1
        answer += j
    
    return answer
# 문자 s를 s+index로 바꿈
# s+index가 z를 넘으면 다시 a
# skip에 있는 알파벳은 제외