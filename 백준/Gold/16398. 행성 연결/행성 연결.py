import heapq
import sys
input=sys.stdin.readline
V=int(input())

weight=[[0 for _ in range(V+1)]]

for i in range(V):
    row=[0]+list(map(int,input().split()))
    weight.append(row)
#prim (v+e)logv
visit=[0 for _ in range(V+1)]
mst=0
pQ=[]
heapq.heappush(pQ,[0,1])
while pQ:
    u_w,u=heapq.heappop(pQ)
    if visit[u]:
        continue
    visit[u]=1
    mst+=u_w
    for v in range(1,V+1):
        v_w=weight[u][v]
        if v_w!=0 and visit[v]==0:
            heapq.heappush(pQ,[v_w,v])
print(mst)