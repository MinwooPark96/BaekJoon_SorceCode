import sys
input=sys.stdin.readline
N=int(input())
#List=[1,3,8,-2,2]
#N=len(List)
List=[]
for i in range(N):
    List.append(int(input()))
List.sort()
maxnum=List[-1]
minnum=List[0]
print(round(sum(List)/N))
if N==1:
    print(List[0])
else:
    print(List[N//2])

count={}
for i in range(N):
    if not count.get(List[i]):
        count[List[i]]=1
    try:
        if List[i]==List[i+1]:
            count[List[i]]+=1
    except :
        if List[i-1]!=List[i]:
            count[List[i]]=1

mod={}
for i in count.keys():
    if not mod.get(count[i]):
        mod[count[i]]=[i]
    else:
        mod[count[i]].append(i)
maxcount=max(mod.keys())
if len(mod[maxcount])==1:
    print(mod[maxcount][0])
else:
    print(mod[maxcount][1])
print(maxnum-minnum)