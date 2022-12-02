from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 9)
input=stdin.readline

def get_parent(v:int)->int:
    if parent[v]!=v:
        parent[v]=get_parent(parent[v])
    return parent[v]

def union(v1:int,v2:int)->int:
    parent_v1=get_parent(v1)
    parent_v2=get_parent(v2)
    if parent_v1>parent_v2:
        parent[parent_v1]=parent_v2
    else :
        parent[parent_v2]=parent_v1

def find(v1:int,v2:int)->bool:
    if get_parent(v1)==get_parent(v2):
        return True
    return False

n,m=map(int,input().split())
parent=[i for i in range(n+1)]

for _ in range(m):
    operator,v1,v2=map(int,input().split())
    if not operator :
        union(v1,v2)
    else:
        if find(v1,v2):
            print("YES")
        else:
            print("NO")