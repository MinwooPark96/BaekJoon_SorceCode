import math
from collections import deque
import sys
#input=sys.stdin.readline


def get_parent(v:int):
    if parent[v]!=v:
        parent[v]=get_parent(parent[v])
    
    return parent[v]
def union(v1,v2):
    parent_v1=get_parent(v1)
    parent_v2=get_parent(v2)
    if parent_v1>parent_v2:
        parent[parent_v1]=parent_v2
    else:
        parent[parent_v2]=parent_v1
def find(v1,v2):
    parent_v1=get_parent(v1)
    parent_v2=get_parent(v2)
    if parent_v1==parent_v2:
        return True
    return False    


n,m=map(int,input().split())
euclid=[[] for i in range(n+1)]
parent=[i for i in range(n+1)]

for i in range(n):
    x,y=map(int,input().split())
    euclid[i+1]=[x,y]
    
connected={i:set() for i in range(1,n+1)}
connected_edge=0
for _ in range(m):
    v1,v2=map(int,input().split())
    if v2 in connected.get(v1):
        continue
    
    connected[v1].add(v2)
    connected[v2].add(v1)
    connected_edge+=1
Edges=[]
mst=0
linked_edge=0
for i in range(1,n):
    for j in range(i+1,n+1):
        x1,y1=euclid[i]
        x2,y2=euclid[j]
        distance=(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) 
        if j in connected.get(i) or i in connected.get(j):
            union(i,j)
            continue
        Edges.append([i,j,distance])
Edges.sort(key=lambda x:x[2])
Edges=deque(Edges)
while linked_edge!=n-1-connected_edge:
    try:
        v1,v2,square_distance=Edges.popleft()
    except:
        break
    if find(v1,v2):
        continue
    union(v1,v2)
    mst+=math.sqrt(square_distance)
    linked_edge+=1
print(format(mst, ".2f"))