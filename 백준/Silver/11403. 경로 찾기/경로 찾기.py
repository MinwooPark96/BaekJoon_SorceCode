from collections import deque
import sys
input=sys.stdin.readline
Inf=int(1e9)
V=int(input())
w=[]
for _ in range(V):
    row=list(map(int,input().split()))
    row= [Inf if i==0 else i for i in row]
    w.append(row)
import copy
d=copy.deepcopy(w)
for k in range(V):
    for i in range(V):
        for j in range(V):
            if d[i][k]!=Inf and d[k][j] != Inf and d[i][k]+d[k][j]<d[i][j]:
                d[i][j]=d[i][k]+d[k][j]
for i in range(V):
    for j in range(V):
        if d[i][j]==Inf:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()