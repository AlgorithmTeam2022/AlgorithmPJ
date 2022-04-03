def solution(food_times, k):
    led_food_times = len(food_times)
    min_food_times = min(food_times)


    if sum(food_times) <= k:
        return -1
    food = -1

    if min_food_times * led_food_times < k:
        for i in range(0,led_food_times):
            food_times[i] -= min_food_times

        k -= min_food_times * led_food_times




    while k != 0:

        print(food_times, k)
        food = food + 1
        if food == led_food_times:
            food = 0
        if food_times[food] == 0:
            food = food + 1

        food_times[food] -= 1
        k -= 1

    if food_times[food] == 0:
        food = food + 1
    if food == led_food_times:
        food = 0



    return food + 1

print(solution([3,1,1,1,2,4,3],12))
print(solution([1,1,1,1,1],1))
print(solution([10, 8, 4, 10, 6, 9, 2, 7, 6, 8], 48))#답4
print(solution([3, 1, 2],5))
print(solution([7,8,3,3,2,2,2,2,2,2,2,2], 35))#답 2
print(solution([1,1,1,1], 4))