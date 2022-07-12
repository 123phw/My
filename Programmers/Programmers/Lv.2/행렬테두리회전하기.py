import sys
def solution(rows, columns, queries):
    answer = []
    n=1
    array=[[(i)*columns+(j+1) for j in range(columns)] for i in range(rows)]
    for x1, y1, x2, y2 in queries:
        answer.append(rotation(x1,y1,x2, y2,array))

    return answer
def rotation(x1, y1, x2, y2, array):
    m=sys.maxsize
    now=[x1,y1]
    temp2=array[x1][y1-1] #14
    #오
    for i in range(y1,y2+1):
        temp=array[x1-1][i-1] #현재값 temp에 저장
        array[x1-1][i-1]=temp2 #이전값 가져오기
        temp2=temp
        m = min(m,temp)
    #아
    for i in range(x1+1, x2+1):
        temp=array[i-1][y2-1]
        array[i-1][y2-1]=temp2
        temp2=temp
        m = min(m,temp)
    #왼
    for i in range(y2-1,y1-1,-1):
        temp=array[x2-1][i-1]
        array[x2-1][i-1]=temp2
        temp2=temp
        m = min(m, temp)
    #위
    for i in range(x2-1,x1,-1):
        temp=array[i-1][y1-1]
        array[i-1][y1-1]=temp2
        temp2=temp
        m = min(m,temp)

    return m
