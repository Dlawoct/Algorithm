def solution(arr):
    arr.remove(min(arr))
    if sum(arr) == 0:
        return [-1]
    return arr