import sys
input=sys.stdin.readline
n,m=map(int,input().split())

parent=[i for i in range(n)]

def get_parent(v:int):
    if v!=parent[v]:
        parent[v]=get_parent(parent[v])
    
    return parent[v]
    
def union(v1:int,v2:int):
    p1=get_parent(v1)
    p2=get_parent(v2)
    if p1>p2:
        parent[p1]=p2
    else:
        parent[p2]=p1
def find(v1:int,v2:int):
    if get_parent(v1)==get_parent(v2):
        return True
    return False
step=1
for _ in range(m):
    v1,v2=map(int,input().split())
    if find(v1,v2):
        print(step)
        break
    
    union(v1,v2)
    step+=1
if step==m+1:
    print(0)