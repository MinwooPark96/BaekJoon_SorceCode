from typing import Deque
import sys
input=sys.stdin.readline
n=int(input())
inputs=list(map(int,input().split(" ")))
numqueue=Deque(inputs)
operatorlist=list(list(map(int,input().split(" "))))
op=0
operator=[]
for i in operatorlist:
    for _ in range(i):
        operator.append(op)
    op+=1
#numqueue=Deque([1,2,3,4,5,6])
#operator=[0,0,1,2,3]
use=[False]*(n-1)

Answer=[]

def calculator(List:Deque):
    
    if len(List)==1:
        Answer.append(List[0])
    
    else:
        for i in range(n-1):#0~5
            if not use[i]:
                use[i]=True
                x=List.popleft()
                y=List.popleft()
                result=codeCal(operator[i],x,y)
                List.appendleft(result)
                ###recursive
                calculator(List)
                ###recursive
                List.popleft()
                List.appendleft(y)
                List.appendleft(x)
                use[i]=False
        
def codeCal(o:int,x:int,y:int):
    #0:+, 1:-, 2:*, 3:// 
    if o==0:
        return x+y
    elif o==1:
        return x-y
    elif o==2:
        return x*y
    elif o==3:
        return int((x)/y)
calculator(numqueue)
print(max(Answer))
print(min(Answer))