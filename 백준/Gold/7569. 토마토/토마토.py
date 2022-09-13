import copy
import sys
from collections import deque
m,n,h=map(int,input().split())

def neigh(h,n,m,point):
    dx=[-1,0,1,0,0,0]
    dy=[0,1,0,-1,0,0]
    dz=[0,0,0,0,1,-1]
    
    z=point[0]
    x=point[1]
    y=point[2]
    Answer=[]
    for i in range(6):
        child_x=x+dx[i]
        child_y=y+dy[i]
        child_z=z+dz[i]
        if child_x>=0 and child_x<n and child_y>=0 and child_y<m and child_z>=0 and child_z<h:
            Answer.append([child_z,child_x,child_y])
    return Answer

matrix=[]
startpoints=[]
for height in range(h):
    floor=[]
    rownum=0
    for column in range(n):
        #row=list(map(int,input().split()))
        row=list(map(int,sys.stdin.readline().rstrip().split()))
        for i in range(m):
            if row[i]==1:
                startpoints.append([height,rownum,i])
        rownum+=1
        floor.append(row)
    matrix.append(floor)
visit=copy.deepcopy(matrix)

def BFT(startpoints:list):
    day=0
    my_deque=deque()
    for startpoint in startpoints:
        my_deque.append(startpoint)
        visit[startpoint[0]][startpoint[1]][startpoint[2]]=1

    while my_deque:
        point=my_deque.popleft()
        neigh_list=neigh(h,n,m,point)
        for child in neigh_list:
            z=child[0]
            x=child[1]
            y=child[2]
            if not visit[z][x][y]:
                visit[z][x][y]=visit[point[0]][point[1]][point[2]]+1
                if visit[z][x][y]>day:
                    day=visit[z][x][y]
                my_deque.append(child)
    return day-1
check={visit[k][i][j] for k in range(h) for i in range(n) for j in range(m)}
button=1
if not 0 in check:
    print(0)
    button=0
if button:
    answer=BFT(startpoints)
    check={visit[k][i][j] for k in range(h) for i in range(n) for j in range(m)}
    if 0 in check:
        print(-1)
    else:
        print(answer)


