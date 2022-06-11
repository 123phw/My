def solution(n, vertex):
    answer = 0
    distance=[0 for i in range(n)]
    visited=[0 for i in range(n)]
    visited[0]=1
    
    graph=[[]for i in range (n)]
    for v1,v2 in vertex:
        graph[v1-1].append(v2-1)
        graph[v2-1].append(v1-1)
    
    queue=[0]
    while queue:
        idx = queue.pop(0)
        for i in graph[idx]: 
            if visited[i]==1: #해당하는 노드에 방문했다면
                continue
            distance[i]=distance[idx]+1 #방문하지않았다면
            visited[i]=1
            queue.append(i)
    distance.sort(reverse=True)
    answer=distance.count(distance[0])
    return answer
  '''
n크기의 리스트를 만들어 노드와 직접 연결된 값들을 추가한다.
즉, 1번 인덱스에는 1번인덱스와 직접 연결된 노드를 추가함
그리고 1번과 직접연결된 노드에 방문하여 거리 리스트에 1씩추가하고
해당 노드에 저장된 노드에 다시 방문하여 이전 리스트값에 1을 추가함
계속 반복하고 거리리스트에 가장 큰 숫자 갯수를 반환함
'''
