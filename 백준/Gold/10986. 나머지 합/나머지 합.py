import sys
input=sys.stdin.readline

n,M=map(int,input().split(" "))
List=list(map(int,input().split(" ")))
cummul=[0]*n
for i in range(len(List)):
    cummul[i]=List[i]+cummul[i-1]
cummul=[i%M for i in cummul]

dic={}
for i in cummul:
    if dic.get(i):
        dic[i]+=1
    else:
        dic[i]=1
count=0
for i in dic:
    if i==0:
        n=dic[i]
        count+=n+n*(n-1)//2
    else:
        n=dic[i]
        count+=n*(n-1)//2

print(count)