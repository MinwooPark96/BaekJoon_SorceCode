import sys
import copy
#input=sys.stdin.readline
from collections import deque
n=int(input())
matrix=[]
for i in range(n):
    matrix.append([int(i) for i in input()])
    
visit=copy.deepcopy(matrix)
my_queue=deque()
def neigh(point,matrix,n):
    x=point[0]
    y=point[1]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    result=[]
    for i in range(4):
        if (x+dx[i])<0 or (y+dy[i])<0 or (x+dx[i])>=n or (y+dy[i])>=n:
            continue
        else:
            result.append([x+dx[i],y+dy[i]])
    return result
def BFT(point):
    global count
    global n
    x=point[0]
    y=point[1]
    visit[x][y]=0
    my_queue.append((i,j))
    count+=1
    while my_queue:
        point=my_queue.popleft()
        for child in neigh(point,matrix,n):
            x=child[0]
            y=child[1]
            if visit[x][y]:
                visit[x][y]=0
                my_queue.append(child)
                count+=1
    
answer=[]
count=0
for i in range(n):
    for j in range(n):
        if visit[i][j]: #방문한적이 없다면,
            BFT([i,j])
            answer.append(count)
            count=0
print(len(answer))
answer.sort()
for i in answer:
    print(i)