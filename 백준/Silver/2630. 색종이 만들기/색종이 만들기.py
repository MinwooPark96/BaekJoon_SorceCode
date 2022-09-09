import sys
input=sys.stdin.readline
n=int(input())
Matrix=[]
for _ in range(n):
    Matrix.append(list(map(int,input().split())))


def count(matrix,n): #하나의 색으로 확정되면 색상과 개수를 반환 
    numList=[j for i in matrix for j in i]
    count=[0,0]
    for num in numList:
        count[num]+=1
    
    if not count[0]:
        return 1
    if not count[1]:
        return 0
    else:
        return -1

Answer=[0,0]
    
def QuardTree(n,Matrix):
    checker=count(Matrix,n)
    if checker!=-1:
        Answer[checker]+=1
    else:
        dic={}
        dic[1]=[i[:n//2] for i in Matrix[:n//2]]
        dic[2]=[i[n//2:] for i in Matrix[:n//2]]
        dic[3]=[i[:n//2] for i in Matrix[n//2:]]
        dic[4]=[i[n//2:] for i in Matrix[n//2:]]
    
        for i in dic:
            QuardTree(n//2,dic[i])
        
QuardTree(n,Matrix)
for i in Answer:
    print(i)