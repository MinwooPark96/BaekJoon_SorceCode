import sys
from collections import deque

input=sys.stdin.readline
v,e,s=map(int,input().split())
edge={i:[] for i in range(1,v+1)}

for _ in range(e):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in edge:
    edge[i].sort()

answer=[s]
visit=[0 for i in range(v+1)]
visit[s]=1
def DFS(s:int):
    for child in edge[s]:
        if visit[child] == 0:
            visit[child] = 1
            answer.append(child)
            DFS(child)
DFS(s)
for i in answer:
    print(i, end=' ')
print()
answer=[s]
visit=[0 for i in range(v+1)]
visit[s]=1

queue=deque()
queue.append(s)

while queue:
    curver=queue.popleft()
    visit[curver]=1
    print(curver,end=' ')
    for child in edge[curver]:
        if visit[child]==0:
            visit[child]=1
            queue.append(child)
