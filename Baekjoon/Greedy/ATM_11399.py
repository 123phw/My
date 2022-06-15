n = int(input()) #사람수
p = list(map(int, input().split())) #각 사람이 돈을 인출시 걸리는 시간

p.sort()
temp,sum=0,0
for i in p:
    temp+=i
    sum+=temp

print(sum)
