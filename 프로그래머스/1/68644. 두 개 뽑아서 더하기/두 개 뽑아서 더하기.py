from itertools import combinations
def solution(numbers):
    answer = []
    for comb in combinations(numbers, 2):
        if sum(comb) not in answer:
            answer.append(sum(comb))
    return sorted(answer)