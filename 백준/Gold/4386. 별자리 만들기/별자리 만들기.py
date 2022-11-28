# 해당 문제는 vertex 기준으로 풀어야할듯 -> O(N^2) prim algorithm
import heapq
import math
from collections import defaultdict
n=int(input())
euclid={i:[] for i in range(1,n+1)}

for i in range(1,n+1):
    x,y=map(float,input().split())
    euclid[i]=[x,y]
mst=0
def weight(v1:int,v2:int):
    x_v1,y_v1=euclid[v1]
    x_v2,y_v2=euclid[v2]
    return (x_v1-x_v2)*(x_v1-x_v2)+(y_v1-y_v2)*(y_v1-y_v2)

def decrease_key(vertex,new_key):
    for i in range(len(pQ)):
        if pQ[i][1]==vertex:
            break
    pQ[i][0]=new_key

def get_weight(vertex):
    for i in range(len(pQ)):
        if pQ[i][1]==vertex:
            return pQ[i][0]


INF=10000000
pQ=list()
for i in range(1,n+1):
    pQ.append([INF,i])
pQ[0][0]=0
visit=[0 for i in range(n+1)]
while pQ:
    u_weight,u=heapq.heappop(pQ)
    visit[u]=1
    mst+=math.sqrt(u_weight)
    for v in range(1,n+1):
        if (v!=u):
            if visit[v]==0 and weight(v,u)<get_weight(v):
                decrease_key(v,weight(v,u))
                heapq.heapify(pQ)
    
print(round(mst,2))