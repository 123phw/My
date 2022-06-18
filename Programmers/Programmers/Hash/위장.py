import collections
def solution(clothes):
    b=list(zip(*clothes))[1]
    cnt=collections.Counter(b)
    temp=list(cnt.values())
    answer=1
    for i in range(len(temp)):
        answer*=(temp[i]+1)
    answer=answer-1
    return answer
