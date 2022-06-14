def solution(array, commands):
    answer = []
    for value in commands:
        i=value[0]-1
        j=value[1]
        k=value[2]-1
        temp=array[i:j]
        temp.sort()
        answer.append(temp.pop(k))
    return answer
