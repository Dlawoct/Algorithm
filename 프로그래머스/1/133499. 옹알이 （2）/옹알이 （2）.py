def solution(babbling):
    answer = 0
    babble_list = ["aya", "ye", "woo", "ma"]
    
    for s in babbling:
        text = ""
        pre_text = ""
        is_true = True
        for i in s:
            text += i
            if text in babble_list and pre_text != text:
                pre_text = text
                text = ""
                is_true = True
            else: 
                is_true = False
                
        if is_true:
            answer += 1
        
    return answer
# 애기가 발음 할 수 있는건 리스트에 있는 단어 뿐
# 차피 단어 시작이 다르니까 a가 나오면 무조건 aya면 통과?