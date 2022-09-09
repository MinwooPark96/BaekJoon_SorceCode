import copy
import sys
#input=sys.stdin.readline

def Dot(A,B)->list: #A@B
    C=copy.deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A)):
            C[i][j]=0
            for k in range(len(A)):
                C[i][j]+=A[i][k]*B[k][j]
            C[i][j]
    return C
def Binary(m:int)->str:
    a=bin(m)[2:]
    return [int(i) for i in a[-1::-1]] #14->0111 : 2+4+8

def Identity(A):
    n=len(A)
    result=copy.deepcopy(A)
    for i in range(n):
        for j in range(n):
            if i==j:
                result[i][j]=1
            else:
                result[i][j]=0
    return result

def DotB(A,k):# k= 0,1,2..
    result=[]
    result.append(Dot(A,Identity(A)))
    while k!=0:
        A=Dot(A,A)
        k-=1
        result.append(A)
    return result

###FunctionPart End###

n=int(input())
A=[[0,1],[1,1]]
m=n-1
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    binm=Binary(m)
    maxk=len(binm)-1
    AList=DotB(A,maxk)
    empty=True;count=0
    for i in binm:
        if i and empty:
            answer=AList[count]
            empty=False
        elif i:
            answer=Dot(answer,AList[count])
        count+=1 
    
    print(answer[-1][-1])