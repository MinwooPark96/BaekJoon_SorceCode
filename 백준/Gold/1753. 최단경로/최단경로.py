import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

V, E = map(int,input().split())
s=int(input())
child=[[] for i in range(0,V+1)]
visit=[0 for i in range(V+1)]
for _ in range(E):
    v1,v2,w=map(int,input().split())
    child[v1].append([v2,w])
distance=[1e9 for i in range(V+1)]
distance[s]=0
pQ=[[0,s]]
flag=0
while pQ and sum(visit)!=V:
    _,u=heapq.heappop(pQ)
    if visit[u]==1:
        continue
    
    visit[u]=1
    for v,w in child[u]:
        if distance[u]!=INF and distance[v]>distance[u]+w:
            flag=1
            distance[v]=distance[u]+w
        if flag==1:
            heapq.heappush(pQ,[distance[v],v])
        flag=0

for i in distance[1:]:
    if i==INF:
        print('INF')
    else :
        print(i)