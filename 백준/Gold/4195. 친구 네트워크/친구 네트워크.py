from collections import defaultdict
from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 5)
input=stdin.readline


def get_parent(v:int):
    if parent[v]!=v:
        parent[v]=get_parent(parent[v])
    return parent[v]
def union(v1:int,v2:int):
    a=get_parent(v1)
    b=get_parent(v2)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a
def find(v1,v2):
    if get_parent(v1)==get_parent(v2):
        return True
    return false

n=int(input())

for _ in range(n):
    m=int(input())
    parent=defaultdict(int)
    person_count=0
    translate=dict()
    parent_v=defaultdict(set)
    set_size=dict()
    for _ in range(m):
        name1,name2=input().split()
        if translate.get(name1)==None:
            translate[name1]=person_count
            parent[person_count]=person_count
            set_size[person_count]=1
            person_count+=1
            
        if translate.get(name2)==None:
            translate[name2]=person_count
            parent[person_count]=person_count
            set_size[person_count]=1
            person_count+=1
            
        p1=translate[name1]
        p2=translate[name2]
        if get_parent(p1)!=get_parent(p2):
            a=set_size[get_parent(p1)]+set_size[get_parent(p2)]
            union(p1,p2)
            p=get_parent(p1)
            set_size[p]=a
        p=get_parent(p1)    
        print(set_size[p])
        