def solution(record):
    answer = []
    size=len(record)
    record_split=[list(map(str, i.split())) for i in record] #문자열 공백을 잘라 리스트에 저장
    #for문 내에서 i.split()해도됨
    dic={}

    for i in range(size): #변동있는 이름을 변경
        if record_split[i][0] in ["Enter", "Change"]:
            dic[record_split[i][1]]=record_split[i][2]

    for j in range(size): #출력
        if record_split[j][0]=="Enter":
            answer.append(dic[record_split[j][1]]+"님이 들어왔습니다.")
        elif record_split[j][0]=="Leave":
            answer.append(dic[record_split[j][1]]+"님이 나갔습니다.")

    return answer
