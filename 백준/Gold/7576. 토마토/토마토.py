import copy
import sys
from collections import deque
m,n=map(int,input().split())

def neigh(n,m,point):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    x=point[0]
    y=point[1]
    Answer=[]
    for i in range(4):
        child_x=x+dx[i]
        child_y=y+dy[i]
        if child_x>=0 and child_x<n and child_y>=0 and child_y<m:
            Answer.append([child_x,child_y])
    return Answer
matrix=[]
rownum=0
startpoints=[]
for _ in range(n):
    #row=list(map(int,input().split()))
    row=list(map(int,sys.stdin.readline().rstrip().split()))
    for i in range(m):
        if row[i]==1:
            startpoints.append([rownum,i])
    rownum+=1
    matrix.append(row)

visit=copy.deepcopy(matrix)

def BFT(startpoints:list):
    day=0
    my_deque=deque()
    for startpoint in startpoints:
        my_deque.append(startpoint)
        visit[startpoint[0]][startpoint[1]]=1

    while my_deque:
        point=my_deque.popleft()
        neigh_list=neigh(n,m,point)
        for child in neigh_list:
            x=child[0]
            y=child[1]
            if not visit[x][y]:
                visit[x][y]=visit[point[0]][point[1]]+1
                if visit[x][y]>day:
                    day=visit[x][y]
                my_deque.append(child)
    return day-1
check={visit[i][j] for i in range(n) for j in range(m)}
button=1
if not 0 in check:
    print(0)
    button=0
if button:
    answer=BFT(startpoints)
    check={visit[i][j] for i in range(n) for j in range(m)}
    if 0 in check:
        print(-1)
    else:
        print(answer)

