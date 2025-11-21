def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        nums =[]
        nums = array[commands[i][0]-1:commands[i][1]]
        nums.sort()
        answer.append(nums[commands[i][2]-1])
        
    return answer