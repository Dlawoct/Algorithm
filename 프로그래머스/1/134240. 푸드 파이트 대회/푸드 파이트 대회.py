def solution(food):
    answer = ''
    sort_food = [1]
    foods = ''
    for f in range(1,len(food)):
        if food[f] % 2 != 0:
            sort_food.append(food[f]-1)
        else:
            sort_food.append(food[f]) #[1,2,4,6], [1,6,0,2]
    
    for i in range(1,len(sort_food)):
        foods += str(i) * (sort_food[i]//2)
        
    answer = foods + "0" + foods[::-1]
    
        
    return answer