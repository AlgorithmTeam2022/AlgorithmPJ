def solution(num):
    num = str(num)
    L = sum(list(map(int, list(num[0:len(num)//2]))))
    R = sum(list(map(int, list(num[len(num) // 2:]))))

    if L == R:
        return "LUCKY"
    return "READY"



print(solution(int(input())))
# print(solution(123402))
# print(solution(7755))