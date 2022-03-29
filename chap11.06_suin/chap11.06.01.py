def solution(food_times, k):
    j, answer = 0,0
    while (j != k+1):
        for i in range(len(food_times)):
            if(food_times[i]!=0):
                food_times[i] = food_times[i] - 1
                j += 1
                answer = i+1
        if(j==k+1):
            break
    return answer