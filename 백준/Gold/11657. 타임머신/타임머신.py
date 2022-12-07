import sys
input=sys.stdin.readline

V,E=map(int,input().split())
s=1
INF=int(1e9)
distance=[INF for i in range(V+1)]
distance[s]=0
parent=[0 for i in range(V+1)]

Edges=[]

for _ in range(E):
    v1,v2,w=map(int,input().split())
    Edges.append([v1,v2,w])
    
def relax(v1,v2,w):
    if distance[v1]>=INF:
        return
    
    if distance[v2]>distance[v1]+w:
        distance[v2]=distance[v1]+w
        parent[v2]=v1
        
def bellman():
    global distance
    for _ in range(V-1):
        for v1,v2,w in Edges:
            relax(v1,v2,w)
    for v1,v2,w in Edges:
        if distance[v1]!=INF and distance[v2]>distance[v1]+w:
            return False
    return True
checker=bellman()
if not checker:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, V+1):
        if distance[i] == INF: # 도달할 수 없는 경우 -1 출력
            print('-1')
        else: # 도달할 수 있는 겨우 거리를 출력
            print(distance[i])