import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

time=0
scc=0
V,E=map(int,input().split())


child={i:[] for i in range(1,V+1)}
child_T={i:[] for i in range(1,V+1)}
visit=[0 for i in range(V+1)]
visit_T=[0 for i in range(V+1)]

finish=[0 for i in range(V+1)]
arrive=[0 for i in range(V+1)]

def DFT(u):
    global time
    if visit[u]==0:
        visit[u]=1
        time+=1
        arrive[u]=time
        for v in child[u]:
            if visit[v]==0:
                DFT(v)
        
        time+=1
        finish[u]=time
            
    
for _ in range(E):
    u,v=map(int,input().split())
    child[u].append(v)
    child_T[v].append(u)
    
for u in child.keys():
    DFT(u)
    
v_f=[[i,finish[i]] for i in range(1,V+1)]
f_v=[[finish[i],i] for i in range(1,V+1)]

scc=0
def DFT_T(u):
    if visit_T[u]==0:
        visit_T[u]=1
        for v in child_T[u]:
            if visit_T[v]==0:
                DFT_T(v)
v_f.sort(key=lambda x:x[1],reverse=True)        
for u,_ in v_f:
    if visit_T[u]==0:
        scc+=1
        DFT_T(u)
    
if scc==1:
    print('Yes')
else :
    print('No')