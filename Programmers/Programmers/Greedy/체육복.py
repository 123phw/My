def solution(n, lost, reserve):
    answer = 0
    lost_ps=[i for i in lost if i not in reserve]
    reserve_ps=[i for i in reserve if i not in lost]
    lost_ps.sort()
    reserve_ps.sort()
    cnt=n-len(lost_ps)
    for i in lost_ps:
        if i-1 in reserve_ps:
            reserve_ps.remove(i-1)
            cnt+=1
        elif i+1 in reserve_ps:
            reserve_ps.remove(i+1)
            cnt+=1
    return cnt
