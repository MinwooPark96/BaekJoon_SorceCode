import copy
import sys
input=sys.stdin.readline

def Dot(A,B)->list: #A@B
    C=copy.deepcopy(A)
    for i in range(2):
        for j in range(2):
            C[i][j]=0
            for k in range(2):
                C[i][j]+=A[i][k]*B[k][j]%1000000007
            C[i][j]%1000000007
    return C


def DotB(A,k):# k= 0,1,2..
    answer=[[1,0],[0,1]]
    num=k
    matrix=copy.deepcopy(A)
    while num!=0:
        if num%2:
            answer=Dot(answer,matrix)
        matrix=Dot(matrix,matrix)
        num//=2
    return answer

n=int(input())
if n==0:
    print(0)
else:
    result=DotB([[0,1],[1,1]],n-1)
    print(result[-1][-1]%1000000007)     
        