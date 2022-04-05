def solution(st):
    st = sorted(st)
    count = 0
    while st[0].isdigit():
        count += int(st[0])
        del st[0]

    return ''.join(st) + str(count)


print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))