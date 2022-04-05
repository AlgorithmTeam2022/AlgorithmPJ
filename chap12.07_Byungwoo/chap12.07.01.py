def solution(num):
    if sum(list(map(int, list(str(num)[0:len(str(num))//2])))) == sum(list(map(int, list(str(num)[len(str(num)) // 2:])))):
        return "LUCKY"
    return "READY"



#print(solution(int(input())))
print(solution(123402))
print(solution(7755))