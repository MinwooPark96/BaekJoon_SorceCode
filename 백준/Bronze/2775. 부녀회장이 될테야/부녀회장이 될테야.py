# 0층 1 2 3
#1층 1 3 6
#2층 1 4 10


###
n=int(input())

floors=[]
sts=[]

for _ in range(n):
    floors.append(int(input()))
    sts.append(int(input()))


x=max(floors)
y=max(sts)
matrix=[[0]*y for _ in range(x+1)]

for i in range(x+1):
    for j in range(y):
        if i==0 :
            matrix[i][j]=j+1
        elif j==0:
            matrix[i][j]=1
        else :
            matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
for i in range(n):
    print(matrix[floors[i]][sts[i]-1])