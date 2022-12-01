N,M=map(int,input().split())
child={i:[] for i in range(1,N+1)}
visit=[i for i in range(N+1)]
indegree=[0 for i in range(N+1)]
indegree[0]=40000
for _ in range(M):
    v1,v2=map(int,input().split())
    child[v1].append(v2)
    indegree[v2]+=1
import heapq
pQ=[]
sort_list=[]
for v in range(N+1):
    if not indegree[v]:
        pQ.append(v)
        sort_list.append(v)
while pQ:
    v=heapq.heappop(pQ)
    for v_child in child[v]:
        indegree[v_child]-=1
        if indegree[v_child]==0:
            pQ.append(v_child)
            sort_list.append(v_child)
            
for i in sort_list:
    print(i,end=' ')
    