import itertools

def prime_check(value):
    if value < 2:
        return False
    for i in range(2, value//2+1):

        if value%i == 0:
            return False
        
    return True

def solution(numbers):
    cnt=0
    permutation_list=[]
    result=[]
    for i in range(1,len(numbers)+1):
        permutation_list.extend(itertools.permutations(numbers,i))
        result=[int(''.join(i))for i in permutation_list]
    permutation_list=list(set(permutation_list))
    for j in set(result):
        if prime_check(j) == True:
            cnt+=1
    return cnt
'''
1. 반복문에 itertools.permutations로 조합가능한 순열을 모두 찾아 리스트네 extends로 삽입
2.해당 리스트를 ''.join으로 통해 튜플의 각값을 정수로 변경함
3.set으로 리스트의 중복제거
4.for문에서 소수를 찾는 함수를 통해 반환값이 true이면 cnt를 증가함
5.반복문이 끝나면 cnt를 반환함
'''
