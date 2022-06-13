import math
def solution(progresses, speeds):
    temp = list(map(lambda x:100-x,progresses)) 
    remainingDay = list(map(lambda x:(math.ceil(temp[x]/speeds[x])),range(len(progresses)))) #(100-progresses)//speeds를 하고 몫을 올림함
    #remainingDay에 남은일수를 계산해 초기화함
    cnt=0
    answer=[]
    first=remainingDay[0]

    while remainingDay: 
        #남은일수에 맞게 배포(값제거)를하고 remainingDay리스트가 모두 제거될때까지 반복
        if first>=remainingDay[0]: #첫값보다 더큰값이나올때까지 값을제거하고 cnt+1
            del remainingDay[0]
            cnt+=1
        else: #첫값보다 더큰값이나오면 첫값을 큰값으로변경, answer리스트에cnt추가후 cnt를0으로변경
            answer.append(cnt)
            first=remainingDay[0]
            cnt=0
    answer.append(cnt)
    return answer
