def solution(s):
    answer = 10000
    for n in range(1, len(s)//2+2): #n은 문자열을 몇개씩 나눌것이냐를 의미
        res=''
        count = 1
        tmp = s[:n] #입력받은 s의 문자열을 n개씩 나눈 묶음 문자열 리스트
        print(tmp)
        for i in range(n,len(s)+n,n):
            if tmp == s[i:i+n]: #결국 tmp는 s한테서 받은 원소롸 비교한는 거라서 tmp자리의 다음 자기부터 같은지 검사하면 됨. 
                print(tmp, s)
                count+=1
            else:
                if count == 1:
                    res += tmp
                else:
                    res += str(cnt)+tmp
                tmp = s[i:i+n]
                cnt = 1
        answer = min(answer, len(res))
    return answer

s = input()
solution(s)