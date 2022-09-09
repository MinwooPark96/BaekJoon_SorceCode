import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n,m,start=map(int,input().split())
neigh={i+1:[] for i in range(n)}
vertecies=list(neigh.keys())
for i in range(m):
    v1,v2=map(int,input().split())
    neigh[v1].append(v2)
    neigh[v2].append(v1)
for i in neigh:
    neigh[i].sort(reverse=True)

rank={start:1}
visit=[False for i in range(n+1)]; visit[0]=True
count=2
def DFS(point):
    global count
    visit[point]=True
    for i in neigh[point]:
        if not visit[i]:#방문한적이 없다면
            visit[i]=True
            rank[i]=count
            count+=1
            DFS(i)
DFS(start)
for i in vertecies:
    try:
        print(rank[i])
    except:
        print(0)