import math
n=int(input())
colordic={i+1:1 for i in range(n)}
visit={i+1:False for i in range(n)}

color=2
for i in visit:
    if i==1:
        visit[i]=True
        continue    
    if not visit[i]:#방문한적이없다면
        temp=1
        interest=i #현재 관심숫자
        while interest<=n: #우리의 숫자범위내에서
            if not visit[interest]:
                visit[interest]=True
                colordic[interest]=color
            interest=i
            temp+=1
            interest*=temp #계속곱해줌
        color+=1

Answer=colordic.values()
totalcolor=max(Answer)

print(totalcolor)
for i in Answer:
    print(i,end=" ")