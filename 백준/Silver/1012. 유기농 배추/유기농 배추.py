#M,N,K=map(int,input().split(" "))
import copy
from collections import deque
import sys
#List=[[0,0],[1,0],[1,1],[4,2],[4,3],[4,5],[2,4],[3,4],[7,4],[8,4],[9,4],[7,5],[8,5],[9,5],[7,6],[8,6],[9,6]]


def neigh(point,matrix,n,m):
    x=point[0]
    y=point[1]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    result=[]
    for i in range(4):
        if (x+dx[i])<0 or (y+dy[i])<0 or (x+dx[i])>=n or (y+dy[i])>=m:
            continue
        else:
            result.append([x+dx[i],y+dy[i]])
    return result

def BFT(point):
    global land
    x=point[0];y=point[1]
    if not visit[x][y]:
        return
    my_deque.append(point)
    visit[x][y]=0
    land+=1
    while my_deque:
        point=my_deque.popleft()
        for child in neigh(point,Map,N,M):
            x=child[0];y=child[1]
            if visit[x][y]:
                visit[x][y]=0
                my_deque.append(child)

n=int(input())                

Answer=[]
for _ in range(n):
    N,M,K=map(int,sys.stdin.readline().strip().split())
    List=[]
    for _ in range(K):
        List.append(list(map(int,sys.stdin.readline().strip().split())))
    land=0
    Map=[[0]*M for i in range(N)]
    my_deque=deque()
    for point in List:
        Map[point[0]][point[1]]=1

    visit=copy.deepcopy(Map)

    for point in List:
        BFT(point)
    Answer.append(land)
for i in Answer:
    print(i)


