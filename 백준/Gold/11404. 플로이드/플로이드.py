import sys
import copy
input=sys.stdin.readline
V=int(input())
E=int(input())
inf=int(1e9)
weight=[[0 if i==j else inf for j in range(V+1)]for i in range(V+1)]
for _ in range(E):
    v1,v2,e=map(int,input().split())
    if weight[v1][v2]==inf or weight[v1][v2]>e:
        weight[v1][v2]=e
            
    
distance=copy.deepcopy(weight)
parent=[[None for j in range(V+1)] for i in range(V+1)]
for i in range(1,V+1):
    for j in range(1,V+1):
        if i!=j and weight[i][j]!=inf:
            parent[i][j]=i
for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if distance[i][k] !=inf and distance[k][j] !=inf and distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
                parent[i][j]=parent[k][j]

for i in range(1,V+1):
    for j in range(1,V+1):
        if distance[i][j]==inf:
            print(0,end=' ')
        else:
            print(distance[i][j],end=' ')
    print()