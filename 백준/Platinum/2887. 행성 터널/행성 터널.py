import heapq
import sys
import copy
#input=sys.stdin.readline


mst=0
n=int(input())
distance_list=list()
for i in range(1,n+1):
    x,y,z=map(int,input().split())
    distance_list.append([i,x,y,z])

distance_x=copy.deepcopy(distance_list)
distance_x.sort(key = lambda x: x[1])
distance_y=copy.deepcopy(distance_list)
distance_y.sort(key = lambda x: x[2])
distance_z=copy.deepcopy(distance_list)
distance_z.sort(key = lambda x: x[3])

child={j:dict() for j in range(1,n+1)}

for i in range(1,n):
    v1,x,y,z=distance_x[i]
    v2,a,b,c=distance_x[i-1]
    child[v1][v2]=min(abs(a-x), abs(b-y), abs(c-z))
    child[v2][v1]=min(abs(a-x), abs(b-y), abs(c-z))
    v1,x,y,z=distance_y[i]
    v2,a,b,c=distance_y[i-1]
    child[v1][v2]=min(abs(a-x), abs(b-y), abs(c-z))
    child[v2][v1]=min(abs(a-x), abs(b-y), abs(c-z))
    v1,x,y,z=distance_z[i]
    v2,a,b,c=distance_z[i-1]
    child[v1][v2]=min(abs(a-x), abs(b-y), abs(c-z))
    child[v2][v1]=min(abs(a-x), abs(b-y), abs(c-z))
    
order_num=0
ovy=dict()
voy=dict()

distance_list.sort(key = lambda x: x[2])
for i in range(n):
    ovy[order_num]=distance_list[i][0]
    voy[distance_list[i][0]]=order_num

    order_num+=1

order_num=0
ovz=dict()
voz=dict()
distance_list.sort(key = lambda x: x[3])
for i in range(n):
    ovz[order_num]=distance_list[i][0]
    voz[distance_list[i][0]]=order_num

    order_num+=1


pQ=[[0,1]]
visit=[0 for i in range(n+1)]
count=0
while pQ:
    if count==n:
        break
    u_weight,u=heapq.heappop(pQ)
    if visit[u]==1:
        continue
    visit[u]=1
    count+=1
    mst+=u_weight
    for v in child[u].keys():
        if visit[v]==0:
            heapq.heappush(pQ,[child[u][v],v])
print(mst)

