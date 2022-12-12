from collections import deque
import sys
input=sys.stdin.readline
V,E=map(int,input().split())
university=list(input().split())
university=[0 if i=='W' else 1 for i in university]
university=[-1]+university
Edge=[]
for _ in range(E):
    v1,v2,w=map(int,input().split())
    Edge.append([v1,v2,w])
parent=[i for i in range(V+1)]
def get_parent(v):
    if parent[v]!=v:
        parent[v]=get_parent(parent[v])
    return parent[v]
def union(u,v):
    p1=get_parent(u)
    p2=get_parent(v)
    if p1>p2:
        parent[p1]=p2
    else:
        parent[p2]=p1
def find(u,v):
    p1=get_parent(u)
    p2=get_parent(v)
    if p1==p2:
        return True
    return False

Edge.sort(key=lambda x:x[2])
Edge=deque(Edge)
mst=0
count_Edge=0
while Edge and count_Edge<=V-1:
    v1,v2,w=Edge.popleft()
    if university[v1]!=university[v2] and not find(v1,v2):
        union(v1,v2)
        count_Edge+=1
        mst+=w
if count_Edge!=V-1:
    print(-1)
else :
    print(mst)