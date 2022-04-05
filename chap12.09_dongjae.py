def solution(s):
    count = 0
    minimum = len(s)
    for n in range(1, len(s)//2+1):
        new = ''
        count = 0
        for i in range(n, n*len(s)//n-n+1, n):
            if s[i-n:i] == s[i:i+n]:
                count += 1
            else:
                if count != 0:
                    new += str(count+1) + s[i-n:i]
                else:
                    new += s[i-n:i]
                count = 0
        if count != 0:
            new += str(count+1) + s[i:]
        else:
            new += s[i:]
        if len(new) < minimum:
            minimum = len(new)
    return minimum
