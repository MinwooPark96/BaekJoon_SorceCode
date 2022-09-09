import sys
input=sys.stdin.readline
n,k=map(int,input().split(" "))
List=[]
for _ in range(n):
    List.append(int(input()))


sup=sum(List)//k #가장 최대로 만들 수 있는 길이
inf=min(List)//k #가장 최소로 만들 수 있는 길이
mid=0
#inf<= answer <=sup

def check(List:list,x:int):
    count=0
    for i in List:
        try:
            count+=i//x
        except:
            count=0
            break
    return count
#k 이상개 만들수있는 숫자중 가장 큰 수를 찾아야 한다.

while inf<=sup:
    mid=(inf+sup)//2
    if check(List,mid)>=k: #정답에 속한다면,
        inf=mid+1
    else:
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