import sys
input=sys.stdin.readline
n=int(input())
Time=list(map(int,input().split(" ")))
Timedic={i+1:Time[i] for i in range(n)}
People=[i+1 for i in range(n)]
People.sort(key=lambda x:Timedic[x])
answer=0
t=n
for i in People:
    answer+=Timedic[i]*t
    t-=1
print(answer)