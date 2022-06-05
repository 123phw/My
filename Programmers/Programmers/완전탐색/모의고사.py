def solution(answers):
    p1, p2, p3= 0,0,0
    answer=[]
    pattern=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for idx, v in enumerate(answers):
        if v==pattern[0][idx%5]:
            p1+=1
        if v==pattern[1][idx%8]:
            p2+=1
        if v==pattern[2][idx%10]:
            p3+=1
    person=[[1,p1],[2,p2],[3,p3]]
    for i in range(3):
        if max(person,key=lambda x: x[1])[1]== person[i][1]:
            #person리스트의 1인덱스의 max값과 비교해 같으면 answer리스트에추가
            answer.append(i+1)
    return answer

'''
3명의 패턴을 각각 리스트에 초기화
답이 적힌 answers리스트와 각 패턴들을 반복분에서 비교하고
패턴의 인덱스%패턴 길이값을 구하면 패턴을 무한반복해서 비교할수있음
'''
