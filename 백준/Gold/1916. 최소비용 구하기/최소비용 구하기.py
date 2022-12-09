import sys
import heapq
input=sys.stdin.readline
pQ=[]
inf=int(1e9)
V=int(input())
E=int(input())
Edges=[[] for i in range(V+1)]
visit=[0 for _ in range(V+1)]
distance=[inf for i in range(V+1)]

for _ in range(E):
    v1,v2,w=map(int,input().split())
    Edges[v1].append([v2,w])
s,f=map(int,input().split())
distance[s]=0

heapq.heappush(pQ,[distance[s],s])
while pQ:
    weight_u,u=heapq.heappop(pQ)
    if visit[u]==1:
        continue
    visit[u]=1
    for v,w in Edges[u]:
        flag=0
        if distance[u]!=inf and distance[v]>distance[u]+w:
            flag=1
            distance[v]=distance[u]+w
        if flag==1 and visit[v]==0:
            heapq.heappush(pQ,[distance[v],v])
print(distance[f])