def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    for i in range(m-1, len(score), m):
        answer += score[i] * m
    return answer

# 1~k 점수의 사과
# m개의 사과를 포장
# 한 사과 상자의 가격 = 가장 낮은 점수 p * m개
# m개를 담을 때 가격 높은 순대로 담기, 남으면 버림
# [3,3,2, 2 ,1,1,1]
# [4,4, 4 ,4,4, 4 ,2,2, 2 ,2,1, 1 ]