def solution(s):
    result=[]
    if len(s)==1:
        return 1
    for i in range(1, (len(s)//2)+1):
        b = ''
        cnt = 1
        tmp=s[:i]

        for j in range(i, len(s), i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b = b + str(cnt)+tmp
                else:
                    b = b + tmp
                tmp=s[j:j+i]
                cnt = 1
        if cnt!=1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
                
        result.append(len(b))
    return min(result)

출처: https://eunhee-programming.tistory.com/135 [코드짜는 문과녀:티스토리]
