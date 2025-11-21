def solution(n, arr1, arr2):
    answer = []
    last_arr = []
    
    for i in range(n):
        last_arr.append(bin(arr1[i] | arr2[i]))
        last_arr[i] = last_arr[i][2:n+2]
        while len(last_arr[i]) < n:
            last_arr[i] = "0" + last_arr[i]
    
    for s in last_arr:
        text = ""
        for c in s:
            if c == "1":
                text += "#"
            else:
                text += " "
        answer.append(text)
        
    return answer
# arr1, arr2를 2진수로 바꾸고, or연산하면 최종 지도의 이진수 값 나옴
