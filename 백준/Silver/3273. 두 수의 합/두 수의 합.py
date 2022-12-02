import sys
input=sys.stdin.readline
n=int(input())
count=0
numList=list(map(int,input().split()))
target=int(input())
visit={i:0 for i in numList}
numdict={i:1 for i in numList}

for i in visit:
    if not visit[i]:
        visit[i]=1
        if target-i != i and numdict.get(target-i):
            count+=1
            if visit.get(target-i)==0:
                visit[target-i]=1
            
print(count)
            
        
