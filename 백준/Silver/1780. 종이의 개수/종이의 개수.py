import sys
input=sys.stdin.readline
n=int(input())
Matrix=[]
for _ in range(n):
    Matrix.append(list(map(int,input().split())))


def count(matrix,n): #하나의 색으로 확정되면 색상과 개수를 반환 
    numList=[j for i in matrix for j in i]
    count=[0,0,0]
    for num in numList:
        count[num]+=1
    
    if max(count)==n*n:
        for i in range(-1,2):
            if count[i]:
                return i
    else:
        return 2

Answer=[0,0,0]
    
def QuardTree(n,Matrix):
    checker=count(Matrix,n)
    if checker!=2:
        Answer[checker]+=1
    else:
        dic={}
        for i in range(3):
            for j in range(3):
                dic[(i,j)]=[row[n//3*j:n//3*(j+1)] for row in Matrix[n//3*i:n//3*(i+1)]]
        for i in dic:
            QuardTree(n//3,dic[i])
        
QuardTree(n,Matrix)
for i in range(-1,2):
    print(Answer[i])