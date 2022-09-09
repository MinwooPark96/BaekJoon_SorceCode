import sys
import math
from typing import Deque
input=sys.stdin.readline

N=int(input())
List=[]
for _ in range(N):
    List.append(int(input()))

List.sort(reverse=True)
difference=[]
for i in range(N-1):
    for j in range(i+1,N):
        difference.append(List[i]-List[j])

difference=list(set(difference))
Answer=[]

minnum=min(difference)

for i in range(minnum,1,-1):#minnum~2 까지 넣어보기
    test=1
    for value in difference:
        if value%i!=0:#나머지가 0이 아닌경우가 나오면 후보아님.
            test=0
            break
    if test==1:
        Answer=i
        break

result=Deque([])
def part(n:int):
    if n==2:
        print(2)
    elif n==3:
        print(3)
    else :
        for i in range(int(math.sqrt(n)),1,-1):
            if n%i==0:
                if i*i==n:
                    result.append(i)
                else: 
                    result.appendleft(i)
                    result.append(n//i)
        result.append(n)
        for i in result:
            print(i,end=" ")
part(Answer)