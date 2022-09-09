import sys
input=sys.stdin.readline
n,k=map(int,input().split(" "))
List=list(map(int,input().split(" ")))

sup=max(List) #날의 최대길이
inf=0 #날의 최소길이

if sum(List)-min(List)*n<=k:
    sup=min(List)

def check(List,length):#날의 길이가 주어져 있을 때,벌목양
    result=0
    for i in List:
        result+=max(i-length,0) #날이 더 길다면 벌목양 0
    return result

#정확한 목표 벌목양 k 를 맞출 수 없을 수 도 있다.
#k 이상 벌목할 수 있는 최대 날의 길이를 찾아야 한다.

while inf<=sup:
    mid=(sup+inf)//2
    
    if check(List,mid)>=k: #벌목양이 많다면(날이 짧다면)
        inf=mid+1
    else :
        sup=mid-1

Mid=[mid-1,mid,mid+1]
Answer=[]
for i in Mid:
    if check(List,i)>=k:
        Answer.append(i)
try:
    print(max(Answer))
except:
    print(0)