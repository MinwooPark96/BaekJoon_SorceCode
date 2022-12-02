N=int(input())
M=int(input())
parent=[i for i in range(N+1)]
row_num=1
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

for _ in range(N):
    row=list(map(int,input().split()))
    for i in range(row_num,N+1):
        if row[i-1]:
            union(row_num,i)
    row_num+=1
scedule=list(map(int,input().split()))
scedule=list(set(scedule))
p=get_parent(scedule[0])
flag=0
for i in scedule:
    if p!=get_parent(i):
        flag=1
        break

if flag:
    print('NO')
else :
    print('YES')

