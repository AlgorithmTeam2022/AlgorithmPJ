food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):
    print(food_times)
    j, answer = 0,0
    while (j != k+1):
        for i in range(len(food_times)):
            if(food_times[i]!=0):
                food_times[i] = food_times[i] - 1
                j += 1
                answer = i+1
                print(food_times, answer)
            else:
                continue
            if(j==k):
                break
    return answer

s = solution(food_times, k)
print(s)