def solution(n, computers):
    answer = 0
    def DFS(idx):
        visited[idx]=1 #idx번째 컴퓨터에 방문함
        for i in range(n):
            if computers[idx][i] and not visited[i]: #idx컴퓨터가 i컴퓨터와 연결되있고 i번째에 방문하지않았다면
                DFS(i)
    visited= [0 for i in range(n)] #[0,0,0]생성
    for i in range(n):
        if visited[i]==0: #i번째 컴퓨터에 방문하지않았으면 DFS탐색
            DFS(i)
            answer+=1 #i번째 컴퓨터의 네트워크에 모두 방문하면 answer증가

    return answer
