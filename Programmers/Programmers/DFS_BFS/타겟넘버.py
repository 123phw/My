def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result): #인덱스값이 증가하면서 해당인덱스+,-값을 모두 호출하는 재귀함수 구현
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer

numbers=[4, 1, 2, 1]
target=4
solution(numbers, target)
'''
재귀함수를 이용한 DFS구현(그래프형)
-위의 방법은 처음부터 마지막 인덱스까지 증가할때까지
DFS함수의 매개변수값에 각 인덱스값을 더한값과 뺀값을 모두
넣어 호출하면서 결과값에 target값과 동일한 값이 나오면
answer값을 증가하면서 최종적으로 target값과 동일한 계산결과의
갯수를 구할수 있음
'''
