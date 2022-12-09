import sys
input=sys.stdin.readline
def bellman(n):
    for s in range(1,n+1):
        distance=[INF for _ in range(n+1)]
        distance[s]=0
        for i in range(n):
            for u,v,w in edges:
                if u!=INF and distance[v]>distance[u]+w:
                    if i==n-1:
                        return False
                    distance[v]=distance[u]+w
        return True
    
tc=int(input())
INF=int(1e9)
for _ in range(tc):
    n,m,o=map(int,input().split())
    edges=list()
    
    for _ in range(m):
        u,v,w=map(int,input().split())
        edges.append([u,v,w])
        edges.append([v,u,w])
    for _ in range(o):
        u,v,w=map(int,input().split())
        edges.append([u,v,-1*w])
    answer=bellman(n)
    if answer:
        print('NO')
    else:
        print('YES')