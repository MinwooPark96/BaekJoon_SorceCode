import sys #인라인으로 구현 필수

input=sys.stdin.readline
n,m=map(int,input().split())
matrix=[]
for i in range(n):
    #string=sys.stdin.readline()
    string=list(input())
    matrix.append([ord(i)-ord("A") for i in string])
    
visit=[0 for _ in range(26)]
max_path=1
dx=[1,0,-1,0]
dy=[0,-1,0,1]

visit[matrix[0][0]]=1
    
def Back(n,m,curpoint=[0,0],depth=0,curpath=1):
    global visit
    global max_path
    
    neighboor=[]
        
    for i in range(4):
        update_x=curpoint[0]+dx[i]
        update_y=curpoint[1]+dy[i]
        if 0<=update_x<n and 0<=update_y<m:
            neighboor.append([update_x,update_y])
    
    for child in neighboor:
        cur_x=child[0]
        cur_y=child[1]
        curalpha=matrix[cur_x][cur_y] 
        if not visit[curalpha]:
            visit[curalpha]=1
            curpath+=1
            if curpath>max_path:
                max_path=curpath
            Back(n,m,child,depth+1,curpath)
            visit[curalpha]=0
            curpath-=1
        
Back(n,m)      
print(max_path)