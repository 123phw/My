def solution(k, dungeons):
    answer = 0
    cnt_list=[]
    def dfs(k2,dun2,cnt2):
        for i in range(len(dun2)):
            if i<len(dun2)-1 and k2>=dun2[i][0] and k2>=dun2[i][1]:
                dfs(k2-dun2[i][1],dun2[:i]+dun2[i+1:],cnt2+1)
            elif i==len(dun2)-1 and k2>=dun2[i][0] and k2>=dun2[i][1]:
                dfs(k2-dun2[i][1],dun2[:i], cnt2+1)
        cnt_list.append(cnt2)

    cnt=0
    for i in range(len(dungeons)):
        if i<len(dungeons)-1 and k>=dungeons[i][0] and k>=dungeons[i][1]:
            dfs(k-dungeons[i][1],dungeons[:i]+dungeons[i+1:],cnt+1)
        elif i==len(dungeons)-1 and k>=dungeons[i][0] and k>=dungeons[i][1]:
            dfs(k-dungeons[i][1],dungeons[:i], cnt+1)
    answer=max(cnt_list)
    print(answer)
    return answer
