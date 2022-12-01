import sys
def Heapify(idx:int):
    left=idx*2
    right=idx*2+1
    minest_idx=idx
    if left<len(pQ) and pQ[left]<pQ[idx]:
        minest_idx=left
    if right<len(pQ)and pQ[right]<pQ[minest_idx]:
        minest_idx=right
    
    if idx!=minest_idx:
        pQ[minest_idx],pQ[idx]=pQ[idx],pQ[minest_idx]
        Heapify(minest_idx)

def Insert(key):
    pQ.append(key)
    idx=len(pQ)-1
    while idx!=1 and pQ[idx//2]>pQ[idx]:
        pQ[idx//2],pQ[idx]=pQ[idx],pQ[idx//2]
        idx=idx//2
def Pop():
    if len(pQ)==1:
        return None
    n=len(pQ)-1
    pQ[1],pQ[n]=pQ[n],pQ[1]
    result=pQ.pop()
    Heapify(1)
    return result

#input=sys.stdin.readline
n=int(input())
pQ=[-1]
for _ in range(n):
    x=int(input())
    Insert(x)

answer=0
while len(pQ)-1>=2:
    
    curval1=Pop()
    curval2=Pop()
    newval=curval1+curval2
    answer+=newval
    Insert(newval)
print(answer)