#List=[9,8,7,6,5,4,3,2,1]

#n=len(List)
import sys
input=sys.stdin.readline

def mergesort(List:list,start,end):
    
    if start==end:
        return List[start:end+1]
    
    mid=(start+end)//2
    
    L1=mergesort(List,start,mid)
    L2=mergesort(List,mid+1,end)
    result=[]
    
    while L1 or L2:#L1 L2 어느 하나는 존재
        if L1 and L2: #L1 L2 둘다 존재
            if L1[0]>L2[0]:
                curnum=L2.pop(0)
            else:
                curnum=L1.pop(0)
            result.append(curnum)
        else:
            result+=L1+L2
            break
    return result

n=int(input())
List=[]
for _ in range(n):
    List.append(int(input()))
#List=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
#n=len(List)
#List=mergesort(List,0,n)
List.sort()
for i in List:
    print(i)