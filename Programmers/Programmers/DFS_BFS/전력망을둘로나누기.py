def solution(n, wires):
    count_list=[]
    answer = -1
    def bfs(wires_split):
        cnt=1
        tree=[[] for i in range(n)] 
        q=[0]
        visit=[0 for i in range (n)]
        visit[0]+=1
        for j in wires_split: #송전탑끼리 연결된 번호를 표시
            tree[j[0]-1].append(j[1]-1)
            tree[j[1]-1].append(j[0]-1)
        if tree[0]==[]: #송전탑의 0번트리와 연결된 것이 없으면 1번송전탑을 방문
            q=[1]
            visit[0],visit[1]=0,1
        while q: #방문해야할 송전탑을 q에넣고 연결된 송전탑 갯수확인
            for k in (tree[q.pop(0)]):
                if visit[k]==1:
                    continue
                else: 
                    q.append(k)
                    visit[k]+=1
                    cnt+=1
        count_list.append(abs(cnt-(n-cnt))) #분리된 두 전력망의 개수차이를 count_list에 추가함
    for i in range(len(wires)): #전선개수만큼 반복
        wires_split=wires[:i]+wires[i+1:] #전선 중에서 하나씩 빼서 bfs탐색하기
        bfs(wires_split)
    return min(count_list)
