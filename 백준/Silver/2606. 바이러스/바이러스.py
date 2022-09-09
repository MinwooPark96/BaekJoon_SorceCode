#undirected graphic structure

n=int(input())
vertex=[i+1 for i in range(n)]

k=int(input())
neigh={}
for _ in range(k):
    v1,v2=map(int,input().split(" "))
    if neigh.get(v2):
        neigh[v2].append(v1)
    else:
        neigh[v2]=[v1]
    
    if neigh.get(v1):
        neigh[v1].append(v2)
    else:
        neigh[v1]=[v2]

count=0
visit={i:False for i in vertex}

def graph(n):
    global count
    for i in neigh[n]:
        if not visit[i]:
            visit[i]=True
            count+=1
            graph(i)

graph(1)
print(count-1)

