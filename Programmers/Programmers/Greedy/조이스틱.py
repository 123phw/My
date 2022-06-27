def solution(name):
    answer = 0
    size=len(name)-1

    for i,alpabet in enumerate(name):
        answer += min(ord(alpabet)-ord('A'), ord('Z')-ord(alpabet)+1) #알파벳 순차적 증가와 반대방향 증가 중 더 적은 수를 더함
        next = i+1
        while next<len(name) and name[next]=='A': #현재 알파벳 다음부터 연속된 A문자열 찾기
            next+=1
        #기존방식, 왼쪽부터 연속된 A를 찾는 방식, 오른쪽부터 연속된 A를 찾는 방식
        size=min(size, 2*i+len(name)-next, i+2*(len(name)-next))
    answer += size

    return answer
