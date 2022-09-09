import sys
from collections import deque

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
    neigh[i].sort()


my_queue=deque()
rank={start:1}
visit=[False for i in range(n+1)]; visit[0]=True
num=2
def BFS(point):
    global num
    visit[point]=True
    my_queue.append(point)
    
    while my_queue:
        interest=my_queue.popleft()
        for child in neigh[interest]:
            if not visit[child]:
                visit[child]=True
                rank[child]=num
                num+=1
                my_queue.append(child)
BFS(start)
for i in vertecies:
    try:
        print(rank[i])
    except:
        print(0)