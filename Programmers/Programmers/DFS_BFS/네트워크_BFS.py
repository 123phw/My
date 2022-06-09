def solution(n, computers):            
    
    def BFS(i):
        q = deque()
        q.append(i)
        print(q)
        while q: #컴퓨터끼리 연결이 되어있다면 q에 추가하고 q에 들어있는 모든 컴퓨터를 반복해서 확인
		#visited함수에도 방문한 컴퓨터를 추가하여 반복해서 방문할수 없도록 함
            i = q.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] and not visited[a]:
                     q.append(a)
                     
                
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
            print(visited)
    return answer
