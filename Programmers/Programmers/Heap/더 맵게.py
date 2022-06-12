import heapq
def solution(scoville,k):
    heapq.heapify(scoville)
    answer=0
    while scoville[0]<k: #트리 루트에 위치한 0인덱스는 항상 가장작은값
        #scoville의 가장 작은값이 k보다 커질때까지 반복
        if len(scoville)<=1:
            answer=-1
            break
        else:
            heapq.heappush(scoville,(heapq.heappop(scoville)+(heapq.heappop(scoville)*2)))
            #scoville리스트에 제일작은 두값을 빼고 섞은 값을 추가
            answer+=1
    return answer
