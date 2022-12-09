import sys
import heapq
input=sys.stdin.readline
while 1:
    pQ=[]
    total=0
    mst=0
    V,E=map(int,input().split())
    if V==0 and E==0:
        break
    visit=[0 for i in range(V)]
    Edges=[[] for i in range(V)]
    for _ in range(E):
        v1,v2,w=map(int,input().split())
        Edges[v1].append([v2,w])
        Edges[v2].append([v1,w])
        total+=w
    heapq.heappush(pQ,[0,0])
    while pQ:
        weight,u=heapq.heappop(pQ)
        if visit[u]==1:
            continue
        visit[u]=1
        mst+=weight
        for v,w in Edges[u]:
            if visit[v]==0:
                 heapq.heappush(pQ,[w,v])
    print(total-mst)
    