import sys
#input=sys.stdin.readline
n=int(input())
Matrix=[]
for _ in range(n):
    row=input()
    Matrix.append([int(i) for i in row])


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

Answer=""

def QuardTree(n,Matrix):
    global Answer
    checker=count(Matrix,n)
    if checker!=-1:
        Answer=Answer+str(checker)
    else:
        Answer=Answer+"("
        dic={}
        dic[1]=[i[:n//2] for i in Matrix[:n//2]]
        dic[2]=[i[n//2:] for i in Matrix[:n//2]]
        dic[3]=[i[:n//2] for i in Matrix[n//2:]]
        dic[4]=[i[n//2:] for i in Matrix[n//2:]]
    
        for i in dic:
            QuardTree(n//2,dic[i])
        Answer=Answer+")"

QuardTree(n,Matrix)
print(Answer)

