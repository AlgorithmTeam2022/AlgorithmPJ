def solution(st):
    st = sorted(st)
    sum_Of_Num = 0
    while st[0].isdigit():
        sum_Of_Num += int(st[0])
        del st[0]

    return ''.join(st) + str(sum_Of_Num)


print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))