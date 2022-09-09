import sys

n,m=map(int,input().split())
A=[]
for i in range(n):
    A.append(list(map(int,sys.stdin.readline().rstrip().split())))
    #A.append(list(map(int,input().rstrip().split())))
m,k=map(int,input().split())
B=[]
for i in range(m):
    #B.append(list(map(int,input().rstrip().split())))
    B.append(list(map(int,sys.stdin.readline().rstrip().split())))
C=[[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for t in range(m):
            C[i][j]+=A[i][t]*B[t][j]

for i in range(n):
    for j in range(k):
        print(C[i][j],end=" ")
    print()